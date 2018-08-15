while True:
    km = int(input('请输入公里数'))
    if km<=0:
        print('公里数输入错误,程序结束')
        break
    else:
        if km <= 2 and km > 0:
            print('你需要花费八元')
        if km>2 and km <= 12:
            cost = (8+(km-2)*1.2)
            print(type(cost))
            print('你需要花费%s'%cost)
        if km>12:
            cost=8+(12-2)*1.2+(km-12)*1.5
            print('你需要花费%s'%cost)
