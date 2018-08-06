import pandas as pd
import matplotlib.pyplot as plt

date=[ ' 6/01', ' 6/02', ' 6/03', ' 6/04', ' 6/05', ' 6/06', ' 6/07', ' 6/08', ' 6/09', ' 6/10', ' 6/11', ' 6/12', ' 6/13', ' 6/14', ' 6/15', ' 6/16', ' 6/17', ' 6/18', ' 6/19', ' 6/20', ' 6/21', ' 6/22', ' 6/23', '6/24', ' 6/25', ' 6/26', ' 6/27', ' 6/28', ' 6/29', ' 6/30', ' 7/01', ' 7/02', ' 7/03', ' 7/04', ' 7/05', ' 7/06', ' 7/07', ' 7/08', ' 7/09', ' 7/10', ' 7/11', ' 7/12', ' 7/13', ' 7/14', ' 7/15', ' 7/16', ' 7/17', ' 7/18', ' 7/19', ' 7/20', ' 7/21', ' 7/22', ' 7/23', ' 7/24', ' 7/25', ' 7/26', ' 7/27', ' 7/28', ' 7/29', ' 7/30', ' 7/31']
posts=[8, 21, 16, 10, 11, 10, 10, 14, 12, 12, 12, 16, 18, 42, 100, 185, 153, 301, 233, 192, 141, 253, 193, 282, 226, 197, 309, 445, 276, 181, 337, 334, 313, 212, 104, 128, 280, 165, 63, 66, 161, 170, 63, 103, 149, 320, 66, 33, 21,
11, 9, 6, 16, 10, 2, 8, 5, 7, 3, 5, 4]

x=date
y=posts

plt.figure(figsize=(10,6))
plt.plot(x,y,color='blue',linewidth=2.0,linestyle='-')
plt.xlabel('Date')
plt.ylabel('Posts')
plt.xticks(fontsize=7,rotation=90) 
plt.title('2018WorldCup_Jun&Jul_PTTposts');
plt.show()

#dict = {'date': date,'posts':posts}
#df = pd.DataFrame(dict)
df=pd.DataFrame({ 'date': [' 6/01', ' 6/02', ' 6/03', ' 6/04', ' 6/05', ' 6/06', ' 6/07', ' 6/08', ' 6/09', ' 6/10', ' 6/11', ' 6/12', ' 6/13', ' 6/14', ' 6/15', ' 6/16', ' 6/17', ' 6/18', ' 6/19', ' 6/20', ' 6/21', ' 6/22', ' 6/23', '6/24', ' 6/25', ' 6/26', ' 6/27', ' 6/28', ' 6/29', ' 6/30', ' 7/01', ' 7/02', ' 7/03', ' 7/04', ' 7/05', ' 7/06', ' 7/07', ' 7/08', ' 7/09', ' 7/10', ' 7/11', ' 7/12', ' 7/13', ' 7/14', ' 7/15', ' 7/16', ' 7/17', ' 7/18', ' 7/19', ' 7/20', ' 7/21', ' 7/22', ' 7/23', ' 7/24', ' 7/25', ' 7/26', ' 7/27', ' 7/28', ' 7/29', ' 7/30', ' 7/31']
,
               'posts':[8, 21, 16, 10, 11, 10, 10, 14, 12, 12, 12, 16, 18, 42, 100, 185, 153, 301, 233, 192, 141, 253, 193, 282, 226, 197, 309, 445, 276, 181, 337, 334, 313, 212, 104, 128, 280, 165, 63, 66, 161, 170, 63, 103, 149, 320, 66, 33, 21,
11, 9, 6, 16, 10, 2, 8, 5, 7, 3, 5, 4]
})
print(df)
print(df.describe())

df.to_excel("statistic.csv",columns =['date','posts'])
# import pandas as pd
# import csv
# import numpy as np
# import matplotlib.pyplot as plt

# csv_data = pd.read_csv('worldcup.csv',encoding="utf-8") # 讀取訓練資料 
# csv_data['recommends']=csv_data['recommends'].str.replace("爆",'101')
# csv_data['recommends']=csv_data['recommends'].str.replace("X2",'-11')
# x1=csv_data['recommends']
# y1=csv_data['date']
# df1=pd.DataFrame({ 'recommends':x1,
#                   'date':y1
# })
# print(df1.describe())
# plt.rcParams['font.family']='SimHei' #⿊體

# print('corr: ',df1[['recommends','date']].corr())
# df1.plot(x='recommends',y='date',kind='scatter',title='散布圖')
# plt.show()