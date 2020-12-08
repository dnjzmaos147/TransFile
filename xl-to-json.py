import openpyxl
import json

from openpyxl import load_workbook


fname = 'H-37-2011 근로자의 우울증 예방을 위한 관리감독자용 지침'
angelEx=load_workbook(filename='./{}.xlsx'.format(fname))

sheet = angelEx['Sheet']


output_json = []
        
data = []


multiple_cells = sheet['A1':'E97064']
for row in multiple_cells:
    cell_arr = []

    for cell in row:

        cell_arr.append(cell.value)
    one_row = {
        'standard':cell_arr[1],
        'categoryID':cell_arr[2],
        'type':cell_arr[3],
        'value':cell_arr[4],
    }
    data.append(one_row)
    if not cell_arr[0] == None:
        title = cell_arr[0]
        result = {
            title : data
        }
        output_json.append(result)
        data = []


injson = {}

for o in output_json:
    injson.update(o)

final_j = {
    "{}.hwp".format(fname):injson
}
    


with open('./{}.json'.format(fname), 'w', encoding='utf-8') as outfile:
    json.dump(final_j, outfile, indent='\t', ensure_ascii=False)

