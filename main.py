import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
dict_1 = {}
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
list_6 = []
list_7 = []
#в словаре dict_1 ключами являются поля из заголовка csv файла, значениями - списки с людьми и их данными
for i in contacts_list:
    string = ','.join(i)
    list_1.append((''.join(list(string.split(',')[0]))).split()[0])
    dict_1['lastname'] = list_1[1:]

    if len((''.join(list(string.split(',')[0]))).split()) > 1:
        list_2.append((''.join(list(string.split(',')[0]))).split()[1])
        dict_1['firstname'] = list(filter(None,list_2[0:]))
    if len((''.join(list(string.split(',')[1]))).split()) < 1:
        list_2.append((''.join(list(string.split(',')[1]))).split())
        dict_1['firstname'] = list(filter(None,list_2[1:]))
    else:
        list_2.append((''.join(list(string.split(',')[1]))).split()[0])
        dict_1['firstname'] = list(filter(None,list_2[1:]))

    if len((''.join(list(string.split(',')[0]))).split()) > 2:
        list_3.append((''.join(list(string.split(',')[0]))).split()[2])
        dict_1['surname'] = list_3[1:]
    if len((''.join(list(string.split(',')[1]))).split()) >= 2:
        list_3.append((''.join(list(string.split(',')[1]))).split()[1])
        dict_1['surname'] = list_3[1:]
    if len((''.join((string.split(',')[2]))).split()) >= 1:
        list_3.append((''.join((string.split(',')[2]))).split()[0])
        dict_1['surname'] = list_3[1:]
    if len((''.join(list(string.split(',')[0]))).split()) <= 2 \
            and len((''.join(list(string.split(',')[1]))).split()) <= 0 \
            and len((''.join(list(string.split(',')[2]))).split()) <= 0:
        list_3.append('')
        dict_1['surname'] = list_3[1:]

    if len((''.join(list(string.split(',')[3]))).split()) >= 1:
        list_4.append((''.join(list(string.split(',')[3]))).split()[0])
        dict_1['organization'] = list(filter(None,list_4[1:]))
    if len ((''.join(list(string.split(',')[1]))).split()) <= 0 and \
            len ((''.join(list(string.split(',')[2]))).split()) <= 0 and \
            len ((''.join(list(string.split(',')[3]))).split()) <= 0 and \
            len ((''.join(list(string.split(',')[4]))).split()) <= 0:
        list_4.append('')
        dict_1['organization'] = list_4[1:]
    list_5.append((''.join(list(string.split(',')[4]))))
    dict_1['position'] = list_5[1:]
    list_6.append((''.join(list(string.split(',')[5]))))
    dict_1['phone'] = list_6[1:]
    list_7.append((''.join(list(string.split(',')[6]))))
    dict_1['email'] = list_7[1:]

list_heads_0 = []
list_name_1 = []
list_name_2 = []
list_name_3 = []
list_name_4 = []
list_name_5 = []
list_name_6 = []
list_name_7 = []
list_name_8 = []
contacts_list_1 = []
contacts_list_1.append(list_heads_0)
#преобразование словаря dict_1 в упорядоченный список списков для записи в файл
for key in dict_1.keys():
    list_heads_0.append(key)
for value in dict_1.values():
    list_name_1.append(value[0])
    list_name_2.append(value[1])
    list_name_3.append(value[2])
    list_name_4.append(value[3])
    list_name_5.append(value[4])
    list_name_6.append(value[5])
    list_name_7.append(value[6])
    list_name_8.append(value[7])
resulting_list = []

