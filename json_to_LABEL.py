import json
from openpyxl import load_workbook
import os
 
path_dir = './jsfile'
file_list = os.listdir(path_dir)


with open('최종사전_1206_수정완료.json', 'rt', encoding='UTF8') as json_file:
    cate_dict = json.load(json_file)

drop_fname = '텍스트 라벨링 분류체계_20201203'
angelEx=load_workbook(filename='./{}.xlsx'.format(drop_fname))
sheet = angelEx['제외단어']
drop_word_arr = []
multiple_cells = sheet['B1':'B553']
for row in multiple_cells:
    for cell in row:
        drop_word_arr.append(cell.value)

def drop_word(text):
    for dw in drop_word_arr:
        if dw == text:
            return False
    return True


def matching_label(obj):
    for ca in cate_dict:
        if ca['value'] == obj['value']:
            return ca
    # result = {
    #     "standard": "TTA_BASIC",
	# 	"categoryID": None,
	# 	"type": "literal",
	# 	"value": obj['value']
    # }
    result = obj
    return result


for flist in file_list:
    fileName = flist.replace('.json', '')

    with open('./jsfile/{}.json'.format(fileName), 'rt', encoding='UTF8') as json_file:
        input_js_data = json.load(json_file)


    js_data = {}
    title_name = ""
    for ij in input_js_data:
        title_name = ij
        js_data = input_js_data[title_name]


    data = {}
    for line in js_data:
        js_arr = []
        for one_word in js_data[line]:
            if drop_word(one_word['value']):
                result_row = matching_label(one_word)
                js_arr.append(result_row)
        one_line = {
            line : js_arr
        }
        data.update(one_line)

    output_json = {
        title_name : data
    }


    with open('./LABEL/{}.json'.format(fileName), 'w', encoding='utf-8') as outfile:
        json.dump(output_json, outfile, indent='\t', ensure_ascii=False)