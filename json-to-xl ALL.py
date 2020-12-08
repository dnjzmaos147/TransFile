from openpyxl import Workbook
import re
import json


import os
 
path_dir = 'C:/Users/82109/Desktop/2cha/xl-daro'
 
file_list = os.listdir(path_dir)


def match_dict(text):
    for ca in cate_dict:
        if text['value'] == ca['value']:
            return ca
    nomatch = text
    return nomatch

# def match_dict(text):
#     for ca in cate_dict:
#         if text['value'] == ca['value']:
#             return ca
#     nomatch = {
#         'standard' : 'TTA_BASIC',
#         'categoryID' : '',
#         'type' : 'literal',
#         'value' : text['value']
#     }
#     return nomatch

with open('plz.json', 'rt', encoding='UTF8') as json_file:
    cate_dict = json.load(json_file)

for flist in file_list:
    fileName = flist.replace('.json', '')    

        # 워크북 생성
    wb = Workbook()
    
    # 워크북 활성화
    ws = wb.active




    with open('./jsfile/{}.json'.format(fileName), 'rt', encoding='UTF8') as json_file:
        js_data = json.load(json_file)





    jdata = {}
    for j in js_data:
        jdata = js_data[j]
        break








    for line in jdata:
        cnt = 1
        for onejs in jdata[line]:
            match_result = onejs
            if cnt == jdata[line].__len__():
                ws.append([
                    line,
                    match_result['standard'],
                    match_result['categoryID'],
                    'literal',
                    match_result['value']
                ])
            else:
                ws.append([
                    "",
                    match_result['standard'],
                    match_result['categoryID'],
                    'literal',
                    match_result['value']
                ])
            cnt += 1

        




    wb.save('./xl-output/{}.xlsx'.format(fileName))