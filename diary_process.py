
from file_manage import *
from list_manage import *
import re
########################
# process diary data (from qq_zone.py )
########################

def count_character(check_str):
    count=0
    for ch in check_str:
        if (is_chinese(ch) or is_number(ch) or is_alphabet(ch)):
            count+=1
    return count
#
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def is_number(uchar):
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False

def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

## the file diary.txt generated by qq_zone.py

with open('diary.txt','r',encoding='utf-8') as f:
    datas=f.readlines()
    total_diary=[]
    for data in datas:
        data=recover_list(data)
        time_lis=data[0].split(' ')
        s = re.findall("\d+", time_lis[0])

        if len(s[1])==1:
            s[1] = '0' + s[1]
        if len(s[2])==1:
            s[2] = '0' + s[2]
        str=''
        date=str.join(s)
        try:
            date_list=[date,time_lis[1]]
        except:
            print(data)
            exit()

        content_list=data[1].split('\\n')

        character_num=0
        for sentence in content_list:
            character_num+=count_character(sentence)
        diary_dict={'date':date_list,'content':content_list,'lenth':character_num}
        total_diary.append(diary_dict)
    save_pickle(total_diary,'diary_dict')