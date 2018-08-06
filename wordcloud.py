import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse
import codecs
from wordcloud import WordCloud

# 設定為繁中字典
jieba.load_userdict("dict.txt")
str_load=jieba.cut('dict.txt',cut_all=True) #全模式
jieba.set_dictionary("dict.txt")

def stopwords(filepath):  
    stopwords = [line.strip() for line in open('chinese.txt', 'r', encoding='utf-8').readlines()]  
    return stopwords
# 每首歌的前10大tag
with open("keyword.csv", "r",encoding='utf-8-sig') as f1:
    for line in f1:
        words = jieba.analyse.extract_tags(line,10)
        print(",".join(words))
f1.close()

# 把所有歌的10大tags取N個tags
with open("keyword.csv", "rb") as f2:
    for line in f2:
        tags = jieba.analyse.extract_tags(line,15) #取Ｎ個tags
        print(",".join(tags))
f2.close()


# 讀取欲透過文字雲計算詞頻的檔案
text = open("keyword.csv",encoding='utf-8-sig').read() #繁體字"gbk
# 建立停用字
stop= stopwords('chinese.txt')

wc = WordCloud(font_path="C:\Windows\Fonts\Microsoft JhengHei UI.ttf", #設置字體
               background_color="white", #背景顏色
               max_words = 2000) #文字雲顯示最大詞數
               #stop =stopwords) #停用字詞


# 產生文字雲
wc.generate(text)

# 視覺化
plt.imshow(wc)
plt.axis("off")
plt.figure(figsize=(10,6), dpi = 100)
plt.show()

# 存檔
wc.to_file("wordcloud1.jpg")