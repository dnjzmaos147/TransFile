#제이슨 전체 돌면서 cate 채우고 중복검사하고 제외단어 지우고 하나의  제이슨파일로 추출
import json
import openpyxl
from openpyxl import load_workbook
import os

path_dir = 'C:/Users/82109/Desktop/2cha/jsfile'
 
file_list = os.listdir(path_dir)


#적용할 단어사전
with open('용어사전_1203_영선완료.json', 'rt', encoding='UTF8') as json_file:
    before_category = json.load(json_file)

fname = '개체명가이드'
angelEx=load_workbook(filename='./{}.xlsx'.format(fname))
sheet = angelEx['제외단어']
drop_word_arr = []

#제외단어 셀범위
multiple_cells = sheet['B1':'B554']
for row in multiple_cells:
    for cell in row:
        drop_word_arr.append(cell.value)

def fit_category(obj):
    for bca in before_category:
        if obj['value'] == bca['value']:
            return bca
    result = {
        'standard' : 'TTA_BASIC',
        'categoryID' : '',
        'type' : 'literal',
        'value' : obj['value']
    }
    return result

#중복체크
def check_new_word(dic_obj):
    for ca in result_data:
        if dic_obj['value'] == ca['value']:
            return True
    return False

#제외단어
def drop_word(text):
    for dw in drop_word_arr:
        if text == dw:
            return False
    return True

result_data = []


for flist in file_list:
    fileName = flist.replace('.json', '')

    with open('./jsfile/{}.json'.format(fileName), 'rt', encoding='UTF8') as json_file:
        input_json = json.load(json_file)


    new_js_data = {}
    for ij in input_json:
        new_js_data = input_json[ij]
        
    for line in new_js_data:
        for row in new_js_data[line]:
            if not check_new_word(row):
                result_data.append(row)

js_result_dic_data = []
for raw in result_data:
    if drop_word(raw['value']):
        res = fit_category(raw)
        js_result_dic_data.append(res)



with open('./마지막4개.json', 'w', encoding='utf-8') as outfile:
    json.dump(js_result_dic_data, outfile, indent='\t', ensure_ascii=False)