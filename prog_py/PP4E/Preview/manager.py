__author__ = 'yiqing'

from  person import Person

class Manager0(Person):
    def giveRaise(self,percent,bonus=0.1):
        # why bellow will cause a strange output even if it has a typo
        # self.pay *= (1.0+percent,bonus)
        self.pay *= (1.0+percent+bonus)
        # Person.giveRaise(self, percent + bonus)
class Manager(Manager0):
    def __init__(self,name,age,pay):
        Person.__init__(self,name,age,pay,'manager')


if __name__ == '__main__':
    tom = Manager(name='Tom Doe',age=50,pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
    print(tom)