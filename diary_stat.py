import jieba
from collections import Counter
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from imageio import imread
remove_list=['，','。','！','n','\\','？',' ','\'']

import pickle
def save_pickle(var,name='name'):
    with open(name,'wb') as f:
        pickle.dump(var,f)

def load_pickle(name='name'):
    with open(name,'rb') as f:
        data=pickle.load(f)
    return data
def recover_list(str):
    state_list=str[1:-2].split(', ')
    recover=[state[1:-1] for state in state_list]
    return recover

########################
# jieba split
########################
result_lists=[]
with open('diary.txt','r',encoding='utf-8') as f:
    datas=f.readlines()
    for data in datas:
        data=recover_list(data)
        # print(data)
        jieba_list=list(jieba.cut(data[1]))
        result_list=[x for x in jieba_list if x not in remove_list]
        # print(result_list)

        result_lists.append([data[0],result_list])
save_pickle(result_lists,'diary_jieba_word')


#########################
# clear data
#########################

diary_list=load_pickle('diary_jieba_word')
total_word=[]
for data in diary_list:
    total_word.extend(data[1])
print('word num:',len(total_word))

stopword_list=[')','(','_','《','》','（','）','～',':','┯','ﾉ','﹏','＝',';','ﾟ','̀','́','”','“'
               '╯','╯','╰','╮','╭','」','∠','˘','~','“','ง','＿',',','ฅ','з','●','•',
               'ε','?','Д','↯','ԅ','了','','ಡ','ω','￣','/','+','ｰ','✘','ノ','இ','︵','︿',
               '﹀','"','｡','｀','→','･','◉','〃','：','︶','>','<','▼','*','д','ㅂ','ヽ','|',
               'o','`','≧','≦','¯','๑','´','㉨','-','⊙','✪','^','ಥ','Ծ','▽','—','=']
# with open('stop_word_zh.txt','r',encoding='utf-8') as f:
#     for data in f.readlines():
#         stopword_list.append(data.strip())

total_word_new=[x for x in total_word if x not in stopword_list]
print('use word num:',len(total_word_new))

count_result=Counter(total_word_new)
print(count_result)
num=0

print(len(count_result))
print(type(count_result))

#########################
# wordcloud
#########################
color_mask=imread('D:\software\ps\image\pkq_wordcloud.png')
w=WordCloud(
    font_path='ErZiYuanXinYouShouHuiB-2.ttf',
    max_words=700,
    max_font_size=100,
    mask=color_mask,
    relative_scaling=0.7
)
diary_word_cloud=w.generate_from_frequencies(count_result)
print('done!')
diary_word_cloud.to_file('20200625.png')
plt.imshow(diary_word_cloud,interpolation='bilinear')
plt.show()


