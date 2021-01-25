# -*-coding:utf-8-*-

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Expect
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver import FirefoxOptions

# 云麓里销售页面
url = 'http://www.fangdi.com.cn/new_house/new_house_detail.html?project_id=069c616823d32fc8'


def load_driver_path():
    platform = sys.platform

    if platform.__contains__('darwin'):
        print('System is OsX')
        return 'driver/mac_geckodriver'
    if platform.__contains__('linux'):
        print('System is linux')
        return 'driver/linux_geckodriver'


def dos_can():
    global proxy, server, browser
    try:

        # 启动浏览器
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver_path = load_driver_path()
        browser = webdriver.Firefox(options=options, executable_path=driver_path)

        # 开始获取内容
        browser.get(url)

        Wait(browser, 100).until(
            Expect.presence_of_element_located((By.ID, "salesInformation"))
        )
        navBar = browser.find_element_by_id('salesInformation')
        print(str(navBar.text))
        print('-----------------------')
        insist = navBar.find_elements_by_class_name('new_house_sale_list')

        csList = insist[0].find_elements_by_class_name('text_ellipsis')
        print(csList[0].text)

        csList1 = insist[1].find_elements_by_class_name('text_ellipsis')
        print(csList1[0].text)

        csList1 = insist[3].find_elements_by_class_name('text_ellipsis')
        print(csList1[0].text)

        csList1 = insist[5].find_elements_by_class_name('text_ellipsis')
        print(csList1[0].text)

        print('----------------------')
        salespeed = browser.find_element_by_id('saleSpeed')
        print(salespeed.text)


    finally:
        browser.close()
        browser.quit()
    return ""


if __name__ == "__main__":
    dos_can()
