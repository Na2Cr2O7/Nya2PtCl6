from datetime import datetime
from time import sleep
while True:
    k=datetime.now()
    kl=str(k.hour)+str(k.minute)+str(k.second)
    o=open('replied.txt','r')
    r=o.read()
    o.close()
    
    o2=open('.\\t\\replied'+kl+'.txt','w')
    o2.write(r)
    o2.close()
    sleep(20)
    
