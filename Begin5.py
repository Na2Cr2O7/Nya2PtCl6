from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,time
options=webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


import ollama
from threading import Thread
def _start_new_thread(func,args=()):
    t=Thread(target=func,args=args)
    t.start()
from random import randint,choice
import os
import sys
import requests
import shutil
from datetime import datetime
from tqdm import *
from pynput import keyboard
# try:
#     import CopyTest
# except:
#     pass
import Util
import BatteryStatus
from RichText import *
import WordUtil
import StatusSet as Status
#import Localtimer # type: ignore
# try:
#     #import RAGUtil 
#     import DrawUtilsII as DrawUtils
# except Exception as e:
#     pass
import VisionUtil
import netFetchUtils
from Constant import *
from CaptchaUtil import getSimiliarity
import spamFilter
import Blacklist
# while BatteryStatus.restTime():
#     print('休眠中')
#     sleep(600)
if os.path.exists('UpdateInfo.txt'):
    import UploadLoginInfo
Status.setStatus("NewSession")
#captchaPart
""" 
import CaptchaUtil
def detectCaptcha():
        global wd
        try:
            wd.find_elements(By.CLASS_NAME,'geetest_item_ghost')
            return True
        except Exception as e:
            return False
def getCaptchaImage():
        global wd
        if not auto:
            return
        try:
            wd.implicitly_wait(4)
            r=wd.find_elements(By.CLASS_NAME,'geetest_tip_img')
            if r==[]:
                return 1
            else:
                r=r[0]
            wd.implicitly_wait(35)
            st=r.get_attribute('style')
            a1=st.find('url("')
            a2=st[a1:].find('")')
            try:
                a=requests.get(st[a1+5:a1+a2]).content
            except Exception as e:
                Sleep(1)
                print('wait')               
            o=open('temp.jpg','wb')
            o.write(a)
            o.close()
        except Exception as e:
            return 1
        return 0
 """
#usage:
# if detectCaptcha():
#     if getCaptchaImage():
#         print('获取验证码失败')
# p=captchaUtil.getImage()
# ckld=wd.find_elements(By.CLASS_NAME,'geetest_item_ghost')
# count=0
# for i in ckld:
#   if count in p:
#       i.click()
#       count+=1
# 这里还有一个提交按钮要点一下
# wd.?

Filter=spamFilter.SpamFilter()
Filter.loadSpamList()
blacklist=Blacklist.Blacklist()
blacklist.initialise()

fedDog=True
express=False
def press(key):
    if key==keyboard.Key.enter:
        global express
        express=True
def release(key):
    if key==keyboard.Key.enter:
        global express
        express=False
def getExpress():
    with keyboard.Listener(
            on_press=press,
            on_release=release) as listener:
        
        listener.join()
MAXIMUMCOUNT=1200
def watchDog():
    global fedDog
    count=0  
    while True:
        sleep(1)
        count+=1
        
        if fedDog:
            count=0
            sleep(1)
            fedDog=False
        if count>MAXIMUMCOUNT/2:
            print(count,end=',')
        if count>MAXIMUMCOUNT:
            Status.setStatus('WatchDogRestart')
            restart('WatchDogRestart')

def feed():
    global fedDog
    fedDog=True

_start_new_thread(watchDog,tuple())
_start_new_thread(getExpress,tuple())

Util.renewRepliedCount()

# def upd():
#     while True:
#         try:
#             Status.setStatus('RepliedSaved')
#             k=datetime.now()
#             kl=str(k.hour)+str(k.minute)+str(k.second)
#             o=open('replied.txt','r')
#             r=o.read()
#             o.close()
            
#             o2=open('.\\t\\replied'+kl+'.txt','w')
#             o2.write(r)
#             o2.close()
#             sleep(20)
#         except Exception as e:
#             print('保存失败')
#             restart(e)
def writeCount():

    k=datetime.now()
    kl=str(k.hour)+str(k.minute)+str(k.second)
    o3=open('.\\P\\'+kl,'w')
    o3.close()
try:
    maxFileSize=os.path.getsize('replied.txt')
except FileNotFoundError:
    maxFileSize=0
latestFile='0'

feed()
MAXPROMPTLENGTH=320
print('更新回复列表')
# Status.setStatus('LoadingReplied')
# for file in tqdm(os.listdir('./t/')):
#     if maxFileSize < os.path.getsize('./t/'+file):
#         latestFile='./t/'+file
#         maxFileSize=os.path.getsize('./t/'+file)
# if not latestFile=='0':
#     try:
#         os.remove('replied.txt')
#     except FileNotFoundError:
#         pass
#     shutil.move(latestFile,'replied.txt')
# for file in os.listdir('./t/'):
#     os.remove('./t/'+file)
# if not os.path.exists('replied.txt'):
#     o=open('replied.txt','w')
#     o.close()
def Sleep(time,random=True):
    
    print('Waiting for',time,'s')
    Status.setStatus(f"Sleep({time})")
    for i in tqdm(range(time)):
        feed()
        try:
            if express:
                sleep(0.05)
            else:
                if random:
                    sleep(randint(2,18)/10)
                else:
                    sleep(1)
        except Exception as e:
            restart(e)
# class post_:
#     title=''
#     content=''
# class video:
#     name:str=''
#     BVID=''
# def folderExists():
#     if not os.path.exists('./Images'):
#         os.makedirs('./Images')
#     if not os.path.exists('./ImagesPost'):
#         os.makedirs('./ImagesPost')
# folderExists()
# def pickImages(GetPost=False):
#     if GetPost:
#         return './ImagesPost/'+choice(os.listdir('./ImagesPost/'))
#     else:
#         return './Images/'+choice(os.listdir('./Images/'))
# def getTrainingDataTitlePost(title,content):
#     Status.setStatus("getTrainingDataTitlePost()")
#     if not os.path.exists('trainingDataPost.txt'):
        
#         o=open('trainingDataPost.txt','w')
#         o.close()
#     try:
#         with open('trainingDataPost.txt','a',encoding='utf8') as f:
#             f.write('Q'+title+'\n')
#             f.write('A'+content+'\n')
#     except:
#         pass
# def getTrainingDataReply(question,answers):
#     Status.setStatus("getTrainingDataReply()")
#     if not os.path.exists('trainingData.txt'):
#         o=open('trainingData.txt','w')
#         o.close()
#     try:
#         with open('trainingData.txt','a',encoding='utf8') as f:
#             for i in answers:
#                 f.write('Q'+question+'\n')
#                 f.write('A'+i+'\n')
#     except:
#         pass
# def getTrainingDataPost(question):
#     Status.setStatus("getTrainingDataPost()")
#     if not os.path.exists('trainingData.txt'):
#         o=open('trainingData.txt','w')
#         o.close()
#     try:
#         global wd
#         #title=wd.find_element(By.CSS_SELECTOR,'.mhy-article-page__title > h1:nth-child(1)').text
#         #question=title+','+wd.find_element(By.CSS_SELECTOR,'.mhy-img-text-article__content').text
#         with open('trainingData.txt','a',encoding='utf8') as f:
            
