import time
import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import unittest


d = DesiredCapabilities.FIREFOX
d['loggingPrefs'] = { 'performance':'ALL' }
 
browser_options = Options()
# browser_options.add_argument('--log-level=1')  # 忽略错误
# browser_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# browser_options.add_argument('--ignore-certificate-errors')  # 忽略证书错误
# browser_options.add_argument('--headless')  # 开启无头模式
# browser_options.add_argument('--disable-gpu')
# browser_options.add_experimental_option('w3c', False)
# browser_options.add_argument('--headless')
# browser_options.add_argument('--disable-gpu')
# browser_options.add_argument('--no-sandbox')
# browser_options.add_argument("--start-maximized")
# browser_options.add_argument("--window-size=1920x1080")  # I added this

caps = {
    'browserName': 'Firefox',
    'loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
    },
    'goog:chromeOptions': {
        'perfLoggingPrefs': {
            'enableNetwork': True,
        },
        'w3c': False,
    },
}

 
# class BaiduTestCase(unittest.TestCase):
#   def setUp(self):
#     # self.browser = webdriver.Firefox(desired_capabilities=caps, options=chrome_options)
#     self.browser = webdriver.Firefox(executable_path="/Users/shilei/Downloads/geckodriver",desired_capabilities=d)
#     self.addCleanup(self.browser.quit)
#   def testPageTitle(self):
#     self.browser.get('http://www.baidu.com')
#     self.assertIn('百度', self.browser.title)
# if __name__ == '__main__':
#   unittest.main(verbosity=2)


browser = webdriver.Firefox(executable_path="/Users/shilei/Downloads/geckodriver",desired_capabilities=d)
browser.set_page_load_timeout(150)
browser.get("https://www.baidu.com")

print(dir(browser))

# print("log_types", browser.log_types())
# print(browser.get_log("browser"))


browser.back()

browser.quit()
