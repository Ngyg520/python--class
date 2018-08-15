list1 = [11, 2, 3, 3, 4, 4, 5, 356, 6, 6, 7, 3000, 9]
list2=[]
for x,value in enumerate(list1):
     num1=list1.count(value)
     if num1 ==1:
         list2.append(value)
print(list2)

list1 = ['a','b','v']
list2=[]
for y in range(0,len(list1)):#5,0-12
     num1=list1.count(y)
     if num1 ==1:
         list2.append(y)
print(list2)
#[1,2,7,9]

for i in range(1,15):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,'\t' ,end='')
    print('')