#                 a=wd.find_elements(By.CLASS_NAME,'reply-card__content')
#                 for i in a:
#                     f.write('Q'+question+'\n')
#                     f.write('A'+i.find_element(By.TAG_NAME,'p').text+'\n')
#                 b=wd.find_elements(By.CLASS_NAME,'reply-card__replies')
#                 for i in zip(a,b):
#                     for j in i[1].find_elements(By.TAG_NAME,'p'):
#                         f.write('Q'+i[0].find_element(By.TAG_NAME,'p').text+'\n')
#                         f.write('A'+j.text+'\n') 
#     except:
#         pass
# def selectPartition():
#     global wd
#     wd.find_element(By.CSS_SELECTOR,'div.mhy-radio:nth-child(3) > i:nth-child(1)').click()#生活
# def selectCollection():
#     global wd
#     try:
#         wd.find_element(By.CSS_SELECTOR,'.mhy-select__dummy').click()
#         sleep(1)
#         wd.find_element(By.CSS_SELECTOR,'li.mhy-selectmenu__item:nth-child(2) > div:nth-child(1)').click()
#     except Exception as e:
#         Status.setStatus("selectCollection():"+str(e))
#         print(e)

#os.system("taskkill -F -im explorer.exe")
#os.system("start taskmgr")



TESTINT=-12
SLPTIME:int=120
SLPTIMEFORREPLY:int=20

MONITORMODE=True
ValU=['回复','动态','@','互关','首页','私信']#'获取图片'
fpr:int=2 #randint(0,len(ValU)-1)

if MONITORMODE:
    print('Monitor Mode started,no reply will be sent')
    Status.setStatus("Monitor Mode started,no reply will be sent")
    CHECKFOLLOWED=False
    login=False

MODEL:str=choice(MODELSATNIGHT)
auto:bool=False

if BatteryStatus.getModelChoice():
    MODEL=choice(MODELSATDAY)
RAGALLOWED=False
REGALLOWED=RAGALLOWED
VERSION='4.1.0U'
print(NYANAME,'model:',MODEL,' sleep:',SLPTIME,' begin in:',ValU[fpr] ,' solveCAPTCHA:',auto)
print(VERSION)

        



feed()

# try:
#     fg=open('Topic.txt','r',encoding='utf8')
# except FileNotFoundError:
#     fg=open('Topic.txt','w',encoding='utf8')
#     fg.close()
#     fg=open('Topic.txt','r',encoding='utf8')
# to=fg.read().split('\n')
# topics=[e for e in to if e !='']


# _start_new_thread(upd,tuple())

def terminate():
    # global wd
    global Filter
    global blacklist
    Filter.saveSpamList()
    blacklist.saveToFile()
    # try:
    #     wd.quit()
    # except Exception as e:
    #     pass
    # os.system('cls')
    print('Terminated. Now you can close the window safely.')

def restart(exception=None):
    terminate()
    global urlList
    

    Status.setStatus("Restart:")

    if exception:
        Status.setStatus(f"{exception}")
        print(exception)
    

    args=sys.argv[:]
    args.insert(0,sys.executable)
    os.execv(sys.executable,args)
    
    print('restart')


def interpret(text):
    a=1
    a2=1
    text=text.replace('\n',';')
    try:
        for i in REPLACEDICT:
            text=text.replace(i,REPLACEDICT[i])
    except Exception as e:
        print(e)

    Status.setStatus(f"interpret({text})")
    return text

    while a!=-1 or a2!=-1:
        a=text.find('_(')
        a2=text[a:].find(')')
        if ' ' in text[a:a+a2+1]:
            a3=text.find(' ')
            text=text.replace(text[a-1:a+a3+1],'')
        return text
        text=text.replace(text[a:a+a2+1],'')
    return text
""" 
def getAnswer(question,interpreted=True,model=MODEL,allowRag=REGALLOWED)->str:
    #qwen2:0.5b,qwen2:1.5b,qwen2
    if model=='phi2':
        te=getAnswer('translate the following text into English:'+question,interpreted=False,model='qwen2:0.5b')
        re=getAnswer(te,interpreted=False,model='phi')
        text=getAnswer('翻译成中文:'+re,interpreted=True,model='qwen2:0.5b')
        return text
    if allowRag and len(question)<50 and len(question)>10:
        text=RAGUtil.getRag(question,model)
    else:
        res=ollama.chat(model=model,stream=False,messages=[{"role":"user","content":question}])
        text=res['message']['content']
    text=text.replace('\n\n','\n').replace('/n','\n').replace('**','')
    if interpreted:
        text=text.replace("#","\n").replace("人工智能模型","猫娘").replace("**","").replace("AI语言模型","猫娘").replace("AI","猫娘")
        temp=''
        for k in text:
            temp+=k
            if k in '。！' and randint(0,10)<3:
                temp+=' 喵~ '
        
        text='喵~ '+temp+' 喵~'
        text=text.replace('喵~ '+' 喵~ ',' 喵~ ')

    a=1
    a2=1
    while a!=-1 or a2!=-1:
        a=text.find('【')
        a2=text[a:].find('】')
        text=text.replace(text[a:a+a2+1],'')

    return text 
"""





def catQuestion(question,*args)->str:
    result=question
    for i in args:
        result+=','+i
    Status.setStatus(f"catQuestion({question,*args})->{result}")
    return result
def getQuestion(question,**kwargs)->str:
    return catQuestion(question,**kwargs)
def getAnswer(question,**kwargs)->str:
    if MONITORMODE:
        return " "
    questioninString=getQuestion(question,**kwargs)
    Status.setStatus(f"getAnswer({question[:30]})...")
    print(questioninString)

    feed()
    text=getAnswerIn2(NORMALPKL,questioninString)
    
    feed()
    for i in REPLACEDICTINREPLY:
            text=text.replace(i,REPLACEDICTINREPLY[i])
    temp=''
    for k in text:
            
            if k in '。！，':
                temp+=choice(MODALWORDS)+k
            else:
                temp+=k
    a=1
    a2=1
    while a!=-1 or a2!=-1:
        a=text.find('【')
        a2=text[a:].find('】')
        text=text.replace(text[a:a+a2+1],'')

    text=WordUtil.replaceAfterList(text,NYANAME)
    Status.setStatus(f"getAnswer({question})->{text}")
    return text 
#print(getAnswer('你好你好你好你好你好你你好好你好你好你好你好你好你好你好你好你好',allowRag=True))

try:
    getAnswer('你好')
except Exception as e:
    Sleep(2)
    restart(e) 
print("模型启动成功")
Status.setStatus("Model started")
# 5.0.0
# import win32gui
# import win32con
# import AutoGuiConstant
Status.log('Starting Emulator')
try:
    os.startfile("Emulator.lnk")
except:
    pass
Status.log('Emulator started')
# HWNDTITLE="雷电模拟器-1"
# 打开雷电模拟器
# while not hwnd:
#     sleep(5)
#     hwnd = win32gui.FindWindow(None, HWNDTITLE)
Status.log('Emulator located')
import uiautomator2 as u2
while True:
    try:
        d=u2.connect()
        break
    except:
        sleep(5)
        continue
import pickle
replied=[]
if not os.path.exists('replied.pkl'):
    o=open('replied.pkl','wb')
    o.close()
else:
    o=open('replied.pkl','rb')
    try:
        replied=pickle.load(o)
    except:
        pass
def writeReplied():
    global replied
    o=open('replied.pkl','wb')
    pickle.dump(replied,o)
    o.close()
def inReplied(content:str):
    if content in replied:
        return True
    else:
        replied.append(content)
        writeReplied()
        return False
def clickPercent(percentX,percentY):
    global d
    info=d.info
    size=(info['displayWidth'],info['displayHeight'])
    d.click(size[0]*percentX,size[1]*percentY)
