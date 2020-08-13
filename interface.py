import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont,QIcon
from showwindow import *
from diary_search import *

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('My diary')
        self.setWindowIcon(QIcon('diary_ico'))
        self.content_input.setFont(QFont("Calibri", 12))
        self.year_input.setFont(QFont("Calibri", 12))
        self.month_input.setFont(QFont("Calibri", 12))
        self.day_input.setFont(QFont("Calibri", 12))
        self.min_input.setFont(QFont("Calibri", 12))
        self.max_input.setFont(QFont("Calibri", 12))

        self.submit.clicked.connect(self.search)
        self.dele.clicked.connect(self.dele_query)
    def content(self,search_range,keyword_list):
        dict = search_content(keyword_list, search_range)
        return dict

    def date(self,search_range,date_list):
        dict=search_date(date_list,search_range)
        return dict

    def lenth(self,search_range,len_list):
        dict = search_lenth(len_list,search_range)
        return dict

    def search(self):
        keyword_list=self.content_input.text().split(' ')
        # keyword = self.content_input.toPlainText()
        [year,month,day]=[self.year_input.text(),self.month_input.text(),self.day_input.text()]
        [min,max]=[self.min_input.text(),self.max_input.text()]
        date_result_dicts = self.date(total_diary,[year,month,day])
        content_result_dicts =self.content(date_result_dicts,keyword_list)
        result_dicts = self.lenth(content_result_dicts,[min,max])

        self.show_result(result_dicts )

    def show_result(self,dicts):
        ## date_show
        self.date_show.setPlainText('Result: {} days'.format(len(dicts)))
        for dict in dicts:
            self.date_show.setFont(QFont("Calibri",12))
            self.date_show.append(dict['date'][0]+'\t'+dict['date'][1]+'\t'+str(dict['lenth']))
        ## stat_show
        self.stat_show.setFont(QFont("Calibri", 12))
        self.stat_show.setPlainText('【月份统计】')
        stat_date_dict={}
        stat_time_dict={}
        for dict in dicts:
            year=dict['date'][0][:4]
            month=dict['date'][0][4:6]
            time_hour=dict['date'][1].split(':')[0]
            if(year not in stat_date_dict):
                stat_date_dict[year]={}
            if(month not in stat_date_dict[year]):
                stat_date_dict[year][month]=0
            stat_date_dict[year][month]+=1
            if(time_hour not in stat_time_dict):
                stat_time_dict[time_hour]=0
            stat_time_dict[time_hour]+=1

        for year,month_dict in stat_date_dict.items():
            self.stat_show.append(year)
            now_str=''
            for month,freq in month_dict.items():
                if(freq<10):
                    freq='0'+str(freq)
                now_str=now_str+month+'月'+'【'+str(freq)+'】'+'\t'
            self.stat_show.append("<p><font size='1'>{}</font></p>".format(now_str))
        self.stat_show.append('\n')
        self.stat_show.append('【时间统计】')
        now_str = ''
        for i in range(24):
            if(str(i) in stat_time_dict):
                if(i<10):
                    hour= '0' + str(i)
                else:
                    hour=str(i)
                now_str = now_str + hour + '时' + '【' + str(stat_time_dict[str(i)]) + '】' + '\t'
        self.stat_show.append("<p><font size='1'>{}</font></p>".format(now_str))

        ## detail_show
        self.detail_show.setPlainText('Result: {} days'.format(len(dicts)))
        for dict in dicts:
            self.detail_show.setFont(QFont("Calibri", 10))
            self.detail_show.append('【{}】'.format(dict['date'])+'\t'+'Length:{}'.format(str(dict['lenth'])))
            for sentence in dict['content']:
                self.detail_show.append(sentence)

    def dele_query(self):
        self.content_input.setText('')
        self.year_input.setText('')
        self.month_input.setText('')
        self.day_input.setText('')
        self.min_input.setText('')
        self.max_input.setText('')


if __name__ == '__main__':
    total_diary = load_pickle('diary_dict')


    app = QApplication(sys.argv)
    myWin = MyWindow()

    myWin.show()
    sys.exit(app.exec_())