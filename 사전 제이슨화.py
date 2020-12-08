import openpyxl
import json

from openpyxl import load_workbook


fname = './dict/99개 개체명사전_1207'
angelEx=load_workbook(filename='./{}.xlsx'.format(fname))

sheet = angelEx['Sheet']


output_json = []
        
data = []


multiple_cells = sheet['A1':'D10883']
for row in multiple_cells:
    cell_arr = []

    for cell in row:

        cell_arr.append(cell.value)
    one_row = {
        'standard':cell_arr[0],
        'categoryID':cell_arr[1],
        'type':cell_arr[2],
        'value':cell_arr[3],
    }
    data.append(one_row)





with open('./{}.json'.format(fname), 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent='\t', ensure_ascii=False)
