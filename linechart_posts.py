import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

csv_data = pd.read_csv('worldcup.csv',encoding='utf-8') # 讀取訓練資料 
new=csv_data.iloc[0:7279]
#new['date']=pd.to_datetime(new['date'])
data=new.sort_values(by = 'date',ascending=False)  #按照日期排序
df=data.drop([7278,7261,7260,7259,7258,3,4,5,6,7,8,9,10,11,12])
# print(df) 

#每日貼文量折線圖
gp_posts=df.groupby(by=['date']).size() #每天貼文數
print(gp_posts)
# print(type(gp_posts))

b=list(gp_posts.keys())
y=[]
for key in b:
    y.append(gp_posts[key])
print(b)
print(y)

x=(b)
y=(y)

plt.figure(figsize=(15,18))
plt.plot(x,y,color='blue',linewidth=2.0,linestyle='-')
plt.xlabel('Date')
plt.ylabel('Posts')
# plt.grid(axis='y', alpha=0.75)
# plt.subplots_adjust(bottom=0.8)
plt.xticks(fontsize=5,rotation=90) #设置x轴的标签的旋转角度
#plt.legend(["post", "date"], loc=2); # loc指的是legend要放的位置，loc=2是放在第二象限
plt.title('PTT_2018WorldCup_Posts');
plt.show()


