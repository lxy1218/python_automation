#print("test")
class Person():
    def __init__(self,name,age,pay = 0,job = None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
if  __name__ ==  "__main__":
    Bob = Person("Bob Alen",25,3000,"network engine")
    Susan=Person("Susan Jack",30,6000,"devlopment engine")
    print(Bob.job)
    print(Susan.job)
    print(Bob.name.split()[0])#打印姓氏
    Susan.pay = int(Susan.pay * 2)#涨工资
    print(Susan.pay)
