#  语法一： range(num)
# for x in range(10):
#     print(x)

# 语法二： range（num1,num2）
# for x in range(0,10):
#     print(x)


# 语法三 range(num1,num2,step)  step->步长，break，continue可以正常使用
# for x in range(0,10,2):
#     print(x)


# 计算1到num中有多少个偶数
#
# count=0
# for x in range(1, int(input("请输入num"))):
#     if x%2==0:
#         count+=1
#
# print(f"偶数有{count}个")


# 函数的定义 def 函数名(传入参数)：
#                函数实现
#                return

# def print_hi():
#     print("hi,pythoy")
#
# print_hi()


# None 类型，表示空的，无意义的-->函数无返回值默认会返回None

# def check_age(age):
#     if age>=18:
#         return "成年人"
#     else:
#         return None
# def test1():
#     print("hi")
#
# print(test1())
# print(check_age(16))


# 函数文档 --> 注释

# def add(x, y):
#     """
#     add可以让两个数进行相加，并返回结果
#     :param x:两数相加的其中一个
#     :param y: 两数相加的另一个
#     :return: 两数相加后的结果
#     """
#     result = x + y
#     return result
#
#
# add(1, 3)



# global 可以修改全局变量的值

# 不加global
# num=200
# def test_a():
#     print(num)
#
# def test_b():
#     num=500   # num是局部变量
#     print(num)
#
#
# test_a()
# test_b()
# print(num)

# 加global
# num=200
# def test_a():
#     print(num)
#
# def test_b():
#     global num  # num表示全局变量的num了
#     num=500
#     print(num)
#
#
# test_a()
# test_b()
# print(num)



# list Python中的数组 里面的元素无类型限制
# 取元素可以从前往后，也可以从后往前

name_lislt= ["黄东明",False, 666]
print(name_lislt)
print(type(name_lislt))
# 正向取
print(name_lislt[0])
print(name_lislt[1])
print(name_lislt[2])
# 反向取
print(name_lislt[-1])
print(name_lislt[-2])
print(name_lislt[-3])