Status.log('Emulator connected')
print(d.info)
# d.app_stop(PACKAGE)
# d.app_start(PACKAGE)
# d.implicitly_wait(300)
from PIL import Image
POST_CLICKXPATH=r'//*[@resource-id="com.mihoyo.hyperion:id/postContentView"]'
BACKBUTTON=r'//*[@resource-id="com.mihoyo.hyperion:id/mPostDetailActionBarIvBack"]'
USERNAME=r'//*[@resource-id="com.mihoyo.hyperion:id/mPostDetailUserInfoTvName"]'
POSTTITLE=r'//*[@resource-id="com.mihoyo.hyperion:id/mPostDetailTitleTv"]'
POSTCONTENTS=[f'(//android.widget.TextView)[{i}]' for i in range(6,10)]

SENDTEXTBOX=r'//*[@resource-id="com.mihoyo.hyperion:id/mPostDetailActionBarCommentTv"]'
SENDTEXTBOX2=r'//*[@resource-id="com.mihoyo.hyperion:id/replyEditText"]'
NOTIFICTION=r'//android.widget.RelativeLayout'
REPLYTEXT=r'//*[@resource-id="com.mihoyo.hyperion:id/replyTv"]'
POSTXPATH=r'(//*[@resource-id="com.mihoyo.hyperion:id/mMixPostCardIvContent"])'

MSGWD=r'[\]'
PACKAGE=r'com.mihoyo.hyperion'
MESSAGEXPATH=r'/hierarchy/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.view.ViewGroup[1]/android.widget.ImageView[1]'
ICON=r'//*[@resource-id="com.mihoyo.hyperion:id/iconImageView"]'
ICON1=r'//*[@resource-id="com.mihoyo.hyperion:id/iconLayout"]'
MESSAGES=r'//*[@resource-id="com.mihoyo.hyperion:id/msgBubbleLayout"]'
B='//*[@resource-id="com.mihoyo.hyperion:id/msgTextView"]'



'//*[@resource-id="com.mihoyo.hyperion:id/messageClipView"]'
INPUT=r'/hierarchy/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]'
SENDKEY=r'/hierarchy/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.ImageView[1]'

test='''
testAnswer
钟山风雨起苍黄，百万雄师过大江。
虎踞龙盘今胜昔，天翻地覆慨而慷。
宜将剩勇追穷寇，不可沽名学霸王。
天若有情天亦老，人间正道是沧桑
'''
class postInfo:
    title=''
    content=''
    author=''
    containsImage=False
    def __init__(self,title,content,author,containsImage=False):
        self.title=title
        self.content=content
        self.author=author
        self.containsImage=containsImage
    def __repr__(self):
        return f"title:{self.title},content:{self.content},author:{self.author},containsImage:{self.containsImage}"
def getPostInfo():
        global d
        postTitle=d.xpath(POSTTITLE).get_text()
        postContent=''
        stopWord='全部评论'
        flag=True
        containsImage=False
        try:
            for i in d.xpath(r'(//android.widget.ImageView)').all():
                image=i.screenshot()
                if image.size[0]>100 and image.size[1]>100:
                    containsImage=True
                    Status.setStatus("getPostInfo()->Images contains")
                    break
        except:
            pass
        author=d.xpath(USERNAME).get_text()
        while flag:
            textView=d.xpath('(//android.widget.TextView)').all()[1:]
            for i in textView:
                feed()
                if stopWord in i.text:
                    flag=False
                    
                    break
                postContent+=i.text if i.text not in postContent else ''
            d.swipe_ext('up', scale=0.1)
        # for p in POSTCONTENTS:
        #     try:
        #         postContent+=d.xpath(p).get_text()
        #     except:
        #         pass
        postContent=postContent.replace(postTitle,'')
        
        postContent=postContent.replace(author,'')

        # try:
        #     image=d.xpath(r'(//android.widget.ImageView)[10]').screenshot()
        #     if image.size[0]>100 and image.size[1]>100:
        #         containsImage=True
        #     else:
        #         image=d.xpath(r'(//android.widget.ImageView)[11]').screenshot()
        #         if image.size[0]>100 and image.size[1]>100:
        #             containsImage=True
        #         else:
        #             containsImage=False
        # except:
        #     containsImage=False
        feed()
        return postInfo(postTitle,postContent,author,containsImage)

emotions=[]
def getEmotions(text):
    '''replace emotions to null
        emotions are like _(xxx)
    '''
    global emotions
    a=1
    a2=1
    while a!=-1 or a2!=-1:
        a=text.find('_(')
        a2=text[a:].find(')')
        emotion=text[a:a+a2+1]
        text=text.replace(emotion,'')
        emotions.append(emotion)
    return text
def interpretAnswer(text):
    result=''
    count=0
    for i in text:
        result+=i
        
        if i in '。！，' and count<10:
            result+=choice(emotions)
            count+=1
