
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
import pyperclip


browser = webdriver.Chrome()





# 登录
def login():
    # 登录地址
    browser.get('https://yqms.istarshine.com/v4/subject')
    time.sleep(2)
    # 打开登录链接后，我们手动登录，然后再获取cookies，这样就是登录后的cookies了。
    zh=browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/form/div/div[2]/div[1]/input')
    mm=browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/form/div/div[2]/div[2]/input')
    btn=browser.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/form/div/span')
    zh.send_keys('18380443581')
    time.sleep(1)
    mm.send_keys('ct000000*')
    btn.click()
    time.sleep(2)
    browser.get('https://yqms.istarshine.com/v4/search/')


def getcontent(kwd):
    input=browser.find_element_by_class_name('el-input__inner')
    input.send_keys(kwd)
    input.send_keys(Keys.ENTER)
    time.sleep(5)
    # 设置为当天
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]').click()
    # # 按去重键
    # browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[9]/div/div[1]').click()
    # 找到二级过滤框
    erjiguolv=browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/input')
    erjiguolv.send_keys('火车')
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/button/span').click()

    bls=browser.find_elements_by_xpath('//*[@class="ops-wrap-box"]')
    for b in bls:
        print(b.text)


 




    # time.sleep(2)
    # xuhao=browser.find_elements_by_xpath('//*[@class="list-item-content border-box"]')
    # for i in xuhao:
    #     info=i.find_element_by_xpath('.//*[@class="num"]').text
    #     content=i.find_element_by_xpath('.//div[2]/div/div/div[1]')
    #     t=i.find_element_by_xpath('.//*[@class="time"]')
    #     try:
    #         username=i.find_element_by_xpath('.//div[' + info + ']/div[1]/div[2]/span[2]').text
    #         u=i.find_element_by_xpath('.//div[2]/div/div/div[2]/div[1]/span[2]').text
           
    #         # i.find_element_by_xpath('.//*[@class="ops-wrap-box"]').click()
    #     except:
    #         username='22'
    #         u='33'

            
    #     print(info,content.text,username,t.text,u)
    #     print('-'*100)
       







login()

getcontent('黄牛')

# /html/body/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[1]

# /html/body/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div/div
# /html/body/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/span[2]
# /html/body/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/span[3]
# /html/body/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/

# /html/body/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div

# /html/body/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]


# /html/body/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]
# /html/body/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]

# /html/body/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[10]/div/div/div[2]/div/div/div[2]/div[1]/span[2]