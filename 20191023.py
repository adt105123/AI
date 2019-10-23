
# coding: utf-8

# In[33]:


# Jieba三種斷詞法

# Jieba1
#encoding=utf-8
import jieba
jieba.set_dictionary('dictionary/dict.txt.big.txt') 

seg_list = jieba.cut("我來到台中教育大學",cut_all=True)
print ("Full Mode:", "/ ".join(seg_list)) #全模式

seg_list = jieba.cut("我來到台中教育大學",cut_all=False)
print ("Default Mode:", "/ ".join(seg_list)) #精確模式

seg_list = jieba.cut("我來到台中教育大學") #默認是精確模式
print (", ".join(seg_list))

seg_list = jieba.cut_for_search("志明碩士畢業於台中教育大學，後在日本東京大學深造") #搜索引擎模式
print (", ".join(seg_list))


sentence = "我來到台中教育大學就讀碩士"
# 預設模式斷詞
breakword = jieba.cut(sentence, cut_all=False)
print("預設模式:" + '|' . join(breakword))

# 全文模式斷詞
breakword = jieba.cut(sentence, cut_all=True)
print("全文模式:" + '|' . join(breakword))

# 搜尋引擎模式斷詞
breakword = jieba.cut_for_search(sentence)
print("搜尋引擎:" + '|' . join(breakword))


# In[43]:



import jieba

jieba.set_dictionary('dictionary/dict.txt.big.txt')  

jieba.load_userdict('dictionary/user_dict.txt')

with open('dictionary/stopword.txt', 'r', encoding='utf-8-sig') as file:
    stops = file.read().split('\n')
print("停用詞:"+'|' . join(stops))

sentence = "明天上課請攜帶紅色教科書。預計會上到自然語言處理技術Ch7"

jieba.add_word('自然語言處理技術')
jieba.add_word('紅色教科書')
jieba.del_word('會上')

breakword = jieba.cut(sentence, cut_all=False)
final_words = []

for word in breakword:
    if word not in stops:
        final_words.append(word)
print("去除停用:" + '|' . join(final_words))

breakword = jieba.cut(sentence, cut_all=False)
print("預設模式:" + '|' . join(breakword))    

breakword = jieba.cut(sentence, cut_all=True)
print("全文模式:" + '|' . join(breakword))

breakword = jieba.cut_for_search(sentence)
print("搜尋引擎:" + '|' . join(breakword))

