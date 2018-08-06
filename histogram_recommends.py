import pandas as pd
import csv
import xlrd
import matplotlib.pyplot as plt
import numpy as np

csv_data = pd.read_csv('worldcup.csv') # 讀取訓練資料dataframe 

csv_data['recommends']=csv_data['recommends'].str.replace("爆",'101')
csv_data['recommends']=csv_data['recommends'].str.replace("X2",'-11')
new=csv_data.iloc[:,1]
data=pd.to_numeric(new, errors='coerce') #型別轉換:str轉float

bins= [-20,-10,0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,110]
cat = pd.cut(data, bins)
print(cat)

def get_stats(group):
    return {'count': group.count()}
grouped = csv_data['recommends'].groupby(cat)
bin_counts = grouped.apply(get_stats).unstack()
print (bin_counts)

bin_counts.index = ['--','0','1~10', '11~20', '21~30', '31~40', '41~50', '51~60', '61~70',
                    '71~80', '81~90', '91~100','Bomb']
bin_counts.index.name = 'recommends'
bin_counts.plot(kind='bar', alpha=0.5, rot=0)
plt.show()