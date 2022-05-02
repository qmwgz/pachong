from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


class DySprider(object):

    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options = self.options)
        self.driver.get(self.url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10)

    def parseurl(self):
        self.driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(5)
        items = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        item_lists = []
        for item in items:
            title = item.find_element_by_xpath('./a/div[2]/div[1]/h3').text.strip()
            name = item.find_element_by_xpath('./a/div[2]/div[2]/h2').text.strip()
            commit = item.find_element_by_xpath('./a/div[2]/div[2]/span').text.strip()
            prourl = item.find_element_by_class_name("DyListCover-wrap")
            newurl = prourl.get_attribute('href')
            item_list = [title, name, commit, newurl]
            item_lists.append(item_list)
        return item_lists

    def WriteDate(self, item_lists):
        hr = ['title', 'name', 'commit', 'newurl']
        with open(r'斗鱼信息.csv', 'w', encoding='utf-8', newline='')as f:
            writer = csv.writer(f)
            writer.writerow(hr)
            writer.writerows(item_lists)

    def main(self):
        items_list = []
        while True:
            items_list += self.parseurl()
            self.WriteDate(items_list)
            if self.driver.page_source.find('class="dy-Pagination-disabled dy-Pagination-next"') == -1:
                self.driver.find_element_by_xpath('//*[@id="listAll"]/section[2]/div[2]/div/ul/li[9]/span').click()
                time.sleep(3)
            else:
                self.driver.quit()
                break


if __name__ == '__main__':
    douyu = DySprider()
    douyu.main()
