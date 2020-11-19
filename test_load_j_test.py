import os
import jieba
import json
from os import listdir
import os, jieba, json, re


#open
# with open('./interior_talk_05_ta/【TV】狹長格局暢行無阻！大人小孩都圈粉的低奢莫蘭迪.json', 'r', encoding='utf-8-sig') as f:
#     output = json.load(f)
# print(output)


#open
# with open('./interior_talk_06_ta/當自己的森林之王！單身男子的 10 坪自然系高收納宅.json', 'r', encoding='utf-8-sig') as f:
#     output = json.load(f)
# print(output)
#
#
# analysis_1 = list(output.values())[0]
# print(analysis_1)
#
# analysis_2 = list(output.values())[5]
# print(analysis_2)


# print(os.getcwd())

#os.listdir(r'./interior_talk_06_ta/')
# close(r)



path = 'D:/pytel_data/interior_talk_0923_ta_remix'
filelist = listdir(path)
# fileIndex =[]
# for i in range(1,len(filelist)+1):
#     index = i
#     fileIndex.append(int(index))
# print(fileIndex)

all_data = []
def onlyText(data):
    return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", data)
for fileName in filelist:
    with open(path + '/' + fileName, 'r', encoding='utf-8-sig') as f:
        data = f.readline()
        json_data = json.loads(data)
        # print(fileName)
        try:

        except:

        all_data.append(json_data)

    print(all_data)
# print(type(all_data))