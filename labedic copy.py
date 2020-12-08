from openpyxl import Workbook
import re
import json

import os

from openpyxl import load_workbook







output_json = []
        
drop_word = []


   

 
path_dir = './LABEL'
 
file_list = os.listdir(path_dir)

data = []
# 워크북 생성
wb = Workbook()
 
# 워크북 활성화
ws = wb.active




for flist in file_list:
    fileName = flist


    # fileName = fileName.replace('.xlsx', '')

    with open('./LABEL/{}'.format(fileName), 'rt', encoding='UTF8') as json_file:
        js_data = json.load(json_file)


    def catch_drop(text):
        for word in drop_word:
            if text == word:
                return False
        return True


    # def match_cate(js_obj):
    #     for ca in cate_dict:
    #         if js_obj['value'] == ca['value']:
    #             return ca
    #     return js_obj


    def intent_duplicate(obj):
        for ob in data:
            if ob['value'] == obj['value']:
                return False
        return True

    jsdata = {}
    for line in js_data:
        jsdata = js_data[line]
        break




    for li in jsdata:
        for onejs in jsdata[li]:
            if intent_duplicate(onejs):
                data.append(onejs)


for wo in data:
    if wo['standard'] == 'TTA Basic':
        wo['standard'] = 'TTA_BASIC'
    ws.append([
        wo['standard'],
        wo['categoryID'],
        wo['type'],
        wo['value'],
    ])



wb.save('dict.xlsx')

