f=open('ThatGirl.txt','r',encoding='utf-8')
#'w'模式打开文件,如果当前目录下不存在该文件,则自动创建
f_new=open('ThatGirl.bak','w',encoding='utf-8')

for line in f:
    if '一切都是我的错' in line:
        line=line.replace('一切都是我的错','沉默不是代表我的错')
        f_new.write(line)
    else:
        f_new.write(line)
f.close( )
f_new.close( )

