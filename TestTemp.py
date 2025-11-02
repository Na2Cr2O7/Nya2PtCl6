import ollama
from random import choice
import DrawUtilsII as DrawUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from RichText import *
from time import sleep,time
from Constant import *
def Sleep(t):
    sleep(t)
import os
MODEL='qwen2:0.5b'
import CopyTest
ModalWords=['呢','哦','喵','呀']#语气词

def sendAnswer(answer,inputBox,refuseEmotions=False,MAXIMUMCOUNT=500):
    temp=''
    wordCount=0
    for text in answer:
        
        if text=='\n':
            wordCount+=2
            inputBox.send_keys(temp)
            inputBox.send_keys(Keys.ENTER)
    
            #print(temp)
            temp=''
            sleep(0.01)
        else:
            temp+=text
            wordCount+=1
        if wordCount>MAXIMUMCOUNT:
            break
    inputBox.send_keys(temp)
    #print(temp)
    Sleep(4)
def getAnswer(question,interpreted=True,model=MODEL,allowRag=False,Prompts=[],NewPrompts=False)->str:
    #qwen2:0.5b,qwen2:1.5b,qwen2
    if NewPrompts:
        for i in question.split('\n'):
            if '#' in i:
                Prompts.append(i)
        for i in Prompts:
            question=question.replace(i,'')
        PROMPT='#扮演一只猫娘回复\n#只要结果部分\n'+'\n#'.join(Prompts)+question
    else:
        PROMPT=question
    if allowRag and len(question)<50 and len(question)>10:
        text='RAG'
    else:
        res=ollama.chat(model=model,stream=False,messages=[{"role":"user","content":PROMPT}])
        text=res['message']['content']
    text=text.replace('\n\n','\n').replace('/n','\n').replace('**','')
    if interpreted:
        text=text.replace("#","\n").replace("人工智能模型","猫娘").replace("**","").replace("AI语言模型","猫娘").replace("AI","猫娘")
        temp=''
        for k in text:
            
            if k in '。！，':
                temp+=choice(ModalWords)+k
            else:
                temp+=k
        
        text='喵~ '+temp

    a=1
    a2=1
    while a!=-1 or a2!=-1:
        a=text.find('【')
        a2=text[a:].find('】')
        text=text.replace(text[a:a+a2+1],'')

    return text
if __name__=='__main__':
    question='#英文\n你好，请问你是哪里人？#图片描述:一杯开水'
    print(getAnswer(question,NewPrompts=True))
    print('-----------')
    print(getAnswer('以人为主题发一条帖子的标题……只要标题,小于30字',False,allowRag=False).replace('"',''))
    image=DrawUtils.drawPicture()
    image.save('test.SS.jpg')
    answer=debugText
    wd=webdriver.Firefox()
    
    if True:
        wd.get('https://www.miyoushe.com/ys/')
        Sleep(12)
        try:
            wd.find_element(By.CSS_SELECTOR,".header__avatar > img:nth-child(1)").click()
        except:
            wd.find_element(By.CSS_SELECTOR,".header__avatarwrp").click()
        Sleep(12)
        r=wd.find_element(By.ID,"mihoyo-login-platform-iframe")
        Sleep(12)
        wd.switch_to.frame(r)
        wd.find_element(By.CSS_SELECTOR ,'#tab-password').click()
        wd.find_element(By.CSS_SELECTOR ,'#username').send_keys(ACCOUNT)
        wd.find_element(By.CSS_SELECTOR ,'#password').send_keys(PASSWORD)
        wd.find_element(By.CSS_SELECTOR ,'.el-checkbox__inner').click()
        wd.find_element(By.CSS_SELECTOR ,'button.el-button').click()
        Sleep(12)
    
    wd.get('https://www.miyoushe.com/ys/article/58733041')
    sleep(12)
    inputBox=wd.find_element(By.ID,'reply').find_element(By.CLASS_NAME,"ql-editor")
    if True:
                            try:
                                richtext=containsRichText(answer)
                                
                                if richtext:
                                    sendAnswer(richtext[1],inputBox,MAXIMUMCOUNT=1000)
                                    wd.find_element(By.CSS_SELECTOR,'.icon-tupian1').click()
                                    CopyTest.uploadSth(os.path.abspath(image))
                            except:
                                pass