# -*- coding: utf-8 -*- 

from openpyxl import Workbook
import re
import json
import pandas as pd
from konlpy.tag import Okt

okt = Okt()

with open('category_dict.json', 'rt', encoding='UTF8') as json_file:
    cate_dict = json.load(json_file)

# 파일명
fileName = 'G-25-2011 눈 보호구의 선정 및 유지보수에 관한 안전가이드'

# 워크북 생성
wb = Workbook()
 
# 워크북 활성화
ws = wb.active

with open('./textfile/{}.txt'.format(fileName), 'rt', encoding='UTF8') as read:
    text_file = read.readlines()

drop_josa_one = ['은', '는', '이', '가', '와', '에', '및','을', '를', '과', '의', '된','로', '만', '적','될', '들','할','히']
drop_josa_worddict = ['되더라도','하여야한다','있어서도','하므로써','하였을','아니된다','일지라도','했음에도','나타난다','하려는','알려주고','해지거나','이루어지기','바람직하다','일어나기','만들어진','씌운다','올리는데','때문이다','때문에','갖추어야','되어있어야','않는다면','과도하게','적절한','적절히','있는데','알려주어야','따른다','특별한','인하여','갖춰야','시키도록','하다면','이었는지','이였는지','해야한다','없어야','없도록','하여서','갖는다','받으면서','되거나','것으로서','함으로써','되면서','하였다면','대해서도','하였거나','되었는지','받는다','일으킬','하고자','있는가', '하는가','대하여는','관련하여','관련된','관하여','관련한','관한','관련','의해서만','시키고','높아야','대해서','하면서','하는지','하는것','한다면','해지고','해주는','통해서','못한다','통하여','알아야','하는데','되어져야','있으며','있으면','만든다','놓으면','놓았을','놓아야','놓는다','따라야','따르며','따라서','있으나','대하여','놓이지','놓이게','위해서는','에서도','하더라도','라는','하므로','만들고','이러한','정하는','까지','과는','그리고','되는지','이므로','않도록','적이어야','있어서','이어야','있어야','않는다','시킨다','않아야','아니라','말아야','말하며','의한다','와의','의한','또는','되고','되지','와는','하기','하지만','및','에는','있거나','되도록','해서','된다면','된다','할지','에만','같은','시키기','반드시','만드는','시키는','미치지','하든가','시키며','이어서','이여서','되므로','되는','받거나','된대로','말한다','으로써','으로서','나오는','이거나', '으로부터', '으로','이면서','이면','로부터', '에서', '위하여','있는지', '이며','있을', '있으므로', '있도록','적인', '되어야', '하여야','하다', '에도', '시켜야', '로서','하게','하거나','일으킬','에게','있다면','있다고','되어', '하고','하지', '받아야','있고','하며','하도록', '하는', '같다', '이라고','또한','또','있다','있는','해야','의해서','특별하게','특별히', '의해', '갖는','대한', '이다','있게', '처럼','않을', '하여','한다','받은','시킬','바에', '이나','로써','부터','되며','있음','하되', '준다','이와','들은','들의','들이','많은', '많다', '있어','대해','인한', '위해', '혹은','되듯','보다', '특히', '높게','않은', '않는', '얻을', '되면', '하에', '되게', '위한', '들어', '쉽다', '하면','받는', '받게', '받고','통해','했을', '인해', '받을', '시켜', '마다','좋다','하려고','받아', '있지', '따른', '다른', '따라', '가까이','가까운','않으면', '않다', '한다고', '적어도', '않게','쉽게','이라', '없다', '있기', '같이']



def drop_josa(text): 
    for d2 in drop_josa_worddict:
        if d2 in text:
            return text.replace(d2, '')
    return text

def preprocessing(text):
    # 개행문자 제거
    text = str(text)
    text = re.sub('\\\\n', '', text)
    fix_text = re.sub('[^가-힣ㄱ-ㅎㅏ]', ' ', text)
    return fix_text.strip()

def fixte(te):
    if not te == '내' and not te == '함' and not te == '이' and not te == '라' and not te == '밖' and not te == '위' and not te == '이상' and not te == '눈'and not te == '시' and not te == '수' and not te == '것':
        return True
    return False

data = []
for line in text_file:
    fix_word_arr = []
    fix_line =  preprocessing(line)
    word_arr = fix_line.split(' ')
    # word_arr = okt.nouns(fix_line)
    for te in word_arr:
        te_flag = True
        te = drop_josa(te)
        if not te == "":
            for dr in drop_josa_one:
                if te[-1] == dr:
                    fix_te = te[:-1]
                    
                    if not fix_te == "":
                        if fixte(fix_te):
                            fix_word_arr.append(fix_te)
                        te_flag = False
            if te_flag:
                if fixte(te):

                    fix_word_arr.append(te)
    data.append({
        'full_line' : line,
        'one_word' : fix_word_arr
    })



wo_list = []
for wo in data:
    cnt =1
    st = ""
    for w in wo['one_word']: 
        flag = True
        if cnt == wo['one_word'].__len__():
            
            for ca in cate_dict:
                if w == ca['value']:
                    ws.append([
                        wo['full_line'],
                        ca['standard'],
                        ca['categoryID'],
                        "literal",
                        w
                    ])
                    flag = False
                    break
            if flag:
                ws.append([
                   wo['full_line'],
                   "TTA Basic",
                   "",
                   "literal",
                   w
                ])
        else:
            for ca in cate_dict:
                if w == ca['value']:
                    ws.append([
                        "",
                        ca['standard'],
                        ca['categoryID'],
                        "literal",
                        w
                    ])
                    flag = False
                    break
            if flag:
                ws.append([
                "",
                "TTA Basic",
                "",
                "literal",
                w
                ])
        cnt += 1


wb.save('./xlfile/{}.xlsx'.format(fileName))