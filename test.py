# import time

# from selenium import webdriver

# if __name__ == '__main__':

#     driver = webdriver.Chrome()
#     driver.get("https://yqms.istarshine.com/v4/subject")

#     cl=driver.find_element_by_xpath('')
#     print(cl)


#     # time.sleep(1)
#     #
#     # driver.find_element_by_id('kw').send_keys('Python测试开发社区')
#     #
#     # time.sleep(1)
#     #
#     # driver.find_element_by_id('su').click()
#     #
#     # time.sleep(5)
#     #
#     # driver.quit()
#     #
#     # print('Done!')
#     #
#     # time.sleep(1)


a=['a','b','c']
b='的链接发来的飞机垃圾的身份垃圾地方b'
flaglist=[]
for i in a:
    if i in b:
        print(1)
        flaglist.append(1)
    else:
        flaglist.append(0)
if 1 in flaglist:
    print(222)