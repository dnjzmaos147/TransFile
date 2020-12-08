# Labeling-File Conversion
데이터 라벨링작업을 위해 파일을 txt, xlsx, json 등으로 변환합니다.<br>

python의 openpyxl과 json 활용<br><br>


----------------


v0.1.0<br>
1. 원본 텍스트 파일을 한줄씩 읽어와 기본 전처리 적용하여 띄어쓰기 기준 토큰화 후 단어를 원본문장과 엑셀에 저장 (txt_to_xl.py)<br>
2. json파일을 엑셀로 전환 (json_to_xl.py)<br> 
3. 수작업된 엑셀파일을 json 파일로 변환(xl_to_json.py)<br>
4. json파일을 읽어 중복된 단어를 제거하여 단어사전 파일생성 (label_dict.py) <br>
5. 파일이름이나 디렉토리 전체파일을 단어사전과 매칭해 기존에 쓰였던 단어 라벨링 (json_to_LABEL.py)

-------
<br>


       

json 파일을 불러와 변수에 저장
```python
with open('최종사전_1206_수정완료.json', 'rt', encoding='UTF8') as json_file:
    cate_dict = json.load(json_file)
```
<br>

기존 사전단어와 일치하는 단어를 찾는 함수
```python
def matching_label(obj):
    for ca in cate_dict:
        if ca['value'] == obj['value']:
            return ca
    result = {
        "standard": "TTA_BASIC",
		"categoryID": None,
		"type": "literal",
		"value": obj['value']
    }
    return result
```
<br>

open 함수 2번째 인자에 'w'을 입력하여 쓰기모드로 json 파일을 저장
```python
with open('./LABEL/{}.json'.format(fileName), 'w', encoding='utf-8') as outfile:
    json.dump(output_json, outfile, indent='\t', ensure_ascii=False)
```
<br>

openpyxl의 Workbook 클래스를 사용하여 xl파일 읽고쓰기 가능
```python
from openpyxl import Workbook
# 워크북 생성
wb = Workbook()
 
# 워크북 활성화
ws = wb.active
```
<br>

ws.append함수를 이용해 xl행의 추가되는  cell 정의
```python
ws.append([
            line,
            match_result['standard'],
            match_result['categoryID'],
            'literal',
            match_result['value']
])
```
<br>

wb.save함수로 경로와 파일이름을 정해 엑셀파일 저장
```python
wb.save('./xlfile/{}.xlsx'.format(fileName))
```
<br>


<br><br>

### TODO LIST
1. 기존에 파일이름이나 디렉토리 경로를 입력하면서 작업에 맞는 파이썬파일을 매번 실행하는 것이 아닌 하나의 웹페이지나 실행파일로 통합된 라벨링툴로 개발






