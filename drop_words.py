import json
import openpyxl
import json

from openpyxl import load_workbook




fname = '텍스트 라벨링 분류체계_20201203'
angelEx=load_workbook(filename='./{}.xlsx'.format(fname))

sheet = angelEx['제외단어']


output_json = []
        
drop_word_arr = []


multiple_cells = sheet['B1':'B553']
for row in multiple_cells:
    

    for cell in row:

        drop_word_arr.append(cell.value)
   

with open('찐마지막.json', 'rt', encoding='UTF8') as json_file:
    before_category = json.load(json_file)

def drop_wrod(text):
    for dw in drop_word_arr:
        if dw == text:
            return False
    return True


fresult = []
for row in before_category:
    if drop_wrod(row['value']):
        fresult.append(row)










with open('./1차확정사전.json', 'w', encoding='utf-8') as outfile:
    json.dump(fresult, outfile, indent='\t', ensure_ascii=False)