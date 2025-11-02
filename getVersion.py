o=open("begin.py",'r',encoding='utf-8')
for line in o: 
    if "VERSION=" in line: 
        version=line.split("=")[1].strip()
        print(version)
        break