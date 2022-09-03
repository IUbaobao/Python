import random

guess=random.randint(1,100)
# print(guess)
flag=0
a = int(input("请猜数字"))
while flag==0:
    if a==guess:
        print("恭喜你，猜到了")
        flag=1
        break
    elif a > guess:
        print("猜大了")
        a=int(input())

    else:
        print("猜小了")
        a = int(input())



