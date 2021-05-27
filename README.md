# qq_zone_crawling

three parts in this repository

1. craw logs frome qq_zone
  (log in to qq_zone by click QQ Avatar in web)
  (set qq account in qq_zone.py and run)
  (can get all logs text)
 
2. show in a simple interface
  (run diary_process.py: get a dict for all logs)
  (diary_search.py: search data in dict, some functions)
  (run interface.py: an interface based on pyqt5)
 
3. show through word cloud
  (run diary_stat.py)
 
 
 by the way, if you have installed pyinstallner.exe, you can get a exe file by running the following command in CMD(windows)
 【pyinstaller.exe -i diary_ico.ico -w -F interface.py -p diary_search.py -p showwindow.py】
