# # 输入
# name = input("请输入你的名字\n")
# major = input("请输入你的专业\n")
# num = input("请输入你的电话号码\n")
# # 输出
# print(name , major ,num)

# import math
# # 接收半径r
# r = int(input("请输入半径\n"))
# # 计算球的面积
# s = 4*math.pi*r**2
# # 计算球的体积
# v = 4/3*math.pi*r**3
# # 输出结果
# print("半径为%d的球，面积为%.2f，体积为%.2f"% (r,s,v))



# i = int(input())
# arr="零一二三四五六七八九"
# print(arr[i])



import random
# 随机生成验证码
arr = [0,0,0,0]
arr[0] = chr(random.randint(65,90))
arr[1] = chr(random.randint(65,90))
arr[2] = random.randint(0,9)
arr[3] = random.randint(0,9)
# 循环输出
for i in arr:
    print(i,end='')