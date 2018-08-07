import jieba
jieba.load_userdict("dict.txt")
jieba.set_dictionary("dict.txt")
ret = open("keyword.csv", "r",encoding='utf-8-sig').read()
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
    
    f.write(str(hash))