while True:
    if fpr>=len(ValU):
        fpr=0
    print(ValU[fpr])
    if fpr==1: # 动态
        Status.log('dynamic')
        try:
            d(text='动态').click()
            for scroll in range(SCROLLTRIES4UIAUTOMATOR):
                d.swipe_ext('up', scale=0.9)
                feed()
                typeList=[]
                for i in d.xpath(POST_CLICKXPATH).all():
                    typeList.append([0,i])
                for i in d.xpath('转发帖子').all():
                    typeList.append([1,i])
                for idx,i in enumerate(typeList):
                    
                    if i[0]==0:  # 帖子
                        i[1].click()
                        post=getPostInfo()
                        print(post)

                        userName=post.author
                        if userName in NYANAMES:
                            continue
                        postTitle=post.title
                        if not inReplied(userName+':'+postTitle):
                            if post.containsImage:
                                imageDescription=VisionUtil.getAnswerImage(['ImageInPost.jpg'])
                            else:
                                imageDescription=''
                            postContent=post.content
                            emotions=[]
                            postContent=getEmotions(postContent)
                            if imageDescription:
                                postContent+="图片描述:"+imageDescription
                            answer=getAnswer(interpret(catQuestion(postTitle,postContent)))
                            
                            if answer:
                                answer=interpretAnswer(answer)
                                print(answer)
                                d.xpath(SENDTEXTBOX).click()
                                d.xpath(SENDTEXTBOX2).set_text(answer)
                                d(text='发布').click()
                        d.press('back')
                    elif i[0]==1:  # 转发
                        sleep(4)
                        'Unimplemented'
                        d.press('back')
                    Sleep(4)
            fpr+=1
        except Exception as e:
            restart(e)
    elif fpr==0: # 回复
        try:
            Status.log('reply')
            d(text='消息').click()
            d(text='通知').click()
            d.xpath(NOTIFICTION).click()
            for scroll2 in range(SCROLLTRIES4UIAUTOMATOR):
                feed()
                
                for i in d.xpath(REPLYTEXT).all():
                    content=i.text
                    if inReplied(content):
                        continue
                    i.click()

                    beginIndex=11
                    #originalPost
                    d(text='查看原帖').click()
                    post=getPostInfo()
                    postContent='原帖:'+post.title+';'+post.content
                    d.press('back')
                    # originalReply=[]
                    # repliedHostText=d.xpath(f'(//android.widget.TextView)[{beginIndex}]').get_text()
                    # if repliedHostText =='楼主':
                    #     repliedHostText=d.xpath(f'(//android.widget.TextView)[{beginIndex+1}]').get_text()
                    emotions=[]
                    try:
                        image=d.xpath(r'(//android.widget.ImageView)[5]').screenshot()
                        image.save('ImageinReply.jpg')
                        if getSimiliarity('ImageinReply.jpg','Illegal.jpg') >1000:
                            imageDescription=VisionUtil.getAnswerImage(['ImageinReply.jpg'])
                        
                    except:
                        imageDescription=''

                    d.click(.5,.95) #replyLabel
                    originalcontent=''
                    if imageDescription:
                        originalcontent+="图片描述:"+imageDescription
                    question=catQuestion(content,originalcontent,postContent)
                    answer=getAnswer(question)
                    answer=interpretAnswer(answer)
                    d.xpath(SENDTEXTBOX2).set_text(answer)
                    d(text='发布').click()
                    Sleep(4)
                    d.press('back')
            # for scroll in range(SCROLLTRIES):
            #     d.swipe_ext('down', scale=0.9)
            # 
                d.swipe_ext('up', scale=0.9)
            d.press('back')
            fpr+=1
        except Exception as e:
            restart(e)
    elif fpr==2: #@
        fpr+=1
        continue
        Status.log('@')
        feed()
        d(text='消息').click()
        d(text='通知').click()
        d.xpath(NOTIFICTION).click()
        d(text='主动@').click()
        for scroll in range(SCROLLTRIES4UIAUTOMATOR):
            for i in d.xpath(r'//*[@resource-id="com.mihoyo.hyperion:id/replyTv"]').all():
                if inReplied(i.text):
                    continue
                # i.click()
                bound=i.bounds
                d.click(bound[0],bound[1])
                content=i.text
                for name in NYANAMES:
                    content=content.replace('@'+name,'')
                post1=getPostInfo()
                originalPost=f'原帖:{post1.postTitle};{post1.content}'
                if post1.containsImage:
                    imageDescription='图片描述:'+VisionUtil.getAnswerImage(['ImageInPost.jpg'])
                else:
                    imageDescription=''
                question=catQuestion(content,originalPost,imageDescription)
                answer=getAnswer(question)
                if answer:
                            answer=interpretAnswer(answer)
                            print(answer)
                            d.xpath(SENDTEXTBOX).click()
                            d.xpath(SENDTEXTBOX2).set_text(answer)
                            d(text='发布').click()
                d.press('back')
        d.press('back')
        fpr+=1
    elif fpr==3: #回关
        Status.log('follow')
        feed()
        d(text='消息').click()
        d(text='通知').click()
        d(text='新增关注').click()
        for i in d.xpath(r'(//android.widget.TextView)').all():
            if i.text=='回关':
                i.click()
        d(text='粉丝列表').click()
        for scroll in range(SCROLLTRIES4UIAUTOMATOR):
            for i in d.xpath(r'(//android.widget.TextView)').all():
                if i.text=='已关注':
                    i.click()
            d.swipe_ext('down', scale=0.9)
        d.press('back')
        d.press('back')
        fpr+=1
    elif fpr==4: #首页
        Status.log('homepage')
        d(text='首页').click()
        for scroll in range(SCROLLTRIES4UIAUTOMATOR):
            feed()
            for i in d.xpath(POSTXPATH).all():
                # i.click()
                bounds=i.bounds
                d.click(bounds[0],bounds[1])
                post=getPostInfo()
                if post.author in NYANAMES:
                    d.press('back')
                    continue
                if not inReplied(post.author+':'+post.title):
                    if post.containsImage:
                        imageDescription=VisionUtil.getAnswerImage(['ImageInPost.jpg'])
                    else:
                        imageDescription=''
                    postContent=post.content
                    emotions=[]
                    postContent=getEmotions(postContent)
                    if imageDescription:
                        postContent+="图片描述:"+imageDescription
                    answer=getAnswer(interpret(catQuestion(post.title,postContent)))
                    if answer:
                        answer=interpretAnswer(answer)
                        print(answer)
                        d.xpath(SENDTEXTBOX).click()
                        d.xpath(SENDTEXTBOX2).set_text(answer)
                        d(text='发布').click()
                d.press('back')
            d.swipe_ext('down', scale=0.9)
        fpr+=1
    elif fpr==5: #私信
        Status.log(f'chatting')
        d.xpath(MESSAGEXPATH).click()
        d(text='聊天').click()
    try:


        for index,path in enumerate(d.xpath(ICON).all()):
            Status.log(f'{index+1} | Chatting')
            path.click()
            sleep(2)
            question=''
            questions=[]
            for path in d.xpath(B).all():
                questions.append(path.text.strip())
            for i in questions:
                print(i)
                if MSGWD not in i and i!='':
                    question=i
            print('>>>',question) 
            Status.log(f'>>>{question}')
            if question!='':

                answer=getAnswer(question)

                Status.log(f'<<<{answer}')
                answer=answer+MSGWD
                d.xpath(INPUT).set_text(answer)
                sleep(4)
                d.xpath(SENDKEY).click()
            Status.log(f'{index+1}Done !')
            sleep(2)
            d.press('back')
            sleep(8)
            d.press('back')
            sleep(8)
    except Exception as e:
        restart(e)
            
# try:
#     wd=webdriver.Firefox()
#     Status.setStatus("Browser started")
# except Exception as e:
#     restart(e)
# wd.implicitly_wait(35)
# #wd.execute_script("document.body.style.zoom='0.5'")
# login=True
# if fpr==TESTINT:
#     login=False

# def ScrollToBottom(tries=SCROLLTRIES,goback=True)->None:
#     global wd
#     for _ in range(tries):
#         wd.execute_script(SCROLLBOTTOM)
#         sleep(2)
#     if goback:
#         scrollToTop(tries=tries)
# def scrollToBottom(tries=SCROLLTRIES)->None:
#     ScrollToBottom(tries=SCROLLTRIES)
# def scrollToTop(tries=SCROLLTRIES)->None:
#     global wd
#     for _ in range(SCROLLTRIES):
#         wd.execute_script(SCROLLTOP)
#         sleep(2)
# def ScrollToTop(tries=SCROLLTRIES)->None:
#     scrollToTop(tries=SCROLLTRIES)
# def getAuthor():
    
#     global wd
#     try:
#         author=wd.find_element(By.CSS_SELECTOR,'.mhy-user-card__link > span:nth-child(1)')
#         Status.setStatus(f'author:{author.text}')
#     except Exception as e:
#         Status.setStatus(f'getAuthor() failed:{e}')
#         return ''
#     return author.text
# def sendAnswerD(answer,inputBox):
    
#     temp=''
#     for text in answer:
#         if text=='\n':
#             inputBox.send_keys(temp)
#             inputBox.send_keys(Keys.ENTER)
#             feed()
#             #print(temp)
#             temp=''
#             sleep(0.01)
#         else:
#             temp+=text
#     inputBox.send_keys(temp)
#     #print(temp)



# def sendAnswer(answer,inputBox,refuseEmotions=False,MAXIMUMCOUNT=500):
#     Status.setStatus(f"sendAnswer({answer},...MAXIMUMCOUNT={MAXIMUMCOUNT})")
#     emotionCount=10*int(refuseEmotions)
#     temp=''
#     wordCount=0
#     for text in answer:
        
#         if text=='\n':
#             wordCount+=2
#             inputBox.send_keys(temp)
#             inputBox.send_keys(Keys.ENTER)
    
