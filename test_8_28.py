# 类的定义
class test1():

    def sum(self,a):
        return a+1


a= test1()
print(a)
b=a.sum(1)
print(b)


class test2(test1):
    def test(self):
        print("继承")

c=test2()
d=c.sum(10)
print(d)







