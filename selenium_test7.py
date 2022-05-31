from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # 和下面WebDriverWait一起用的
from selenium.webdriver.support.wait import WebDriverWait


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
    # 处理 content 乱码问题
    content = str(etree.tostring(content, encoding='utf-8', method='html'), 'utf-8')
    # 提取 content 中所有图片的地址
    script = tree.xpath('//script/@src')

    data = {
        "script": script
    }

    print(data)


if __name__ == '__main__':
    url = "https://www.billance.com"
    result = get_news_content(url)
    print(result)