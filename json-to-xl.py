from openpyxl import Workbook
import re
import json





fileName = 'H-37-2011 근로자의 우울증 예방을 위한 관리감독자용 지침'

# 워크북 생성
wb = Workbook()
 
# 워크북 활성화
ws = wb.active


with open('{}.json'.format(fileName), 'rt', encoding='UTF8') as json_file:
    js_data = json.load(json_file)


with open('plz.json', 'rt', encoding='UTF8') as json_file:
    cate_dict = json.load(json_file)


jdata = {}
for j in js_data:
    jdata = js_data[j]
    break


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



for line in jdata:
    cnt = 1
    for onejs in jdata[line]:
        match_result = match_dict(onejs)
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

    




wb.save('{}.xlsx'.format(fileName))