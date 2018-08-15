while True:
    height=float(input('请输入你的身高'))
    weight=float(input('请输入你的体重'))
    best_weight=height-105
    if weight>best_weight:
        print('偏胖')
    if weight==best_weight:
        print('正常')
    if weight< best_weight:
        print('你偏瘦')