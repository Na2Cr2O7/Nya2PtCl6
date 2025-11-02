import requests
import json
import os
import VisionUtil
import AIGCDetection
import threading
import spamFilter
filter = spamFilter.SpamFilter()
def startNewThread(target,args=()):
    t=threading.Thread(target=target,args=args)
    t.start()
detector=AIGCDetection.AIGCDetector()
MODEL=''
#Temp
MODEL='jingyaogong/minimind2:latest'
# Flask应用的URL
url = 'http://127.0.0.1:5000'

def getAnswer(question:str,image:str=None)->str:
    posturl=url+f'/anyModel/{question}'
    try:
        if image is not None:
            imageDescription=VisionUtil.getImageDescription([image])
            posturl=url+f'/anyModel/{question};图片描述:{imageDescription}'
        response = requests.post(posturl)
        if response.status_code == 200:
            result = json.loads(response.text)
            answer=result['answer']
            if detector.isAIGC(answer) or filter.isSpam(answer):
                return getAnswerbyOllama(question,image)
            return answer
        else:
            return ''
    except:
        return ''
import ollama
def validifyModel(model:str)->None:
    try:
        ollama.chat(model)
    except ollama.ResponseError as e:
        print('Error:', e.error)
        if e.status_code == 404:
            print('Model not found, trying to pull it from Ollama...')
            ollama.pull(model)
startNewThread(validifyModel,args=(MODEL,))
def getAnswerbyOllama(question:str,image:str=None)->str:
    validifyModel(MODEL)
    res=ollama.chat(model=MODEL,stream=True,messages=[{"role":"system","content":"请用不超过三句话简洁的回复"},{"role":"user","content":question}])
    text=''
    for i in res:
        _=i['message']['content']
        print(_,end='')
        text+=_
    print('\n')
    text=text.replace('\n\n','\n').replace('/n','\n').replace('**','')
    detector.isAIGC(text)
    return text
if __name__ == '__main__':
    # print(getAnswer('碎觉碎觉,晚安啦，大氵怪们'))
    print(getAnswerbyOllama('你是把这个地方虚无化了吗','dbg.jpg'))
