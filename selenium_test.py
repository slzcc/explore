import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import unittest

 
chrome_options = Options()
chrome_options.add_argument('--log-level=1')  # 忽略错误
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument('--ignore-certificate-errors')  # 忽略证书错误
chrome_options.add_argument('--headless')  # 开启无头模式
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_experimental_option('w3c', False)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1920x1080")  # I added this

caps = {
    'browserName': 'chrome',
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

 
class BaiduTestCase(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Chrome(desired_capabilities=caps, chrome_options=chrome_options)
    self.addCleanup(self.browser.quit)
  def testPageTitle(self):
    self.browser.get('http://www.baidu.com')
    self.assertIn('百度', self.browser.title)
if __name__ == '__main__':
  unittest.main(verbosity=2)