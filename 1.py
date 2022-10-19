# import random
# a=random.randint(0,9)                         #随机生成0-9的整数
# count=0                                       #初始化count值
# for i in range(10):                           #设循环次数10次
#     num=int(input("请输入你猜的数字："))
#     if num>a:
#         print("猜大了")
#         count=count+1
#     elif num<a:
#         print("猜小了")
#         count=count+1
#     elif num==a:
#         count=count+1
#         print("恭喜，猜对了，一共猜了N次恭喜，猜对了，一共猜了"+format(count)+"次".format(count))
#         break

# s = input("请输入字符串:")
# chi = 0  # 记录汉字
# alpha = 0  # 记录字母
# space = 0  # 记录空格
# num = 0  # 记录数字
# other = 0  # 记录其他字符
# for i in s:
#     if '\u4e00' <= i <= '\u9fa5':
#         chi += 1
#     elif ord("a") <= ord(i.lower()) <= ord("z"):
#         alpha += 1
#     elif ord(" ") == ord(i):
#         space += 1
#     elif ord("0") <= ord(i) <= ord("9"):
#         num += 1
#     else:
#         other += 1
# print("您输入的字符串中有{}个中文，{}个英文字符，{}个数字，{}个空格，{}个其他字符".format(chi, alpha, num, space, other))







# print("请输入一个字符串：")
# tmpStr = input()
# if tmpStr == tmpStr[::-1]: #一前一后比较
#     print('yes')
# else:
#     print('no')






# import random
# char = 'BCEFGHJKMPQTVWXY2346789'
# lst = []
# for i in range(5):
#     ls = random.sample(char,5)
#     s = ''.join(ls)
#     lst.append(s)
# key = '-'.join(lst)
# print(key)
#

# import random
# a='BCEFGHJKMPORTVWXY2346789'
# sum=[]
# n=0
# key=''
# for i in range(5):
#     sum=sum+random.sample(a, 5)
#
# for i in sum:
#     if n==5:
#         key=key+'-'
#         n=0
#     n+=1
#     key=key+i
# print(key)

#
#
# import random
# char='BCEFGHJKMPORTVWXY2346789'
# sum=''
# for i in range(5):
#      sum=sum+random.sample(char, 5)
#     if 1<=i<=4:
#         sum=sum+'-'
# print(sum)
#
# 1、	实现isOdd()函数，参数为整数，如果整数为奇数，返回True，否则返回False。
# 2、	实现multi()函数，参数个数不限，返回所有参数的乘积。
# 3、	实现isPrime()函数，参数为整数，如果整数是质数，返回True，否则返回False.
# 以上函数要有异常处理，并且对函数进行多次调用测试
# 4、	给定红包的总金额和红包发放数量，定义抢红包游戏的函数，限定每个红包的最低金额为0.01元（提示：可用round(x,2)四舍五入函数将金额限定在小数点后2位，uniform(a,b)函数生成[a,b]之间的随机小数）

# 1
import random


def isOdd(x):
    try:
        if type(x)!=type(1):
            raise TypeError
        if x%2==0:
            return True
        else:
            return False
    except TypeError:
        print("这不是一个有效整数")


print(isOdd(2))
print(isOdd(5))
print(isOdd(1.0))


# 2.
def multi(*a):
    sum=1
    try:
        for i in a:
            if type(i) == type("a"):
                raise TypeError
            sum*=i
        return sum
    except TypeError:
        print("字符串类型无效")



print(multi(1,2,3,4))
print(multi(1,2,3,4,'a'))


# 3.
def isPrime(x):
    try:
        if type(x)!=type(1):
            raise TypeError
        i=2
        flag = 0
        while i<x:
            if x%i==0:
                flag=1
                break
            i+=1
        if flag==0:
            return True

        return False

    except TypeError:
        print("这不是这一个有效的整形")


print(isPrime(3))
print(isPrime(4))
print(isPrime("ab"))
print(isPrime(100))

#
# # 4
# def FaHongBao(money,num):
#     leftover=0
#     list=[]
#     RedEnpe=0
#     for i in range(1,num):
#         RedEnpe = float(random.randint(1,(money-leftover-(num-i))))
#         list.insert(i,RedEnpe)
#         leftover+=RedEnpe
#
#     list.insert(num-1,money-leftover)
#     return list
#
#
# money=int(input("请输入你要发放的红包金额"))
# num=int(input("请输入发放数量"))
# print(FaHongBao(money,num))
#
















