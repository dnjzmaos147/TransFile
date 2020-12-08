import openpyxl
import json

from openpyxl import load_workbook

import os
 
path_dir = 'C:/Users/82109/Desktop/2cha/xlfile/1ro'
 
file_list = os.listdir(path_dir)

for flist in file_list:
    fname = flist.replace('.xlsx', '')
    angelEx=load_workbook(filename='./xlfile/1ro/{}.xlsx'.format(fname))

    sheet = angelEx['Sheet']


    output_json = []
            
    data = []


    multiple_cells = sheet['A1':'E15000']
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

