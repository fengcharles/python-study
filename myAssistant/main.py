import platform
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
        return 'driver/mac_geckodriver'
    if platform.__contains__('linux'):
        return 'driver/linux_geckodriver'

def dos_can():
    global proxy, server, browser
    try:

        # 获取当前操作系统名称


        # 启动代理
        # server = Server('/Users/von/Documents/exapps/browsermob-proxy-2.1.4/bin/browsermob-proxy')
        # server.start()
        # proxy = server.create_proxy()
        # print('proxy', proxy.proxy)

        # 启动浏览器
        profile = webdriver.FirefoxProfile()
        # profile.set_preference('network.proxy.type', 1)
        # profile.set_preference('network.proxy.http', '127.0.0.1')
        # profile.set_preference('network.proxy.http_port', proxy.port)
        profile.update_preferences()
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver_path = load_driver_path()
        print(driver_path)
        browser = webdriver.Firefox(options=options, executable_path=driver_path)

        # proxy.new_har(options={
        #     'captureContent': True,
        #     'captureHeaders': True
        # })

        browser.get(url)
        # time.sleep(10)

        Wait(browser, 100).until(
            Expect.presence_of_element_located((By.ID, "salesInformation"))
        )
        navBar = browser.find_element_by_id('salesInformation')

        nslist = navBar.find_elements_by_class_name('new_house_sale_list')

        csList = nslist[0].find_elements_by_class_name('text_ellipsis')
        print(csList[0].text)

        csList1 = nslist[1].find_elements_by_class_name('text_ellipsis')
        print(csList1[0].text)

        csList1 = nslist[3].find_elements_by_class_name('text_ellipsis')
        print(csList1[0].text)

        csList1 = nslist[5].find_elements_by_class_name('text_ellipsis')
        print(csList1[0].text)
    finally:
        # proxy.close()
        # server.stop()
        browser.close()
        browser.quit()
    return ""


if __name__ == "__main__":
    dos_can()
