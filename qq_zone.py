from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


options = webdriver.ChromeOptions()
#	设置无图模式
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
# options.add_argument('--headless')          # 浏览器隐藏
options.add_argument('--disable-gpu')
options.add_experimental_option('prefs', prefs)        #设置无图模式
browser = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(browser, 5)


def get_last_page():
    url = 'https://user.qzone.qq.com/2955859128/311' # 空间说说的网址
    browser.get(url)
    time.sleep(3)
    try:
        browser.find_element(By.NAME, 'login_frame')  # 发现登陆的frame
    except:
        raise
    else:
        try:
            browser.switch_to_frame('login_frame')  # 发现之后进入login_frame
            login = wait.until(EC.element_to_be_clickable(
                (By.ID, 'img_out_2955859128')))  # 点击头像登录空间
            time.sleep(3)
            login.click()
        except Exception as e:
            raise
    time.sleep(3)
    browser.switch_to_frame('app_canvas_frame')  # 进入说说的frame
    time.sleep(1)

    with open('text.txt', 'a', encoding='utf-8') as f:
        # 一页有20条说说
        for k in range(20):
            # 尝试对每一条说说点击（展开全文）
            try:
                browser.find_element_by_xpath('//*[@id="msgList"]/li[{}]/div[3]/div[2]/div/a'.format(k+1)).click()
            except:
                pass
            time.sleep(1.5)
            # 利用xpath获取日期和文本信息
            text=browser.find_element_by_xpath('//*[@id="msgList"]/li[{}]/div[3]/div[2]/pre'.format(k+1)).get_attribute('textContent')
            date=browser.find_element_by_xpath('//*[@id="msgList"]/li[{}]/div[3]/div[4]/div[1]/span/a'.format(k + 1)).get_attribute('title')


            print(k+1)
            print(date)

            # 保存日期和文本信息
            f.write(str([date,text]) + '\n')

        time.sleep(1.5)

        # 一共有n页
        for m in range(10):
            browser.find_element_by_id('pager_num_{}_{}'.format(m,m+2)).click() # 跳转到第m页
            time.sleep(1.5)
            for k in range(20):
                try:
                    browser.find_element_by_xpath('//*[@id="msgList"]/li[{}]/div[3]/div[2]/div/a'.format(k + 1)).click()
                except:
                    pass
                time.sleep(1.5)
                text = browser.find_element_by_xpath('//*[@id="msgList"]/li[{}]/div[3]/div[2]/pre'.format(k + 1)).get_attribute(
                    'textContent')

                date = browser.find_element_by_xpath(
                    '//*[@id="msgList"]/li[{}]/div[3]/div[4]/div[1]/span/a'.format(k + 1)).get_attribute('title')
                print(m,k+1)
                print(date)
                f.write(str([date, text]) + '\n')
            time.sleep(1.5)





if __name__ == '__main__':
    page_last = get_last_page()