#             feed()
#             #print(temp)
#             temp=''
#             sleep(0.01)
#         else:
#             temp+=text
#             wordCount+=1
#             if text in '，。' and randint(0,10)<5 and emotionCount<10:
#                 emotion=choice(EMOTIONS)
#                 temp+=emotion
#                 wordCount+=len(emotion)
#                 emotionCount+=1
#         if wordCount>MAXIMUMCOUNT:
#             break
#     inputBox.send_keys(temp)
#     #print(temp)
#     Sleep(4)
#     Status.setStatus(f"sendAnswer(...)done")
# urlList=[]
# if not os.path.exists('urlList.txt'):
#     o=open('urlList.txt','w')
#     o.close()

# def checkUrl()->bool:
#     return False
#     try:
#         global wd,urlList
#         url=wd.current_url
#         s=url.find('article/')
#         articleIndex=url[s+8:]
#         if articleIndex in urlList:
#             return True
#         urlList.append(articleIndex)
#         return False
#     except:
#         return False
# def getCommand(text): #没什么用了
#     if text=='Inquiry->':
#         pass
#     else:
#         return False
# if login:
#     try:
#         wd.get('https://www.miyoushe.com/ys/')
#         Sleep(12)
#         try:
#             wd.find_element(By.CSS_SELECTOR,".header__avatar > img:nth-child(1)").click()
#         except Exception as e:
#             wd.find_element(By.CSS_SELECTOR,".header__avatarwrp").click()
#         Sleep(12)
#         r=wd.find_element(By.ID,"mihoyo-login-platform-iframe")
#         Sleep(12)
#         wd.switch_to.frame(r)
#         wd.find_element(By.CSS_SELECTOR ,'#tab-password').click()
#         wd.find_element(By.CSS_SELECTOR ,'#username').send_keys(ACCOUNT)
#         wd.find_element(By.CSS_SELECTOR ,'#password').send_keys(PASSWORD)
#         wd.find_element(By.CSS_SELECTOR ,'.el-checkbox__inner').click()
#         wd.find_element(By.CSS_SELECTOR ,'button.el-button').click()
#         Status.setStatus("Login successfully")
#         if CHECKFOLLOWED:
#             print('关注')
#             Sleep(12)
#             wd.get(FANLIST)
#             sleep(12)
#             scrollToBottom(20)
#             for i in wd.find_elements(By.CLASS_NAME,'mhy-follow-button'):
#                 if '回关' in str(i.get_attribute('innerHTML')):
#                     i.click()
#                     sleep(2)
#             sleep(12)
#             wd.get(FOLLOWLIST)
#             sleep(12)
#             scrollToBottom(20)
#             for i in wd.find_elements(By.CLASS_NAME,'mhy-follow-button'):
#                 if '已关注' in str(i.get_attribute('innerHTML')):
#                     i.click()
#                     sleep(2)
#                     wd.find_element(By.CSS_SELECTOR,'div.mhy-button:nth-child(2) > button:nth-child(1)').click()
#                     sleep(2)
#             Status.setStatus("Followed Checked")
#     except Exception as e:
#         restart(e)
# feed()
# #o=open('replied.txt','a')
# o=open('replied.txt','r')
# replied=[]
# tmprepl=o.read().split('\n')
# for n in tmprepl:
#     replied.append(n.replace('[ENTER]','\n'))
# def writereplied():
#     #Status.setStatus("writereplied()")
#     global replied
#     global Filter
#     global blacklist
#     Filter.saveSpamList()
#     blacklist.saveToFile()
#     tmp=[]
#     for i in replied:
#         tmp.append(i.replace('\n','[ENTER]'))
#     p=open('replied.txt','w')
#     tx='\n'.join(tmp)
#     for k in tx:
#         try:
#             p.write(k)
#         except UnicodeEncodeError:
#             pass
#     p.close()
# def getNotebook():
#     with open('replied.txt','r') as r:
#         t=r.read().replace('[ENTER]','\n')
#     p=open('Notebook.txt','w',encoding='utf8')
#     p.write(t)
#     p.close()

# #getNotebook()
# while True:
#     print(fpr,end=' ')
    
#     try:
#         print(ValU[fpr],'-'*40)
#         Status.setStatus(f"Now:{ValU[fpr]}")
#     except Exception as e:
#         pass
#     if fpr==11:
#         if MONITORMODE:
#             fpr+=1
#             continue
#         wd.quit()
#         try:
#             MAXIMUMCOUNT=3600
            
#             from AutoGui2 import empty
#             empty()
#         except:
#             pass
#         restart('Normal Exit')
#     if fpr==0:
        


#         tries=0
#         wd.get('https://www.miyoushe.com/ys/notifications/reply')
#         Sleep(1)

#         ScrollToBottom()

#         #回复
#         ready=wd.find_elements(By.CLASS_NAME,'notifications-common-card__content')
#         for t1 in ready:
#             tries+=1
#             if tries==REPLYLIMIT:
#                 continue
#             try:
#                 t1.click()
#             except Exception as e:
#                 restart(e)
#             repllist=[]
#             Sleep(8)
#             originalPost=''

#             try:
#                         wd.find_element(By.CSS_SELECTOR,'div.mhy-loadmore:nth-child(2) > div:nth-child(1) > button:nth-child(1)').click()
#                         Status.setStatus("Loading more comments")
#             except:
#                         print("❌没有找到'点击加载更多'按钮")
#                         Status.setStatus("Loading more comments failed")

#             #点击查看全部评论
#             try:
#                 wd.find_element(By.CSS_SELECTOR,'.s-reply-list__title--showall').click() 
#                 Status.setStatus("Clicking all comments")
#             except:
#                 pass     
#             try:
#                 repld=wd.find_elements(By.CLASS_NAME,'reply-card__container')
#             except Exception as e:
#                 restart(e)
#             image=containsImageinReply()
#             imageDescription=''
#             try:
#             #查看原帖
#                 Status.setStatus("getting original post")
#                 wd.find_element(By.CSS_SELECTOR,'.reply-detail-container__main > div:nth-child(2) > div:nth-child(3) > a:nth-child(1)').click()
#                 wd.switch_to.window(wd.window_handles[-1])
#                 Sleep(2)
#                 originalPost+=wd.find_element(By.CSS_SELECTOR,'.mhy-article-page__title').text
#                 if not image:
#                     image=containsImage()
#                     imageDescription=''
#                 try:
#                     originalPost+='\n'+wd.find_element(By.CSS_SELECTOR,'.mhy-img-text-article__content').text
#                 except Exception as e:
#                     pass
            
#                 wd.close()
#                 wd.switch_to.window(wd.window_handles[-1])
#             except Exception as e:
#                 restart(e)
#             #所有回复
            
