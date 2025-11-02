from time import sleep
a=open('Atr.py','r',encoding='utf8')
a2=a.read().split('\n')
a.close()
for i in a2:
    print(i)
    exec(i)
    sleep(0.1)
