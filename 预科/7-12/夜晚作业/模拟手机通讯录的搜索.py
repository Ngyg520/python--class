name_list=['郝超杰','李威','吕朝朝','张广师','李宇恒','池永伟','黄保安','陈鹏','余江帆','曹森','郑慧诏','郭克松','高翔','杨建宇','孟新珂','司金辉','张梦冉','王坤峰','蔡飞','樊俊','张稼瑞','吴亚涛','葛成云','王鹏基','樊俊峰','张崇雷','陈泽坤','王震宇','曾一飞','凌晨洋','郑雪鹏','李鑫一','晋吉祥','王晓茹','陶林','范雪婷','岳银龙','王继涛','张力方','牛铭瑞','马深凌','楚少杰','刘家豪']
name_dict = {}
for x in range(0,len(name_list)):
    name = name_list[x]
    s = name[0]
    list1 = [name]
    if s not in name_dict.keys():
        name_dict[s] = list1
    else:
        name_dict[s].append(name)
while True:
    aaa = input('请输入要查找的联系人姓氏首字符：')
    if aaa in name_dict:
        aaa_list = name_dict[aaa]
        for bbb in range(0,len(aaa_list)):
            print('%s.%s'%(bbb+1,aaa_list[bbb]))
    else:
        print('无此姓氏首字符的联系人')