#удаление дублей сравнением всех списков между собой по имени и фамилии, и каждого элемента в каждом списке с соответствующим элементом в релевантном списке
if list_name_1[0] == list_name_2[0] and list_name_1[1] == list_name_2[1]:
    for i in [0, 1, 2, 3, 4, 5, 6]:
        if list_name_1[i] != '' and list_name_2[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_2[i] != '' and list_name_1[i] == '':
            resulting_list.append(list_name_2[i])
        elif list_name_1[i] == '' and list_name_2[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_1[i] == list_name_2[i]:
            resulting_list.append(list_name_1[i])
    contacts_list_1.append(resulting_list)
    resulting_list = []
    list_name_1 = [0]
    list_name_2 = [0]
if list_name_1[0] == list_name_3[0] and list_name_1[1] == list_name_3[1]:
    for i in [0, 1, 2, 3, 4, 5, 6]:
        if list_name_1[i] != '' and list_name_3[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_3[i] != '' and list_name_1[i] == '':
            resulting_list.append(list_name_3[i])
        elif list_name_1[i] == '' and list_name_3[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_1[i] == list_name_3[i]:
            resulting_list.append(list_name_1[i])
    contacts_list_1.append(resulting_list)
    resulting_list = []
    list_name_1 = [0]
    list_name_3 = [0]
if list_name_1[0] == list_name_4[0] and list_name_1[1] == list_name_4[1]:
    for i in [0, 1, 2, 3, 4, 5, 6]:
        if list_name_1[i] != '' and list_name_4[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_4[i] != '' and list_name_1[i] == '':
            resulting_list.append(list_name_4[i])
        elif list_name_1[i] == '' and list_name_4[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_1[i] == list_name_4[i]:
            resulting_list.append(list_name_1[i])
    contacts_list_1.append(resulting_list)
    resulting_list = []
    list_name_1 = [0]
    list_name_4 = [0]
if list_name_1[0] == list_name_5[0] and list_name_1[1] == list_name_5[1]:
    for i in [0, 1, 2, 3, 4, 5, 6]:
        if list_name_1[i] != '' and list_name_5[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_5[i] != '' and list_name_1[i] == '':
            resulting_list.append(list_name_5[i])
        elif list_name_1[i] == '' and list_name_5[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_1[i] == list_name_5[i]:
            resulting_list.append(list_name_1[i])
    contacts_list_1.append(resulting_list)
    resulting_list = []
    list_name_1 = [0]
    list_name_5 = [0]
if list_name_1[0] == list_name_6[0] and list_name_1[1] == list_name_6[1]:
    for i in [0, 1, 2, 3, 4, 5, 6]:
        if list_name_1[i] != '' and list_name_6[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_6[i] != '' and list_name_1[i] == '':
            resulting_list.append(list_name_6[i])
        elif list_name_1[i] == '' and list_name_6[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_1[i] == list_name_6[i]:
            resulting_list.append(list_name_1[i])
    contacts_list_1.append(resulting_list)
    resulting_list = []
    list_name_1 = [0]
    list_name_6 = [0]
if list_name_1[0] == list_name_7[0] and list_name_1[1] == list_name_7[1]:
    for i in [0, 1, 2, 3, 4, 5, 6]:
        if list_name_1[i] != '' and list_name_7[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_7[i] != '' and list_name_1[i] == '':
            resulting_list.append(list_name_7[i])
        elif list_name_1[i] == '' and list_name_7[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_1[i] == list_name_7[i]:
            resulting_list.append(list_name_1[i])
    contacts_list_1.append(resulting_list)
    resulting_list = []
    list_name_1 = [0]
    list_name_7 = [0]
if list_name_1[0] == list_name_8[0] and list_name_1[1] == list_name_8[1]:
    for i in [0, 1, 2, 3, 4, 5, 6]:
        if list_name_1[i] != '' and list_name_8[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_8[i] != '' and list_name_1[i] == '':
            resulting_list.append(list_name_8[i])
        elif list_name_1[i] == '' and list_name_8[i] == '':
            resulting_list.append(list_name_1[i])
        elif list_name_1[i] == list_name_8[i]:
            resulting_list.append(list_name_1[i])
    contacts_list_1.append(resulting_list)
    resulting_list = []
    list_name_1 = [0]
    list_name_8 = [0]
else:
    contacts_list_1.append(list_name_1)

if list_name_2 != [0]:
    if list_name_2[0] == list_name_3[0] and list_name_2[1] == list_name_3[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_2[i] != '' and list_name_3[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_3[i] != '' and list_name_2[i] == '':
                resulting_list.append(list_name_3[i])
            elif list_name_2[i] == '' and list_name_3[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_2[i] == list_name_3[i]:
                resulting_list.append(list_name_2[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_2 = [0]
        list_name_3 = [0]
    elif list_name_2[0] == list_name_4[0] and list_name_2[1] == list_name_4[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_2[i] != '' and list_name_4[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_4[i] != '' and list_name_2[i] == '':
                resulting_list.append(list_name_4[i])
            elif list_name_2[i] == '' and list_name_4[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_2[i] == list_name_4[i]:
                resulting_list.append(list_name_2[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_2 = [0]
        list_name_4 = [0]
    elif list_name_2[0] == list_name_5[0] and list_name_2[1] == list_name_5[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_2[i] != '' and list_name_5[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_5[i] != '' and list_name_2[i] == '':
                resulting_list.append(list_name_5[i])
            elif list_name_2[i] == '' and list_name_5[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_2[i] == list_name_5[i]:
                resulting_list.append(list_name_2[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_2 = [0]
        list_name_5 = [0]
    elif list_name_2[0] == list_name_6[0] and list_name_2[1] == list_name_6[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_2[i] != '' and list_name_6[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_6[i] != '' and list_name_2[i] == '':
                resulting_list.append(list_name_6[i])
            elif list_name_2[i] == '' and list_name_6[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_2[i] == list_name_6[i]:
                resulting_list.append(list_name_2[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_2 = [0]
        list_name_6 = [0]
    elif list_name_2[0] == list_name_7[0] and list_name_2[1] == list_name_7[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_2[i] != '' and list_name_7[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_7[i] != '' and list_name_2[i] == '':
                resulting_list.append(list_name_7[i])
            elif list_name_2[i] == '' and list_name_7[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_2[i] == list_name_7[i]:
                resulting_list.append(list_name_2[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_2 = [0]
        list_name_7 = [0]
    elif list_name_2[0] == list_name_8[0] and list_name_2[1] == list_name_8[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_2[i] != '' and list_name_8[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_8[i] != '' and list_name_2[i] == '':
                resulting_list.append(list_name_8[i])
            elif list_name_2[i] == '' and list_name_8[i] == '':
                resulting_list.append(list_name_2[i])
            elif list_name_2[i] == list_name_8[i]:
                resulting_list.append(list_name_2[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_2 = [0]
        list_name_8 = [0]
    else:
        contacts_list_1.append(list_name_2)

if list_name_3 != [0]:
    if list_name_3[0] == list_name_4[0] and list_name_3[1] == list_name_4[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_3[i] != '' and list_name_4[i] == '':
                resulting_list.append(list_name_3[i])
            elif list_name_4[i] != '' and list_name_3[i] == '':
                resulting_list.append(list_name_4[i])
            elif list_name_3[i] == '' and list_name_4[i] == '':
                resulting_list.append(list_name_3[i])
            elif list_name_3[i] == list_name_4[i]:
                resulting_list.append(list_name_3[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_3 = [0]
        list_name_4 = [0]
    elif list_name_3[0] == list_name_5[0] and list_name_3[1] == list_name_5[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_3[i] != '' and list_name_5[i] == '':
                resulting_list.append(list_name_3[i])
            elif list_name_5[i] != '' and list_name_3[i] == '':
                resulting_list.append(list_name_5[i])
            elif list_name_3[i] == '' and list_name_5[i] == '':
                resulting_list.append(list_name_3[i])
            elif list_name_3[i] == list_name_5[i]:
                resulting_list.append(list_name_3[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_3 = [0]
        list_name_5 = [0]
    elif list_name_3[0] == list_name_6[0] and list_name_3[1] == list_name_6[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_3[i] != '' and list_name_6[i] == '':
                resulting_list.append(list_name_3[i])
            elif list_name_6[i] != '' and list_name_3[i] == '':
                resulting_list.append(list_name_6[i])
            elif list_name_3[i] == '' and list_name_6[i] == '':
                resulting_list.append(list_name_3[i])
            elif list_name_3[i] == list_name_6[i]:
                resulting_list.append(list_name_3[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_3 = [0]
        list_name_6 = [0]
    elif list_name_3[0] == list_name_7[0] and list_name_3[1] == list_name_7[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_3[i] != '' and list_name_7[i] == '':
                resulting_list.append(list_name_3[i])
            elif list_name_7[i] != '' and list_name_3[i] == '':
                resulting_list.append(list_name_7[i])
            elif list_name_3[i] == '' and list_name_7[i] == '':
                resulting_list.append(list_name_3[i])
            elif list_name_3[i] == list_name_7[i]:
                resulting_list.append(list_name_3[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_3 = [0]
        list_name_7 = [0]
    elif list_name_3[0] == list_name_8[0] and list_name_3[1] == list_name_8[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_3[i] != '' and list_name_8[i] == '':
                resulting_list.append(list_name_3[i])
            elif list_name_8[i] != '' and list_name_3[i] == '':
                resulting_list.append(list_name_8[i])
            elif list_name_3[i] == '' and list_name_8[i] == '':
                resulting_list.append(list_name_3[i])
            elif list_name_3[i] == list_name_8[i]:
                resulting_list.append(list_name_3[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_3 = [0]
        list_name_8 = [0]
    else:
        contacts_list_1.append(list_name_3)

if list_name_4 != [0]:
    if list_name_4[0] == list_name_5[0] and list_name_4[1] == list_name_5[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_4[i] != '' and list_name_5[i] == '':
                resulting_list.append(list_name_4[i])
            elif list_name_5[i] != '' and list_name_4[i] == '':
                resulting_list.append(list_name_5[i])
            elif list_name_4[i] == '' and list_name_5[i] == '':
                resulting_list.append(list_name_4[i])
            elif list_name_4[i] == list_name_5[i]:
                resulting_list.append(list_name_4[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_4 = [0]
        list_name_5 = [0]
    if list_name_4[0] == list_name_6[0] and list_name_4[1] == list_name_6[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_4[i] != '' and list_name_6[i] == '':
                resulting_list.append(list_name_4[i])
            elif list_name_6[i] != '' and list_name_4[i] == '':
                resulting_list.append(list_name_6[i])
            elif list_name_4[i] == '' and list_name_6[i] == '':
                resulting_list.append(list_name_4[i])
            elif list_name_4[i] == list_name_6[i]:
                resulting_list.append(list_name_4[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_4 = [0]
        list_name_6 = [0]
    if list_name_4[0] == list_name_7[0] and list_name_4[1] == list_name_7[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_4[i] != '' and list_name_7[i] == '':
                resulting_list.append(list_name_4[i])
            elif list_name_7[i] != '' and list_name_4[i] == '':
                resulting_list.append(list_name_7[i])
            elif list_name_4[i] == '' and list_name_7[i] == '':
                resulting_list.append(list_name_4[i])
            elif list_name_4[i] == list_name_7[i]:
                resulting_list.append(list_name_4[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_4 = [0]
        list_name_7 = [0]
    if list_name_4[0] == list_name_8[0] and list_name_4[1] == list_name_8[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_4[i] != '' and list_name_8[i] == '':
                resulting_list.append(list_name_4[i])
            elif list_name_8[i] != '' and list_name_4[i] == '':
                resulting_list.append(list_name_8[i])
            elif list_name_4[i] == '' and list_name_8[i] == '':
                resulting_list.append(list_name_4[i])
            elif list_name_4[i] == list_name_8[i]:
                resulting_list.append(list_name_4[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_4 = [0]
        list_name_8 = [0]
    else:
        contacts_list_1.append(list_name_4)

if list_name_5 != [0]:
    if list_name_5[0] == list_name_6[0] and list_name_5[1] == list_name_6[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_5[i] != '' and list_name_6[i] == '':
                resulting_list.append(list_name_5[i])
            elif list_name_6[i] != '' and list_name_5[i] == '':
                resulting_list.append(list_name_6[i])
            elif list_name_5[i] == '' and list_name_6[i] == '':
                resulting_list.append(list_name_5[i])
            elif list_name_5[i] == list_name_6[i]:
                resulting_list.append(list_name_5[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_5 = [0]
        list_name_6 = [0]
    if list_name_5[0] == list_name_7[0] and list_name_5[1] == list_name_7[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_5[i] != '' and list_name_7[i] == '':
                resulting_list.append(list_name_5[i])
            elif list_name_7[i] != '' and list_name_5[i] == '':
                resulting_list.append(list_name_7[i])
            elif list_name_5[i] == '' and list_name_7[i] == '':
                resulting_list.append(list_name_5[i])
            elif list_name_5[i] == list_name_7[i]:
                resulting_list.append(list_name_5[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_5 = [0]
        list_name_7 = [0]
    if list_name_5[0] == list_name_8[0] and list_name_5[1] == list_name_8[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_5[i] != '' and list_name_8[i] == '':
                resulting_list.append(list_name_5[i])
            elif list_name_8[i] != '' and list_name_5[i] == '':
                resulting_list.append(list_name_8[i])
            elif list_name_5[i] == '' and list_name_8[i] == '':
                resulting_list.append(list_name_5[i])
            elif list_name_5[i] == list_name_8[i]:
                resulting_list.append(list_name_5[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_5 = [0]
        list_name_8 = [0]
    else:
        contacts_list_1.append(list_name_5)

if list_name_6 != [0]:
    if list_name_6[0] == list_name_7[0] and list_name_6[1] == list_name_7[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_6[i] != '' and list_name_7[i] == '':
                resulting_list.append(list_name_6[i])
            elif list_name_7[i] != '' and list_name_6[i] == '':
                resulting_list.append(list_name_7[i])
            elif list_name_6[i] == '' and list_name_7[i] == '':
                resulting_list.append(list_name_6[i])
            elif list_name_6[i] == list_name_7[i]:
                resulting_list.append(list_name_6[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_6 = [0]
        list_name_7 = [0]
    if list_name_6[0] == list_name_8[0] and list_name_6[1] == list_name_8[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_6[i] != '' and list_name_8[i] == '':
                resulting_list.append(list_name_6[i])
            elif list_name_8[i] != '' and list_name_6[i] == '':
                resulting_list.append(list_name_8[i])
            elif list_name_6[i] == '' and list_name_8[i] == '':
                resulting_list.append(list_name_6[i])
            elif list_name_6[i] == list_name_8[i]:
                resulting_list.append(list_name_6[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_6 = [0]
        list_name_8 = [0]
    else:
        contacts_list_1.append(list_name_6)

if list_name_7 != [0]:
    if list_name_7[0] == list_name_8[0] and list_name_7[1] == list_name_8[1]:
        for i in [0, 1, 2, 3, 4, 5, 6]:
            if list_name_7[i] != '' and list_name_8[i] == '':
                resulting_list.append(list_name_7[i])
            elif list_name_8[i] != '' and list_name_7[i] == '':
                resulting_list.append(list_name_8[i])
            elif list_name_7[i] == '' and list_name_8[i] == '':
                resulting_list.append(list_name_7[i])
            elif list_name_7[i] == list_name_8[i]:
                resulting_list.append(list_name_7[i])
        contacts_list_1.append(resulting_list)
        resulting_list = []
        list_name_7 = [0]
        list_name_8 = [0]
    else:
        contacts_list_1.append(list_name_7)

#форматирование номеров телефонов с использованием regex и перезапись в списки в корректном формате:
for i in contacts_list_1:
    i[5] = re.sub(r'(^\+7|^8)?(\s*)?([(])?(\d{3})?([)])?(\W)?(\d{3})?(\W)?(\d{2})?(\W)?(\d{2})(\s*)?([(])?(\w{3})?(\.)?(\s*)?(\d{4})?([)])?', r'+7(\4)\7-\9-\11 \14\15\17', i[5])

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list_1)