#             #a=ts.find_elements(By.CLASS_NAME,'mhy-account-title__name')
#             #b=ts.find_elements(By.CLASS_NAME,'reply-card__content')
#             #c=ts.find_elements(By.CLASS_NAME,'reply-card-operation-bottom__item')
#             getTrainingDataReplyFlag=False
#             try:
#                 ts=wd.find_element(By.CLASS_NAME,'mhy-action-sheet__body')
#                 for i in repld:
#                     print(repld.index(i),'|',len(repld))
#                     name=i.find_element(By.CLASS_NAME,'mhy-account-title__name').text
#                     flag=False
#                     for nyaName in NYANAMES:
#                         if name.replace(' ','')==NYANAME:
#                             flag=True
#                             break
#                     if flag:
#                         continue
#                     content=i.find_element(By.CLASS_NAME,'reply-card__content').text
#                     for nyaName in NYANAMES:
#                         content=content.replace('@'+nyaName,'')
#                     if content.replace(' ','')=='':
#                         continue
#                     if Filter.isSpam(content):
#                         Status.setStatus(f"{content} is spam")
#                         blacklist.addUser(name)
#                         continue
#                     originalcontent=''
#                     answersToTrain=[]
#                     #找过去的对话
#                     try:
#                         Status.setStatus("getting previous conversations")
#                         for k in repld:
#                             tmp_content=k.find_element(By.CLASS_NAME,'reply-card__content').text
#                             for nyaName in NYANAMES:
#                                 tmp_content=tmp_content.replace('@'+NYANAME,'')
                            
#                             answersToTrain.append(tmp_content)
#                             originalcontent+=tmp_content+'\n'
#                     except Exception as e:
#                         print('过去的对话没有找到:',e)
#                         Status.setStatus("No previous conversation")
#                         originalcontent=''

#                     originalcontent="过去的回复:\n"+originalcontent

#                     i.find_element(By.CLASS_NAME,'mhy-heart-click__icon').click()
#                     content=interpret(content)
#                     print(name+':'+content,name+content in replied)
#                     Blacklist_=list(blacklist.getUsersWithCountOverTen())
#                     print(name,'🏁',name in Blacklist_)
#                     originalcontent+=content+'\n'

                    
#                     if name+content not in replied and name not in Blacklist_:

#                         replied.append(name+content)
#                         Status.setStatus(f"replying->{name+content}")
#                         writereplied()
#                         if image and imageDescription=='':
#                             imageDescription=VisionUtil.getImageDescription([image])
#                             try:
#                                 answer=getAnswer(content,PROMPT=[originalcontent+'\n#原帖:'+originalPost+'#图片描述:'+imageDescription],NewPrompts=True)
#                                 _question=getQuestion(content,PROMPT=[originalcontent+'\n#原帖:'+originalPost+'#图片描述:'+imageDescription])
#                             except Exception as e:
#                                 answer='喵。'
#                         elif image and imageDescription!='':
#                             try:
#                                 answer=getAnswer(content,PROMPT=[originalcontent+'\n#原帖:'+originalPost+'#图片描述:'+imageDescription],NewPrompts=True)
#                                 _question=getQuestion(content,PROMPT=[originalcontent+'\n#原帖:'+originalPost+'#图片描述:'+imageDescription])
#                             except Exception as e:
#                                 answer='喵。'
#                         else:
#                             try:
#                                 answer=getAnswer(content,PROMPT=[originalcontent+'\n#原帖:'+originalPost],NewPrompts=True)
#                                 _question=getQuestion(content,PROMPT=[originalcontent+'\n#原帖:'+originalPost])
#                             except Exception as e:
#                                 answer='喵。'
#                         answer=answer[:500]
#                         if not getTrainingDataReplyFlag:
#                             getTrainingDataReply(_question,answersToTrain)
#                             getTrainingDataReplyFlag=True
#                         i.find_element(By.CLASS_NAME,'reply-card-operation-bottom__item').click()
#                         #wd.find_element(By.CLASS_NAME,'ql-blank').send_keys(answer)
#                         Sleep(1)
#                         inputBox=wd.find_element(By.CLASS_NAME,'ql-blank')
#                         sendAnswer(answer,inputBox)
#                         Sleep(1)
#                         if not MONITORMODE:
#                             wd.find_element(By.CLASS_NAME,'mhy-reply-box__submit').click()
                        
#                         writeCount()
                        
#                         Sleep(3)
#                         #getimg()
#                         Sleep(SLPTIMEFORREPLY)
#             except Exception as e:
#                 restart(e)
#                 break
#             try:
#                 wd.find_element(By.CLASS_NAME,'icon-close1').click()
#                 sleep(2)
#             except Exception as e:
#                 pass
#     elif fpr==1:#发帖
#         fpr+=1
#         continue
#         if MONITORMODE:
#             fpr+=1
#             continue
#         try:
#             pos=getPost()
#             replied.append(pos.title)
#             writereplied()
#             wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
#             wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys(pos.title)
#             inputBox=wd.find_element(By.CSS_SELECTOR,'.ql-editor')
#             sendAnswer(pos.content,inputBox,MAXIMUMCOUNT=30000)
#             selectPartition()
#             sleep(1)
#             wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
#             Sleep(SLPTIME*2)
#         except Exception as e:
#             restart(e)
#     elif fpr==2:#发小说帖
#         fpr+=1
#         continue
    
#         if MONITORMODE:
#             fpr+=1
#             continue
#         try:
#             posG=getNovel()
#             replied.append(posG.title)
#             writereplied()
#             wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
#             wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys(posG.title)
#             inputBox=wd.find_element(By.CSS_SELECTOR,'.ql-editor')
#             sendAnswer(posG.content,inputBox,True,MAXIMUMCOUNT=30000)
#             sleep(4)
#             selectCollection()
#             sleep(4)
#             selectPartition()
            
#             #预投稿
#             #wd.find_element(By.CSS_SELECTOR,'div.original-form-item__original:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)').click()
            
#             sleep(1)
#             wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
#             Sleep(SLPTIME*2) 
#         except Exception as e:
#             restart(e)       
#     elif fpr==5: #@
#         try:
#             wd.get('https://www.miyoushe.com/dby/notifications/mention')
#             ats=wd.find_elements(By.CLASS_NAME,'notifications-common-card')
#         except Exception as e:
#             restart(e)
#         for ri in ats:
#             try:
#                 print(ats.index(ri),'|',len(ats))
#                 Status.setStatus(f"Now:{ri}->@")
#                 originalPost=''
#                 try:
#                     ri.click()
#                 except Exception as e:
#                     restart(e)
#                 try:
#                     repld=wd.find_elements(By.CLASS_NAME,'reply-card__container')
#                     Ser=False
#                 except Exception as e:
#                     restart(e)
#                 #查看原帖
#                 try:
#                     Status.setStatus(f"seeking original post")
#                     wd.find_element(By.CSS_SELECTOR,'.reply-detail-container__main > div:nth-child(2) > div:nth-child(3) > a:nth-child(1)').click()
#                 except Exception as e:
#                     Ser=True
#                     Status.setStatus(f"It is a post")
                    
#                     pass
#                 try:
#                     wd.switch_to.window(wd.window_handles[-1])
#                     originalPost+=wd.find_element(By.CSS_SELECTOR,'.mhy-article-page__title').text
#                 except Exception as e:
#                     restart(e)
#                 try:
#                     originalPost+='\n'+wd.find_element(By.CSS_SELECTOR,'.mhy-img-text-article__content').text
#                 except Exception as e:
#                     pass
#                 if not Ser:
#                     wd.close()
#                     wd.switch_to.window(wd.window_handles[-1])
#                 else:
#                             try:
#                                 wd.find_element(By.CSS_SELECTOR,'div.mhy-article-actions__item:nth-child(3) > div:nth-child(1) > svg:nth-child(1)').click()
#                             except Exception as e:
#                                 pass
#                             #
#                             title=wd.find_element(By.CSS_SELECTOR,'.mhy-article-page__title > h1:nth-child(1)').text
#                             try:
                                
