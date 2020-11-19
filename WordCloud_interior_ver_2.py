#!/usr/bin/env python
# coding: utf-8

# In[1]:


# get_ipython().system('pip install jieba')


# In[2]:


# get_ipython().system('pip install wordcloud')


# In[3]:


import os, jieba, json, re


# In[4]:


import pandas as pd


# In[5]:


from os import listdir


# ### 連續開檔案

# In[6]:


path = 'D:/pytel_data/interior_talk_0923_ta_remix'


# In[7]:


filelist = listdir(path)


# In[8]:


fileIndex =[]


# In[9]:


for i in range(1,len(filelist)+1):
    index = i
    fileIndex.append(int(index))


# In[10]:


fileIndex


# In[ ]:


all_data = []
def onlyText(data):
    return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","", data)
for fileName in filelist:
    with open(path + '/' + fileName, 'r', encoding='utf-8-sig')  as f:
        data = f.read()
        json_data = json.loads(data)
        print(fileName)
        #new_data = ''.join(json_data['Product Information'][0]['產品資訊'] + json_data['You know']) + json_data['colour'] + json_data['title'] + json_data['summary']
        titelData = onlyText(''.join(json_data['title']))
        dateData = onlyText(''.join(json_data['date']))
        homeData = onlyText(''.join(json_data['home_data']))
        textData = onlyText(str(json_data['內文'] ))
        new_data = [titelData, textData, homeData, dateData, json_data['page_link']]
        all_data.append(new_data)


# In[ ]:


all_data


# In[11]:


part_data_title = []
def onlyText(data):
    return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","", data)
for fileName in filelist:
    with open(path + '/' + fileName, 'r', encoding='utf-8-sig')  as f:
        data = f.read()
        json_data = json.loads(data)
        print(fileName)
        #new_data = ''.join(json_data['Product Information'][0]['產品資訊'] + json_data['You know']) + json_data['colour'] + json_data['title'] + json_data['summary']
        titelData = onlyText(''.join(json_data['title']))
        dateData = onlyText(''.join(json_data['date']))
        remix = [titelData, dateData]
        part_data_title.append(remix)


# In[ ]:


# part_data_title


# In[12]:


part_data_title = str(part_data_title)


# In[ ]:


part_data_detal = []
def onlyText(data):
    return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","", data)
for fileName in filelist:
    with open(path + '/' + fileName, 'r', encoding='utf-8-sig')  as f:
        data = f.read()
        json_data = json.loads(data)
        print(fileName)
        #new_data = ''.join(json_data['Product Information'][0]['產品資訊'] + json_data['You know']) + json_data['colour'] + json_data['title'] + json_data['summary']
        textData = onlyText(str(json_data['內文'] ))
        part_data_detal.append(textData)


# In[ ]:


# part_data_detal


# In[ ]:


part_data_detal = str(part_data_detal)


# In[ ]:


part_data_detal = str(part_data_detal)


# In[ ]:


part_data_homedata = []
def onlyText(data):
    return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","", data)
for fileName in filelist:
    with open(path + '/' + fileName, 'r', encoding='utf-8-sig')  as f:
        data = f.read()
        json_data = json.loads(data)
        #print(fileName)
        #new_data = ''.join(json_data['Product Information'][0]['產品資訊'] + json_data['You know']) + json_data['colour'] + json_data['title'] + json_data['summary']
        homeData = onlyText(''.join(json_data['home_data']))
        part_data_homedata.append(homeData)


# In[ ]:


# part_data_homedata


# In[ ]:


df = pd.DataFrame(all_data, columns=['titel', 'text', 'homeDetel', 'date', 'page_link'])


# In[ ]:


# df


# In[ ]:





# In[ ]:


print(type(all_data))


# In[ ]:


print(type(df))


# In[ ]:


# all_data = str(df)


# In[ ]:


# all_data = str(all_data)


# In[ ]:


# all_data


# ### 分詞

# In[13]:


with open(file='text_to_use/stop_words.txt', mode='r', encoding='utf-8') as file:
    stop_words = file.read().split('\n')
stop_words


# In[ ]:


jieba.load_userdict('./text_to_use/mydict_ver_3.txt')

seg_stop_words_list = []
seg_words_list = jieba.lcut(all_data, cut_all = True)
for term in seg_words_list:
    if term not in stop_words:
        seg_stop_words_list.append(term)
print('/'.join(seg_stop_words_list))


# In[14]:


jieba.load_userdict('./text_to_use/mydict_ver_3.txt')

seg_stop_words_list_titel = []
seg_words_list = jieba.lcut(part_data_title, cut_all = True)
for term in seg_words_list:
    if term not in stop_words:
        seg_stop_words_list_titel.append(term)
print('/'.join(seg_stop_words_list_titel))


# In[ ]:


df_2 = pd.DataFrame(seg_stop_words_list, columns=['titel', 'text', 'homeDetel', 'date', 'page_link'])


# In[ ]:


print(type(seg_stop_words_list))


# In[ ]:


seg_stop_words_list = str(seg_stop_words_list)


# In[ ]:




