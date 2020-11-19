import os, jieba, json, re
import pandas as pd
from os import listdir


path = 'D:/pytel_data/interior_talk'
filelist = listdir(path)
fileIndex =[]

for i in range(1,len(filelist)+1):
    index = i
    fileIndex.append(int(index))

with open(file='text_to_use/stop_words.txt', mode='r', encoding='utf-8') as file:
    stop_words = file.read().split('\n')
jieba.load_userdict('./text_to_use/mydict_ver_3.txt')

part_data_detal = []
def onlyText(data):
    return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", data)
for fileName in filelist:
    with open(path + '/' + fileName, 'r', encoding='utf-8-sig') as f:
        data = f.read()
        json_data = json.loads(data)
        print(fileName)
        #new_data = ''.join(json_data['Product Information'][0]['產品資訊'] + json_data['You know']) + json_data['colour'] + json_data['title'] + json_data['summary']
        textData = onlyText(json_data['內文'])
        dateData = onlyText(''.join(json_data['date']))
        titelData = onlyText(''.join(json_data['title']))

        seg_stop_words_list_detal = []
        seg_words_list = jieba.lcut(textData, cut_all=True)
        for term in seg_words_list:
            if term not in stop_words:
                seg_stop_words_list_detal.append(term)
        remix = [fileName.replace(".json", ""), titelData, dateData, textData, seg_stop_words_list_detal]
        part_data_detal.append(remix)

df_detal = pd.DataFrame(part_data_detal, columns=['fileName', 'titel', 'date', 'text', 'jieba_text'])
# df_detal.index = df_detal.index + 1
print(df_detal)

#匯出csv 用excel (encoding='utf-8-sig')
df_detal.to_csv(r'D:/pytel_data/excel/Forum_detal.csv', encoding='utf-8-sig')