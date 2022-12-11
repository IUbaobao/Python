# print('{:*^10.4}'.format('Flower'))


# a = input("").split(",")
# i = 0
# while i< len(a):
#     print(a[i],end="")
#     i+=1

#
# vlist =[0, 1, 2, 'python', 4]
# print(vlist[3:1:-1])

import turtle
# turtle.pensize(5)
# turtle.circle(50)
# turtle.circle(-100)

def Cardioidary():
    turtle.pensize(5)
    turtle.color('red')
    turtle.begin_fill()
    turtle.left(135)
    turtle.fd(100)
    turtle.circle(-50, 180)
    turtle.left(90)
    turtle.circle(-50, 180)
    turtle.fd(100)
    turtle.end_fill()
    turtle.done()



turtle.pensize(5)

for i in range(5):
    turtle.fd(200)
    turtle.right(144)

turtle.done()