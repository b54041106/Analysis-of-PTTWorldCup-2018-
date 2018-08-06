import numpy as np
import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
import csv

url='https://www.ptt.cc/bbs/WorldCup/index.html'
author_ids = [] # 建立一個空的 list 來放作者 id
recommends = [] # 建立一個空的 list 來放推文數
post_titles = [] # 建立一個空的 list 來放文章標題
post_dates = [] # 建立一個空的 list 來放發文日期
for round in range(500):
	res= requests.get(url) 
	soup= BeautifulSoup(res.text,'lxml')
	#換頁
	paging=soup.select('div.btn-group-paging a')
	next_url='https://www.ptt.cc'+paging[1]['href']
	url= next_url
	
	posts=soup.find_all("div", class_ = "r-ent")
	for post in posts:
		try:
			if soup.find("a"):
				author_ids.append(post.find("div", class_ = "author").string)    
		except:
			author_ids.append(np.nan)
		try:
			if soup.find("a"):
				post_titles.append(post.find("a").string)
		except:
			post_titles.append(np.nan)
		try:
			if soup.find("a"):
				post_dates.append(post.find("div", class_ = "date").string)
		except:
			post_dates.append(np.nan)

	recommendations = soup.find_all("div", class_ = "nrec")
	for recommendation in recommendations:
		try:
			if soup.find("a"):
				recommends.append((recommendation.find("span").string))
		except:
			recommends.append(0)

ptt_worldcup_dict = {"author": author_ids,
                "recommends": recommends,
                "title": post_titles,
                "date": post_dates
}

print(type(ptt_worldcup_dict))
ptt_worldcup_df = pd.DataFrame(ptt_worldcup_dict)
#ptt_worldcup_df.head()
#print(type(ptt_worldcup_df))
#print(ptt_worldcup_df)
ptt_worldcup_df.to_csv("Worldcup.csv",index=False,encoding='utf-8-sig',sep=',')

