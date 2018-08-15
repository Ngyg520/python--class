string1="k:1|k1:2|k2:3|k3:4"
dict1={}
res1=string1.split('|')
for x,value in enumerate(res1):
    str1=value[0:2]
    string2 = str1.replace(':','')
    dict1[string2]=x+1
print(dict1)