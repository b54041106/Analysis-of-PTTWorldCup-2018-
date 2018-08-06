from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(6,9)) #调节图形大小
labels = [u'2018',u'2017',u'2016',u'2015',u'2014'] #定义标签
sizes = [7279,219,124,244,2136] #每块值
colors = ['red','yellowgreen','lightskyblue','yellow','blue'] #每块颜色定义
explode = (0.1,0.1,0.1,0.1,0.1) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
#patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.title('2014.8-2018.7_Posts_pie chart');
plt.show()