# -*- coding: utf-8 -*- 

from openpyxl import Workbook
import re
import json
import pandas as pd
from konlpy.tag import Okt

import os
 
path_dir = 'C:/Users/bct1/Desktop/transfile/textfile'
 
file_list = os.listdir(path_dir)




with open('category_dict.json', 'rt', encoding='UTF8') as json_file:
    cate_dict = json.load(json_file)


drop_josa_one = ['은', '는', '이', '가', '와', '에', '및','을', '를', '과', '의', '된','로', '만', '적','될', '들']
drop_josa_worddict = ['의해서만','시키고','대해서','하는지','하는것','한다면','알아야','하는데','되어져야','있으나','대하여','위해서는','에서도','하더라도','라는','하므로','정하는','까지','과는','그리고','되는지','않도록','적이어야','이어야','있어야','않는다','않아야','말하며','의한다','와의','또는','되고','되지','와는','하기','하지만','및','에는','되도록','해서','된다','할지','에만','같은','시키기','되는','말한다','이거나', '으로부터', '으로','로부터', '에서', '위하여','있는지', '이며','있을', '있으므로', '있도록','적인', '되어야', '하여야','하다', '에도', '시켜야', '로서','하게','하거나','에게','있다면','되어', '하고','하지', '받아야','있고','하며','하도록', '하는', '같다', '이라고','또한','또','있다','있는','해야','의해서', '의해', '갖는', '이다','있게', '처럼','않을', '하여','한다','받은']


for file_name in file_list:
    
    fileName = file_name.replace('.txt', '')


    wb = Workbook()
    

    ws = wb.active

    with open('./textfile/{}.txt'.format(fileName), 'rt', encoding='UTF8') as read:
        text_file = read.readlines()





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
                            fix_word_arr.append(fix_te)
                            te_flag = False
                if te_flag:
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