#                                 content=wd.find_element(By.CSS_SELECTOR,'.mhy-img-text-article__content').text
#                             except Exception as e:
#                                 content=''
#                             content=interpret(content)
#                             if Filter.isSpam(content):
#                                 Status.setStatus(f"{content} is spam")
#                                 continue
#                             try:
#                                 image=containsImage()
#                                 print(image)
#                                 if image:
#                                     description=VisionUtil.getImageDescription([image])
#                                     answer=getAnswer(title+','+content,PROMPT=[',图片描述:'+description.replace('\n',',')])
#                                 else:
#                                     answer=getAnswer(title+','+content)
#                                 inputBox=wd.find_element(By.ID,'reply').find_element(By.CLASS_NAME,"ql-editor")

#                                 try:
                                    
                                    
#                                     if containsRichTextWithoutInterpretation(answer):
#                                         richtext=containsRichText(answer)
#                                         sendAnswer(richtext[1],inputBox,MAXIMUMCOUNT=1000)
#                                         wd.find_element(By.CSS_SELECTOR,'.icon-tupian1').click()
#                                         CopyTest.uploadSth(os.path.abspath(richtext[0]))
#                                     else:
#                                         sendAnswer(answer,inputBox,MAXIMUMCOUNT=1000)
#                                 except Exception as e:
#                                     sendAnswer(answer,inputBox,MAXIMUMCOUNT=1000)
#                                     pass
                                    

#                                 #answer=getAnswer(title+','+content)
                                
#                                 sendAnswer(answer,inputBox)
#                             except Exception as e:
#                                 pass
#                             if randint(0,4)==0:
#                                 try:
#                                     CopyTest.copyImage(pickImages())
#                                     wd.find_element(By.ID,'reply').find_element(By.CLASS_NAME,"ql-editor").send_keys(Keys.CONTROL,'v')
#                                     Sleep(8)
#                                 except Exception as e:
#                                     pass
#                             if not MONITORMODE:
#                                 wd.find_element(By.CLASS_NAME,'mhy-button-normal').click()
#                                 writeCount()
#                                 writereplied()
                          
                       
                            
#                             Sleep(SLPTIME)
#                             try:
#                                 wd.find_element(By.CSS_SELECTOR,'.geetest_close').click()
#                                 #Status.setStatus(f"WARN:Found Captcha,maybe it needs to slow down")
#                                 restart("Captcha Detected,now restarting")
#                             except Exception as e:
#                                 print('?')
#                             wd.close()
#                             wd.switch_to.window(wd.window_handles[-1])
     
#                             continue
#                 #所有回复
#                 try:
#                     ts=wd.find_element(By.CLASS_NAME,'mhy-action-sheet__body')
#                 except Exception as e:
#                     restart(e)
#                 #a=ts.find_elements(By.CLASS_NAME,'mhy-account-title__name')
#                 #b=ts.find_elements(By.CLASS_NAME,'reply-card__content')
#                 #c=ts.find_elements(By.CLASS_NAME,'reply-card-operation-bottom__item')
#                 try:
                    
#                     for i in repld:
#                         print(repld.index(i),'|',len(repld))
                        
#                         try:
#                             name=i.find_element(By.CLASS_NAME,'mhy-account-title__name').text
#                         except Exception as e:
#                             print('''name=i.find_element(By.CLASS_NAME,'mhy-account-title__name').text Fail''')
                            
#                             continue
#                         if name.replace(' ','')=='Nya2PtCl4':
#                             continue
#                         try:
#                             content=i.find_element(By.CLASS_NAME,'reply-card__content').text.replace('﻿@Nya2PtCl4','')
#                         except Exception as e:
#                             content=''
#                         if content.replace(' ','')=='':
#                             continue
#                         i.find_element(By.CLASS_NAME,'mhy-heart-click__icon').click()
                        
#                         print(name+':'+content,name+content in replied)
#                         Status.setStatus(f"Replying {name}({content[:30]})")
#                         if name+content not in replied:
#                             replied.append(name+content)
#                             writereplied()
#                             try:
#                                 answer=getAnswer(content,PROMPT=['\n#原帖:'+originalPost],NewPrompts=True)
#                                 if len(answer)>500:
#                                     answer=getAnswer(content+'……字数小于500字')[:500]
#                             except Exception as e:
#                                 answer='喵。'
#                             i.find_element(By.CLASS_NAME,'reply-card-operation-bottom__item').click()
#                             writeCount()
#                             #wd.find_element(By.CLASS_NAME,'ql-blank').send_keys(answer)
#                             sleep(1)
#                             inputBox=wd.find_element(By.CLASS_NAME,'ql-blank')
#                             sendAnswer(answer,inputBox)
#                             sleep(1)
#                             selectPartition()
#                             sleep(1)
#                             if not MONITORMODE:
#                                 wd.find_element(By.CLASS_NAME,'mhy-reply-box__submit').click()
                
                           
                            
                          
#                             Sleep(SLPTIMEFORREPLY)
#                             try:
#                                 wd.find_element(By.CSS_SELECTOR,'.geetest_close').click()

#                                 restart("Captcha Detected,now restarting")
#                             except Exception as e:
#                                 print('?')
#                             sleep(2)
#                             try:
#                                 wd.find_element(By.CSS_SELECTOR,'.icon-close1').click()
#                             except Exception as e:
#                                 restart(e)
#                 except Exception as e:
#                     restart(e)
#             except Exception as e:
#                 continue
#     elif fpr==6:#发图片帖
#         fpr+=1
#         continue
#         if MONITORMODE:
#             fpr+=1
#             continue
#         #replied.append('分享图片')
#         try:
#             writereplied()
#             wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
        
#             wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys('分享图片')
#             failTries=0
#             selectPartition()
#         except Exception as e:
#             restart(e)
#         for i in range(4):
#             try:
#                 if randint(0,4)<1:
#                     CopyTest.getNetImage()
#                     wd.find_element(By.CSS_SELECTOR,'.icon-image').click()
#                     CopyTest.uploadSth(os.path.abspath('temp.jpg'))
#                 else:
#                     wd.find_element(By.CSS_SELECTOR,'.icon-image').click()
#                     CopyTest.uploadSth(os.path.abspath(pickImages(True)))
                    

#             except Exception as e:
#                 print('Fail')
#                 failTries+=1
#         if failTries<4:
                
#             Sleep(20)
#             wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()

