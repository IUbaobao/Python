import wordcloud,jieba,requests
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup

# 生成词云
def makewordcloud(filename):
    """filename:文件名称
      生成词云图"""
    words = open(filename, "r",encoding='utf-8').read()
    words = jieba.lcut(words)
    words = ' '.join(words)
    w = wordcloud.WordCloud(font_path='simhei.ttf', width=1000, height=600, background_color='white')
    w.generate(words)
    w.to_file('new.jpg')


# 处理文件内容，返回文件中频率最高的前十的词语和出现的频率次数
def dispose_file(filename,len1):
    words=open(filename,"r",encoding='utf-8').read()
    words=jieba.lcut(words)
    str=""
    for word in words:
        if word=='行' and str=='还' :# 对‘还行’这个词进行特殊处理
            words.append(str+word)
        str=word

    print(words)
    counts={}
    for word in words:
        if len(word)==1:
            continue
        counts[word]=counts.get(word,0)+1

    items = list(counts.items())  # 字典转成列表类型以便排序
    items.sort(key=lambda x: x[1], reverse=True)
    labels =[]
    size=[]

    for i in range(len1):
        word,count = items[i]
        labels.append(word)
        size.append(count)
    return labels,size # 返回两个列表，一个是频率最高的词语，另一个是对于的频率次数

# 生成饼图
def drawPie(filename):
    labels,size=dispose_file(filename,5)
    sum=0
    for num in size:
        sum+=num
    sizes=[]
    expl=[0.1,0,0,0,0] # #第一块即出现频率最高的那个词语离开圆心0.1
    colors = ["blue", "red", "coral", "green", "yellow", "orange"]  # 设置颜色（循环显示）
    plt.rcParams['font.family'] = 'SimHei'  # 配置参数显示中文
    plt.rcParams['font.sans-serif'] = 'SimHei'
    for num in size:# 计算比例
        sizes.append(num / sum)
    plt.pie(sizes, labels=labels,autopct='%1.2f%%',explode=expl,shadow=True,colors=colors,pctdistance=0.8)
    plt.title('评分图')  # 设置标题
    plt.legend(loc='upper left', bbox_to_anchor=(-0.3, 1))  # bbox_to_anchor参数调整图例的位置
    plt.show()


# 生产条形图
def drawWordBar(filename,len1):
    labels,size=dispose_file(filename,len1)
    ls=[0,20,40,60,80,100,120]
    plt.rcParams['font.family'] = 'SimHei'  # 配置参数显示中文
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.bar(labels,size,label='次数')
    plt.legend()  # 显示图例
    plt.xlabel('词语')  # x轴标签
    plt.ylabel('出现次数')  # y轴标签
    plt.title('词频最高的{}个词语'.format(len1))  # 标题
    # 为每个条形图添加数值标签
    for x, y in enumerate(size):
        plt.text(x, y + 1, y, ha='center')
    plt.show()


# 生成雷达图
def drawRadar(filename):
    # 直接获取文件高频内容
    feature ,values =dispose_file(filename,5)
    # 用于正常显示中文
    plt.rcParams['font.sans-serif'] = 'SimHei'
    # 用于正常显示符号
    plt.rcParams['axes.unicode_minus'] = False
    # 使用ggplot的绘图风格
    plt.style.use('ggplot')

    # 设置每个数据点的显示位置，在雷达图上用角度表示
    angles = np.linspace(0, 2 * np.pi, len(values), endpoint=False)

    # 拼接数据首尾，使图形中线条封闭
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    # 添加一个标签，让其与values的值对应
    feature.append(feature[0])
    # 绘图
    fig = plt.figure()
    # 设置为极坐标格式
    ax = fig.add_subplot(111, polar=True)
    # 绘制折线图
    ax.plot(angles, values, linewidth=2)
    # 填充颜色
    ax.fill(angles, values, alpha=0.25)
    # 设置图标上的角度划分刻度，为每个数据点处添加标签
    ax.set_thetagrids(angles * 180/np.pi, feature,fontproperties="SimHei")
    # 添加标题
    plt.title('评分图')
    plt.show()

# 获取网页内容
def GetHTMLTxt(url):
    try:
        # 获取的时候添加 headers，进行爬虫伪装成浏览器进行访问
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"}
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        return "异常"

# 判断是否是汉字
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


# 获取网页文本内容，过虑无用信息
def HtmlTxt(ls):
    retlist=[]
    for ls_1 in ls:
        retlist.append(ls_1.text)
    return retlist


def is_Delete(word):
    if len(word) == 1 or not is_Chinese(word) or word \
            in ['展开', '不是', '一个', '一部', '可能', '这篇', '有剧', '因为', '什么', '但是', '这么'
        , '看到', '这么', '很多', '自己', '有人', '为了', '首先', '就是', '没有', '这部', '这个', '这样'
                ,'觉得','大家','可以','已经','还是','片子','我们']:
        return True
    return False

def split_word(words):
    strs = ""
    str=""
    for word in words:
        # 过虑没有用的词
        if word=='行' and str=='还' :# 对‘还行’这个词进行特殊处理
            strs+=str+word+" "
        str = word
        if is_Delete(word):
            continue
        strs += word
        strs += " "
    return strs

# 解析网页内容
def Text_parsing():
    ls=[]
    stat=20
    i=0
    Score_list=[]
    labels = ['力荐', '推荐', '还行', '较差', '很差']
    for i in range(10):
        # 翻页操作
        r = GetHTMLTxt("https://movie.douban.com/subject/26752088/reviews?start="+str(stat))
        soup = BeautifulSoup(r)
        ls.append(HtmlTxt(soup.find_all('div', attrs={"class": "short-content"})))
        for word in labels:
            Score_list.append((soup.find_all('span', {"title": word})))
        stat+=20
        print('正在爬第{}页'.format(i))
        i += 1

    words = jieba.lcut(str(ls))
    Score_list=jieba.lcut(str(Score_list))
    Score_str=split_word(Score_list)
    strs = split_word(words)

    return strs,Score_str

def Write_file(filename,str):
    fp = open(filename, "w",encoding='utf-8')
    fp.write(str)
    fp.close()



# filename="film.txt"
# Write_file(filename)
# makewordcloud(filename)
# drawPie(filename)
# drawWordBar(filename)
# drawRadar(filename)

# ls=[]
# r = GetHTMLTxt("https://movie.douban.com/subject/26752088/reviews?start=20")
# soup = BeautifulSoup(r)
# ls.append(soup.find_all('div', attrs={"class": "short-content"}))
# print(HtmlTxt(ls))
# # print(ls[0][0].text)
# ls1=[]
# i=0
# for lists in ls:
#     for l in lists:
#         # print(l.text)
#         ls1.append(l.text)
#
# print(ls1)

# Text_parsing()
# ls=[]
# labels = ['力荐', '推荐', '还行', '较差', '很差']
# r = GetHTMLTxt("https://movie.douban.com/subject/26752088/reviews?start=200")
# soup = BeautifulSoup(r)
# for word in labels:
#     ls.append((soup.find_all('span', {"title": word})))
# print(ls)
#
# print(ls)
strs,Score_str=Text_parsing()
# # print(Score_str)
filename1="film.txt"
filename2="Score_str.txt"
Write_file(filename1,strs)
Write_file(filename2,Score_str)
makewordcloud(filename1)
drawPie(filename2)
drawWordBar(filename1,10)
drawRadar(filename2)













