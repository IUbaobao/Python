# 类的定义
class test1():
    name=None
    age=None
    def __int__(self):
        self.name="小明"
        self.age=19
        print("自动执行的初始化")

    def sum(self,a):
        return a+1


a= test1()
# print(a)
print(a.name)
b=a.sum(1)
print(b)


class test2(test1):
    def test(self):
        print("继承")

c=test2()
d=c.sum(10)
print(d)







