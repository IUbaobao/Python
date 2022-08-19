

# list 的方法使用list名称.index(内容),查找下标
# name_lislt= ["黄东明",False, 666]
# pos = name_lislt.index("黄东明")
# print(pos)

# list名称.insert(下标，元素)
name_lislt= ["黄东明",False, 666]
name_lislt.insert(1,"cpp")
print(name_lislt)


# list名称.append(元素)
name_lislt= ["黄东明",False, 666]
name_lislt.append("数据结构")
print(name_lislt)


# 统计list元素
name_lislt= ["黄东明",False, 666]
count = len(name_lislt)
print(count)


# list 遍历

for x in name_lislt:
    print(x)



# 元组 定义之后不可修改 名称 = ()  tuple
a = ("黄东明",)
print(a)
print(type(a))

b = ("黄东明","月薪过万")
count = b.count("黄东明")
print(count)



# 字符串， 定义之后也是无法修改

name="黄东明月薪过万！"
print(name)



