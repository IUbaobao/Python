# input 接收键盘数据
# name=input("你叫什么名字？\n")
# print("我知道了，你的名字是：",name)


# if elif else 使用
#
# if int(input("请输入你的年龄"))>=18:
#     print("已成年,你的VIP等级是？")
#     if int(input())>3:
#         print("你的VIP等级大于3，可以免费进")
#     else:
#         print("你的VIP等级小于3，需要付钱")
# elif int(input("你多高(cm)"))>=120:
#     print("太高了，五折付费")
#
# else:
#     print("你未成年，可以免费进入")




# while 语句使用
# i=0
# sum=0
# while i<=100:
#     sum+=i
#     i+=1
#
# print(f"sum的值为{sum}")

# i=1
# while i<10:
#     j=1
#     while j<=i:
#         # print(" ",end='')，表示不换行输出
#         print("%2d*%-2d=%-2d"%(j,i,i*j),end='')
#         j+=1
#     print("\n")
#     i+=1
#



# for 语句使用： for 变量 in 待处理的数据->for不可能出现无限循环
name = "I love you"
for x in name:
    print(x)
