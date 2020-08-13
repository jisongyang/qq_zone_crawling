
import re
import pickle
def save_pickle(var,name='name'):
    with open(name,'wb') as f:
        pickle.dump(var,f)

def load_pickle(name='name'):
    with open(name,'rb') as f:
        data=pickle.load(f)
    return data


#########################
# serch data
#########################

def show_detail(dict):
    if type(dict)==list:
        for dic in dict:
            print(dic['date'])
            for sentence in dic['content']:
                print(sentence)
            print('lenth',dic['lenth'])
    else:
        print(dict['date'])
        for sentence in dict['content']:
            print(sentence)
        print('lenth', dict['lenth'])

def get_date(list):
    return [x['date'] for x in list]

def get_lenth(list):
    return [int(x['lenth']) for x in list]

def get_highlight_dict(str,dict):
    new_content=[]
    html_str='<font color="red">{}</font>'.format(str)
    for sentence in dict['content']:
        if str in sentence:
            sentence_list=sentence.split(str)
            new_sentence=html_str.join(sentence_list)
        else:
            new_sentence=sentence
        new_content.append(new_sentence)
    html_font_dict=dict.copy()
    html_font_dict['content']=new_content
    return html_font_dict

def search_content(keyword_list,search_range,show_first_content_sentence=False,show_all_content=False):
    if(keyword_list[0]=='' and len(keyword_list)==1):
        return search_range
    else:
        dict_search_result = []
        for str in keyword_list:
            dict_search_result = []
            for dict in search_range:
                for sentence in dict['content']:
                    if str in sentence:
                        html_font_dict=get_highlight_dict(str,dict)
                        dict_search_result.append(html_font_dict)
                        if show_all_content:
                            show_detail(dict)
                            break
                        if show_first_content_sentence:
                            print(dict['date'])
                            print(sentence)
                            break
                        break
            search_range=dict_search_result


        if(len(dict_search_result))==0:
            print('Can not find!')
        return dict_search_result

def search_date(date_list,search_range,show_all_content=False):
    if(date_list[0]=='' and date_list[1]=='' and date_list[2]==''):
        return search_range
    else:
        dict_search_result=[]
        for dict in search_range:
            date_split=[dict['date'][0][:4],dict['date'][0][4:6],dict['date'][0][6:8]]
            if((date_list[0]=='' or date_list[0]==date_split[0]) and
            (date_list[1]=='' or date_list[1]==date_split[1]) and
            (date_list[2]=='' or date_list[2]==date_split[2])):
                if show_all_content:
                    show_detail(dict)
                dict_search_result.append(dict)
        if (len(dict_search_result)) == 0:
            print('Can not find!')
        return dict_search_result

def search_lenth(len_list,search_range,show_date=False,show_all_content=False):
    [min, max] = len_list
    if(min=='' and max==''):
        return search_range
    else:
        min = int(min) if min != '' else 0
        max = int(max) if max != '' else 1e4
        dict_search_result=[]
        for dict in search_range:
            if ((min<int(dict['lenth'])) and (int(dict['lenth'])<max)):
                if show_date:
                    print(dict['date'])
                if show_all_content:
                    show_detail(dict)
                dict_search_result.append(dict)
        if (len(dict_search_result)) == 0:
            print('Can not find!')
        return dict_search_result


if __name__=='__main__':
    total_diary=load_pickle('/diary_dict')
    #
    # dict=search_content('爷爷',total_diary,show_first_content_sentence=True)
    dict=search_lenth(['1500',''],total_diary,show_date=True,show_all_content=True)




