from openpyxl import Workbook
import re
import json




# 워크북 생성
wb = Workbook()
 
# 워크북 활성화
ws = wb.active


with open('1차확정사전.json', 'rt', encoding='UTF8') as json_file:
    js_data = json.load(json_file)




for row in js_data:
    ws.append([
        row['standard'],
        row['categoryID'],
        row['type'],
        row['value']
    ])

    

wb.save('1차확정 사전_1203.xlsx')