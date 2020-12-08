import json

fileName = 'H-27-2011 택시, 버스 운전원의 직무스트레스 예방을 위한 관리감독자용 지침'

with open('{}.json'.format(fileName), 'rt', encoding='UTF8') as json_file:
    input_json = json.load(json_file)

with open('category_dict.json', 'rt', encoding='UTF8') as json_file:
    before_category = json.load(json_file)

result_data = []
for bca in  before_category:
    result_data.append(bca)

new_js_data = {}
for ij in input_json:
    new_js_data = input_json[ij]
    
def check_new_word(dic_obj):
    for ca in result_data:
        if dic_obj['value'] == ca['value']:
            return True
    return False

    
for line in new_js_data:
    for row in new_js_data[line]:
        if not check_new_word(row):
            result_data.append(row)


with open('./category_dict.json', 'w', encoding='utf-8') as outfile:
    json.dump(result_data, outfile, indent='\t', ensure_ascii=False)