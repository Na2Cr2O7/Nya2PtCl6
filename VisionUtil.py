'''
visionutil.py
图像视觉工具
'''
import Constant
import ollama
import os
from time import *
from PIL import Image
import LocalTranslate
import Constant
try:
    from ascii_magic import AsciiArt
except ImportError as e:
    print(e)
def viewImage(image_path):
    try:
        a=AsciiArt.from_image(image_path)
        a.to_terminal()
    except:
        print("ascii_magic not installed")
def validifyModel(model:str)->None:
    try:
        ollama.chat(model)
    except ollama.ResponseError as e:
        print('Error:', e.error)
        if e.status_code == 404:
            print('Model not found, trying to pull it from Ollama...')
            ollama.pull(model)
MAXIMUMIMAGEPIXELS=640*480
port=5050
def resizeImage(imagePath:str,maxPixels=MAXIMUMIMAGEPIXELS):
    img = Image.open(imagePath)
    sizeX,sizeY=img.size
    if sizeX*sizeY>maxPixels:
        sizeX*=0.9
        sizeY*=0.9
    img=img.resize((int(sizeX),int(sizeY)))
    img.save(imagePath)
    return imagePath
def getAnswerImage3(imagePaths:list,limitation=1,translate=False):
    validifyModel(Constant.VISIONMODEL)
    for i in imagePaths:
        viewImage(i)
        print('\n\n')
    start=time()
    res = ollama.chat(
        model=Constant.VISIONMODEL,
        messages=[
            {
                'role': 'user',
                'content': '使用中文描述图片:',
                'images': [os.path.abspath(resizeImage(i)) for i in imagePaths][:limitation]
            }
        ]
    )

    print(res['message']['content'])
    result=res['message']['content']
    if translate:
        try:
            result=LocalTranslate.translate(result)
            if result.strip()=='':
                result=' '
        except:
            pass
    end=time()
    print('Time used:',end-start) 
    return result
def getAnswerImage2(imagePath:str,translate=True):
    if os.path.exists('VisionInput.png'):
        os.remove('VisionInput.png')
    os.rename(imagePath,'VisionInput.png')
    start=time()
    while not os.path.exists('VisionOutput.txt'):
        sleep(0.1)
    with open('VisionOutput.txt','r',encoding='utf-8') as f:
        result=f.read()
    os.remove('VisionOutput.txt')
    try:
        result=LocalTranslate.translate(result)
    except:
        pass
    end=time()
    print('Time used:',end-start) 
    return result
    #os.system(Constant.TORCHPYTHONPATH+' '+'VisionUtil4.py')
import requests
def getAnswerImage(imagePaths:list,limitation=1,translate=True):
    start=time()
    imagePath=imagePaths[:limitation]
    answers=''
    for i in imagePath:
        i=os.path.abspath(i)
        answer=requests.post(f'http://127.0.0.1:{port}/{i}')
        if answer.status_code!=200:
            return ''
        answerJson=answer.json()
        answers+=answerJson['answer']+'\n'
    end=time()
    print('Time used:',end-start) 
    return answers
        

def getImageDescription(imagePath:list):
    if isinstance(imagePath,str):
        imagePath=[imagePath]
    return getAnswerImage(imagePath)


if __name__=='__main__':
    imagePath=r"f6e26e03ed439104a25d1bc9850615d6.png"
    print(getImageDescription(imagePath))