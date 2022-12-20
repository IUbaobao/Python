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




# turtle.pensize(5)
#
# for i in range(5):
#     turtle.fd(200)
#     turtle.right(144)
#
# turtle.done()


# f1 = open('text.txt','r',encoding='UTF-8')
# f1.read(5)
# f1.seek(0)
# print(f1.read(1))
# f1.close()


# turtle.pensize(5)
# turtle.color('red')
#
# for i in range(5):
#     turtle.fd(100)
#     turtle.right(144)
#
#
# turtle.done()

#
# turtle.left(135)
# turtle.fd(200)
# turtle.circle(-100,180)
# turtle.left(90)
# turtle.circle(-100,180)
# turtle.fd(200)
# turtle.done()

# str=["abcdefg",'aa','c']
# print(str[1:-1:2])
#
# print(','.join(str))
#a=lambda x,y : x+y
# print(a(1,2))


# import jieba
#
# txt=open("三国演义.txt","r",encoding='utf-8').read()
# words=jieba.lcut(txt)
# count={}
# for word in words:
#     if len(word)==1:
#         continue
#     count[word]=count.get(word,0)+1
#
# items=list(count.items())
# items.sort(key=lambda x:x[1],reverse=True)
# for i in range(10):
#     word,counts=items[i]
#     print("{:<12}{:>5}".format(word,counts))
#
#




# fo=open("test.csv","r")
# ls=[]
# for line in fo:
#     line=line.replace(',',"")
#     ls.append(line)
# print(ls)
# fo.close()
# import jieba
# txt=open("三国演义.txt","r",encoding='utf-8').read()
# words=jieba.lcut(txt)
#
# count={}
# for word in words:
#     if len(word)==1:
#         continue
#     count[word]=count.get(word,0)+1
#
# ls=list(count.items())
# # ls=list(count)
# ls.sort(key=lambda x:x[1],reverse=True)
# for i in range(10):
#     word,counts=ls[i]
#     print("{:<12}{:>5}".format(word,counts))

# import jieba
# import wordcloud
#
# txt=open("三国演义.txt","r",encoding="utf-8").read()
# words=jieba.lcut(txt)
# txt_str=''.join(words)
# w=wordcloud.WordCloud(font_path='simhei.ttf',width=1000,height=500,background_color='white')
# w.generate(txt_str)
# w.to_file('三国演义.jpg')


# print("{1}的值为{0:.4f}".format(3.1415926,"圆周率"))
#
#
# print("False"or 0)
#
# str="False"or 0
# print(str)
#
# import random
#
# # random.seed(11)
#
# print(random.randrange(0,100))

# print(1/2)
# str="aabc,agccaaa"
# # print(str.split(','))
# print(str.strip('c'))

# s='PYTHON'
#
# print("{0:1.3}".format(s))
# for i in range(2,2):
#     print(i)

#
# for  s  in  'HelloWorld':
#
#        if  s == 'W':
#
#              continue
#
#        print( s , end = "" )

# for i in range(-5, 10, 3):
#     print(i)

# ls =list({'shanghai':200, 'hebei':300, 'beijing':400})
#
# print(ls)


# try:
#     pass
# except:
#     pass

from PIL import Image,ImageFilter,ImageEnhance
#
im=Image.open("birdnest.jpg")
print(im.format,im.size,im.mode)
print(im.tell())
r,g,b=im.split()
newg=g.point(lambda i : i*0.9)
newb=b.point(lambda i : i*0.9)
# om=Image.merge(im.mode,(r,newg,newg))
# om1=im.filter(ImageFilter.CONTOUR)# 轮廓效果
# om2=im.filter(ImageFilter.EMBOSS)# 浮雕效果
om3=ImageEnhance.Color(im)
om3=om3.enhance(0)
# im.show()
# om1.show()
# om2.show()
om3.show()





















