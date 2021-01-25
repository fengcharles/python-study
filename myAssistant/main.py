# -*-coding:utf-8-*-

import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Expect
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver import FirefoxOptions

# 云麓里销售页面
url = 'http://www.fangdi.com.cn/new_house/new_house_detail.html?project_id=069c616823d32fc8'
basemesgurl = 'https://sc.ftqq.com/'
sckey = 'SCU142685Tfd06f72db3371db1938bb69054c0bcef5fed785b32f38'
title = '云麓里销售情况'


def load_driver_path():
    platform = sys.platform

    if platform.__contains__('darwin'):
        print('System is OsX')
        return 'driver/mac_geckodriver'
    if platform.__contains__('linux'):
        print('System is linux')
        return 'driver/linux_geckodriver'


def dos_can():
    try:
        mesg = ''
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

        if len(insist) == 0:
            print('未抓取到数据')
            return

        csList = insist[0].find_elements_by_class_name('text_ellipsis')
        print(csList[0].text)
        mesg = mesg + csList[0].text + '\n'

        csList1 = insist[1].find_elements_by_class_name('text_ellipsis')
        print(csList1[0].text)
        mesg = mesg + csList1[0].text + '\n'

        csList2 = insist[3].find_elements_by_class_name('text_ellipsis')
        print(csList2[0].text)
        mesg = mesg + csList2[0].text + '\n'

        csList3 = insist[5].find_elements_by_class_name('text_ellipsis')
        print(csList3[0].text)
        mesg = mesg + csList3[0].text + '\n'
        print('----------------------')

        # 获取月销售情况
        salespeed = browser.find_element_by_id('saleSpeed')
        print(salespeed.text)

        # 发送消息
        sendmesg(mesg)

    finally:
        browser.close()
        browser.quit()
    return ""


def sendmesg(text):
    furl = basemesgurl + sckey + '.send' + '?text=' + title + '&desp=' + text
    print('通过Server酱发送消息链接:', furl)
    result = requests.get(url=furl)
    print('发送结果', result)


if __name__ == "__main__":
    dos_can()
