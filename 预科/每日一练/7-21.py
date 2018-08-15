name = ['alex', 'wupeiqi', 'yuanhao', 'nezha']
print(list(map(lambda x: x + 'good', name)))

num=[1,5,3,5,899,6,4,55,]
print(list(filter(lambda x:x%2==0,num)))

portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
  {'name': 'AAPL', 'shares': 50, 'price': 543.22},
  {'name': 'FB', 'shares': 200, 'price': 21.09},
  {'name': 'HPQ', 'shares': 35, 'price': 31.75},
  {'name': 'YHOO', 'shares': 45, 'price': 16.35},
  {'name': 'ACME', 'shares': 75, 'price': 115.65}
  ]
print([(item['name'],item['shares']*item['price']) for item in portfolio])
print(list(filter(lambda item:item['price']>100, portfolio)))

li = ['alex','agon','amith','pizza','alen']
print([item.capitalize() if item.startswith('a') else item for item in li])
