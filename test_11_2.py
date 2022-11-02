import jieba
import wordcloud

txt = open("三国演义.txt","r",encoding="utf-8").read()
words=jieba.lcut(txt)
counts={}


for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1

# for word in words:
#     if len(word)!=1:
#         counts[word]=counts.get(word,0)+1

items=list(counts.items())

items.sort(key=lambda x:x[1],reverse=True)

# words=''.join(words)
#
# w= wordcloud.WordCloud(font_path='simhei.ttf',width=2000,height=1000,background_color='white')
# w.generate(words)
# w.to_file('1.jpg')


for i in range(10):
    word,count=items[i]
    print(word,count)