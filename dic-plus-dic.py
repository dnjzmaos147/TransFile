
import json

fname = '1203_plz'

with open('{}.json'.format(fname), 'rt', encoding='UTF8') as json_file:
    new_json = json.load(json_file)

with open('7개 용어사전_1203_영선 라벨링.json', 'rt', encoding='UTF8') as json_file:
    before_cate = json.load(json_file)

data = []
data = before_cate

def intent_duplicate(text):
    for ca in before_cate:
        if ca['value'] == text:
            return False
    return True

for row in new_json:
    if intent_duplicate(row['value']):
        data.append(row)
    


with open('./마지막직전사전.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent='\t', ensure_ascii=False)
