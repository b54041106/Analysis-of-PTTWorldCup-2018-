import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse
import codecs
from wordcloud import WordCloud

#設定為繁中字典
jieba.load_userdict("dict.txt")
str_load=jieba.cut('dict.txt',cut_all=True) #全模式
jieba.set_dictionary("dict.txt")

with open("keyword.csv", "w+",encoding='utf-8-sig') as f2:
    with open("worldcup.csv", "r",encoding='utf-8-sig') as f1:
        for line in f1:
            tags = jieba.analyse.extract_tags(line,15)
            #words = jieba.analyse.extract_tags(line,10)
            t=' '.join(tags)
            f2.write(t)

# 讀取欲透過文字雲計算詞頻的檔案
text = open("keyword.csv",encoding='utf-8-sig').read() #繁體字"gbk

# 建立停用字
stop=set()
stop.update(['新聞'],['公告'],['感想'],['問題'],['討論'],['什麼'],['Re'],['開始'],['是不是'],['本屆'],['Live'],['Group'],
['VS'],['連結'],['不會'],['球隊'],['X1'],['FT'],['進攻'],['世界杯'],['世足賽'],['情報'],['X3'],['X2'],['剛剛'],['為何'],
['Fw'],['階段'],['影片'],['還是'],['世界'],['心得'],['怎麼'],['這屆'],['足球'],['舉辦'],['現在'],['這次'],['分類'],['球星'],
['球員'],['機會'],['關於'],['分享'],['這場'],['隊伍'],['看世足'],['這樣'],['運動'],['請問'],['表現'],['閒聊'],['X5'],
['球衣'],['時間'],['應該'],['沒有'],['不行'],['WOQ'],['hoseumou'],['那麼'],['這麼'],['還有'],['我們'],['一樣'],['哪裡'],['覺得']
,['網友'],['WCQ'],['比賽'],['國家'],['joanzkow'],['分鐘'],['歷史'],['球場'],['一場'],['足球賽'],['國際足'],['人名'])


wc = WordCloud(font_path="C:\Windows\Fonts\mingliu.ttc",#設置字體
               background_color="white", #背景顏色
               max_words = 2000,stopwords =stop) #停用字詞

# 產生文字雲
wc.generate(text)

# 視覺化
plt.imshow(wc)
plt.axis("off")
# plt.figure(figsize=(10,6), dpi = 100)
plt.show()

