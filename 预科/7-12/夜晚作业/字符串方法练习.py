f=open('zfc.txt','r',encoding='utf-8')
for line in f:
    list1=line.split('"')
    for x in list1:
        res=x.startswith('h')
        if res==True:
            print(x)
        else:
            continue
f.close()