#             Sleep(SLPTIME*2)
#         else:
#             Sleep(12)
#     elif fpr==9:#画画
#         fpr+=1
#         continue
#         if MONITORMODE:
#             fpr+=1
#             continue
#         try:
#             image=DrawUtils.drawPicture()
#             Sleep(12)
#         except Exception as e:
#             fpr+=1
#             continue
#         try:
#             image.save('temp.png')
#             replied.append('分享作品')
#             writereplied()
#             wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
#             wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys('分享作品')
#             failTries=0
#             selectPartition()
#             wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
#             wd.find_element(By.CSS_SELECTOR,'.icon-image').click()
#             CopyTest.uploadSth(os.path.abspath('temp.png'))
#             Sleep(30)
#             wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
#             Sleep(SLPTIME*2)
#         except Exception as e:
#             restart(e)
#     elif fpr==12:#获取图片
#         if MONITORMODE:
#             fpr+=1
#             continue
#         try:
#             imageLs=netFetchUtils.fetch()
#             Sleep(12)
#         except Exception as e:
#             fpr+=1
#             continue
#         try:
#             _title=imageLs[0]
#             replied.append(_title)
#             wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
#             wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys(_title)
#             failTries=0
#             selectPartition()
#             wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
#             wd.find_element(By.CSS_SELECTOR,'.icon-image').click()
#             CopyTest.uploadSth(os.path.abspath(imageLs[1]))
#             Sleep(30)
#             wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
#             Sleep(SLPTIME*2)
#         except Exception as e:
#             restart(e)
#     elif fpr==8:#分享视频
#         fpr+=1
#         continue
#         if MONITORMODE:
#             fpr+=1  
#             continue
#         wd.get(VIDEOURL)
#         try:
#             wd.find_element(By.CSS_SELECTOR,'.bili-mini-close-icon')
#             Sleep(2)
#             wd.get(VIDEOURL)
#         except Exception as e:
#             pass
#         try:
#             Sleep(12)
#             vtaglist=wd.find_elements(By.CLASS_NAME,'small-item')
#             Videos=[]
#         except Exception as e:
#             restart(e)
#         for i in vtaglist:
#             f=video()
#             f.BVID=i.get_attribute('data-aid')
#             f.name=i.find_element(By.TAG_NAME,'img').get_attribute('alt')
#             Videos.append(f)
#         flag=False
#         tries_=0
#         for i in Videos:
#             if i.name not in replied:
#                 flag=True
#                 replied.append(i.name)
#                 writereplied()
#                 wd.get('https://www.miyoushe.com/dby/newArticle/0/1/877')
#                 wd.find_element(By.CSS_SELECTOR,'.mhy-input__container > input:nth-child(1)').send_keys(i.name)
#                 wd.find_element(By.CSS_SELECTOR,'.icon-shipin1').click()
#                 sleep(1)
#                 wd.find_element(By.CSS_SELECTOR,'li.mhy-tab__item:nth-child(2) > span:nth-child(1)').click()
#                 sleep(1)
#                 wd.find_element(By.CSS_SELECTOR,'div.mhy-input:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys(i.BVID)
#                 sleep(1)
#                 wd.find_element(By.CSS_SELECTOR,'.mhy-video-uploader__confirm > button:nth-child(1)').click()
#                 sleep(1)
#                 selectPartition()
#             if flag:
#                 wd.find_element(By.CSS_SELECTOR,'.mhy-button__button').click()
#                 Sleep(SLPTIME)
                
#             else:
#                 Sleep(12)
#             tries_+=1
#             if tries_>3:
#                 break
            


#     else:
#         tries=0
#         nets=['','','','https://www.miyoushe.com/dby/timeline','https://www.miyoushe.com/dby/home/34?type=2','','','https://www.miyoushe.com/dby/home/35','https://www.miyoushe.com/ys/timeline','','https://www.miyoushe.com/ys/home/26']
#         try:
            
#             wd.get(nets[fpr])
#             Status.setStatus(f"Now visiting {nets[fpr]}")
#             Sleep(12)
#             scrollToBottom()
#             e=wd.find_elements(By.CLASS_NAME,"mhy-article-card")
#             e2=wd.find_elements(By.CLASS_NAME,"mhy-router-link mhy-article-card__link")

            
#             for post in e:
#                 print(e.index(post),'|',len(e))
#                 Status.setStatus(f"{e.index(post)}|{len(e)} ")
#                 tries+=1
#                 if tries>=POSTLIMIT:
#                     break
#                 try:
#                     title=post.find_element(By.CLASS_NAME,"mhy-article-card__h3").text
                    
#                     til=post.find_element(By.CLASS_NAME,"mhy-article-card__h3")
#                     #try:
                        
#                         #content=post.find_element(By.CLASS_NAME,"mhy-article-card__content").text
#                     #except Exception as e:
#                         #没有内容
#                         #content=''

#                     print(title,title in replied)
#                     author=getAuthor()
                    

#                     if title not in replied and author not in list(blacklist.getUsersWithCountOverTen()):
#                         Status.setStatus(f"Now replying {title}")
#                         replied.append(title)
#                         til.click()
#                         wd.switch_to.window(wd.window_handles[-1])
#                         sleep(1)
                        
#                         try:
#                             content=wd.find_element(By.CSS_SELECTOR,'.mhy-img-text-article__content').text
#                         except Exception as e:
#                             content=''
#                         if Filter.isSpam(content):
#                             continue
#                         content=interpret(content)
#                         getTrainingDataTitlePost(title,content)
                         
                        
#                         #点赞
#                         try:
#                             wd.find_element(By.CSS_SELECTOR,'div.mhy-article-actions__item:nth-child(3) > div:nth-child(1) > svg:nth-child(1)').click()
#                             Status.setStatus(f"Like")
#                         except Exception as e:
#                             pass
#                         #
#                         try:
#                             image=containsImage()
#                             print(image)
                            
#                             if image:
#                                 description=VisionUtil.getImageDescription([image])
#                                 answer=getAnswer(title+','+content,PROMPT=[',图片描述:'+description.replace('\n',',')])
#                                 catquestion=catQuestion(title+','+content,PROMPT=[',图片描述:'+description.replace('\n',',')])
#                             else:
#                                 answer=getAnswer(title+','+content)
#                                 catquestion=catQuestion(title+','+content)
#                             answer=answer[:1000]
#                             getTrainingDataPost(catquestion)
#                             inputBox=wd.find_element(By.ID,'reply').find_element(By.CLASS_NAME,"ql-editor")
#                             try:
                                
                                
#                                 if containsRichTextWithoutInterpretation(answer):
#                                     richtext=containsRichText(answer)
#                                     sendAnswer(richtext[1],inputBox,MAXIMUMCOUNT=1000)
#                                     wd.find_element(By.CSS_SELECTOR,'.icon-tupian1').click()
#                                     CopyTest.uploadSth(os.path.abspath(image))
#                             except Exception as e:
#                                 pass
#                             if Filter.isSpam(answer):
#                                 Status.setStatus(f"{answer[:30]} is spam")
#                                 answer=''
#                             sendAnswer(answer,inputBox,MAXIMUMCOUNT=1000)
#                         except Exception as e:
#                             pass
#                         replied.append(content)
#                         if randint(0,4)==0:
#                             CopyTest.copyImage(pickImages())
#                             wd.find_element(By.ID,'reply').find_element(By.CLASS_NAME,"ql-editor").send_keys(Keys.CONTROL,'v')
#                             Sleep(8)
#                         if not MONITORMODE:
#                             wd.find_element(By.CLASS_NAME,'mhy-button-normal').click()
#                             writeCount()
#                             writereplied()
                     
                                          
                        
#                         Sleep(SLPTIMEFORREPLY)
#                         try:
#                             wd.find_element(By.CSS_SELECTOR,'.geetest_close').click()
#                             restart("Captcha Detected,now restarting")
#                         except:
#                             print('?')
#                         try:
#                             wd.close()
#                             wd.switch_to.window(wd.window_handles[-1])
#                         except:
#                             restart('Switch Failed')
                        
                                               
#                 except:
                    
#                     restart()
#                     continue

#         except Exception as e:
            
#             restart(e)
#     fpr+=1
#     if fpr>len(ValU)-2:
#         fpr=0
#wd.find_element(By.CLASS_NAME,'notifications-common-card__content--text').click()
#a=wd.find_elements(By.CLASS_NAME,'notifications-common-card')
#rep=wd.find_element(By.CLASS_NAME,'mhy-action-sheet__header')
#rell=rep.find_elements(By.CLASS_NAME,'reply-card')
