from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # 和下面WebDriverWait一起用的
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urljoin
from urllib.parse import urlparse

import requests
import re
import logging

with open('conf/domain.list') as f:
    urls = f.read()

logging.basicConfig(level=logging.INFO,
                    filename='/dev/stdout',
                    filemode='a',
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )

REQUEST_PORT = 443

def html_selenium_firefox(url):
    """
    根据 url 使用 selenium 获取网页源码
    :param url: url
    :return: 网页源码
    """
    opt = webdriver.FirefoxOptions()
    # 设置无界面
    opt.add_argument("--headless")
    # 禁用 gpu
    opt.add_argument('--disable-gpu')
    # 指定 geckodirver 的安装路径，如果配置了环境变量则不需指定
    executable_path = "/usr/local/bin/geckodriver"
    driver = webdriver.Firefox(executable_path=executable_path, options=opt)
    # 发送请求
    driver.get(url)
    # 显式等待：显式地等待某个元素被加载
    # wait = WebDriverWait(driver, 20)
    # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'article-content')))
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, 'span')))
    # 获取网页源码
    html = driver.page_source
    # 关闭浏览器释放资源
    driver.quit()
    return html


def get_news_content(url):
    html = html_selenium_firefox(url)
    tree = etree.HTML(html)
    # 提取 content 中所有图片的地址
    script = tree.xpath('//script/@src')
    images = tree.xpath('//img/@src')
    link = tree.xpath('//link/@href')

    data = {
        "script": script,
        "link": link
    }

    return data

def urlPathCompensation(base_url, request_url):

    addr = request_url
    # 判断是否存在 /configs 开头文件
    matchObj = re.match(r'^/configs', addr, re.M|re.I)
    if matchObj:
        base = 'https://{}'.format(urlparse(base_url).hostname)
        addr = urljoin(base, request_url)
        return addr

    matchObj = re.match(r'^/static', addr, re.M|re.I)
    if matchObj:
        base = 'https://{}'.format(urlparse(base_url).hostname)
        addr = urljoin(base, request_url)
        return addr

    matchObj = re.match(r'^//', addr, re.M|re.I)
    if matchObj:
        addr = urljoin('https://', addr)
        return addr

    return request_url

if __name__ == '__main__':
    for url in urls.split('\n'):
        result = get_news_content(url)
        print(result)
        for data_type in result:
            for url_data in result[data_type]:
                print(url_data,urlPathCompensation(url, url_data))
                if url_data:
                    session = requests.get(urlPathCompensation(url, url_data))
                    print(session.status_code)
