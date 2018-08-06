import jieba

ret = open("keyword.csv", "r").read()
seglist = jieba.cut(ret, cut_all=False)

import json
hash = {}
for item in seglist: 
  if item in hash:
    hash[item] += 1
  else:
    hash[item] = 1
json.dump(hash,open("count.json","w"))

fd = open("count.csv","w")
fd.write("word,count\n")
for k in hash:
  fd.write("%s,%d\n"%(k.encode("utf8"),hash[k]))

b=b'\xe7\xbe\x85'
s1=b.decode(encoding='utf-8')
print(s1)

