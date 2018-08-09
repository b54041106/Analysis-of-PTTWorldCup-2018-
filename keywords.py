import jieba
jieba.load_userdict("dict.txt")
jieba.set_dictionary("dict.txt")
ret = open("worldcup.csv", "r",encoding='utf-8-sig').read()
seglist = jieba.cut(ret, cut_all=False)
#print(type(seglist))

import json
with open("noun.txt","w",encoding='utf-8-sig')as f:

    hash = {}
    for item in seglist: 
        if item in hash:
            hash[item] += 1
        else:
            hash[item] = 1
            print(item)
    text=json.dumps(hash,indent=4,ensure_ascii=False)    
    f.write(text)

#123.csv print(a)#new1.csv print(key)字詞#new2.csv print(value)出現次數
#sorted_keyword.csv.xlsx合併new1&2.csv,分類排序

with open('noun.txt', 'r',encoding='utf-8-sig') as j:
    with open('new1.csv', 'w+',encoding='utf-8-sig') as c:
        
        file_q= json.load(j)
        
        a=sorted(file_q.items(),key=lambda d:d[1],reverse=True)
        # c.write("\n")
        # c.write("\n")
        for key,value in a:
            print(key)
            c.write(key)
            c.write("\n")
        
    print(a)