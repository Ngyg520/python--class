"""
座右铭:路漫漫其修远兮,吾将上下而求索
@project:正课第二周
@author:Mr.Yang
@file:多态.PY
@ide:PyCharm
@time:2018-08-01 10:57:40
"""
#多态:不同的子类对象调用相同的父类方法会产生不同的结果
class Dog(object):
    def work(self):
        pass
class ArmyDog(Dog):
    def work(self):
        print('追击敌人')
class DrugDog(Dog):
    def work(self):
        print('追查毒品')
class SearchDog(Dog):
    def work(self):
        print('搜救')


dog1=ArmyDog()
dog2=DrugDog()
dog3=SearchDog()
#多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。
# 在面向对象方法中一般是这样表述多态性：向不同的对象发送同一条消息，不同的对象在接收时会产生不同的行为（即方法）。也就是说，每个对象可以用自己的方式去响应共同的消息。所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数。
def dog_work(obj):
    obj.work()

dog_work(dog1)
dog_work(dog2)
dog_work(dog3)