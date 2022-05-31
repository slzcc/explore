from selenium import webdriver
from time import sleep
import json

driver = webdriver.Chrome()

driver.get("https://baidu.com")

print(driver.title)

sleep(3)

driver.back()

driver.quit()

urls = []

for log in driver.get_log('performance'):
     if 'message' not in log:
        continue
     log_entry = json.loads(log['message'])
     try:
        #该处过滤了data:开头的base64编码引用和document页面链接
        if "data:" not in log_entry['message']['params']['request']['url'] and 'Document' not in log_entry['message']['params']['type']:
            urls.append(log_entry['message']['params']['request']['url'])
     except Exception as e:
        pass

print(urls)

