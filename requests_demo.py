# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import urllib


def get_method(url):
    # url = 'http://www.baidu.com'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    responses = requests.get(url, header)
    encoding = responses.encoding
    responses = responses.text.decode(encoding).encode("utf-8")
    html = BeautifulSoup(responses, 'html5lib')
    print html


def post_method(url):
    # url = 'http://www.baidu.com'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    params={"name":ccc}
    responses = requests.get(url,data=params,headers=headers)
    # 获取网页编码
    encoding = responses.encoding
    # 将编码转utf-8
    responses = responses.text.decode(encoding).encode("utf-8")
    html = BeautifulSoup(responses, 'html5lib')
    print html

    
def get_with_cookie():
    cookies = {'JSESSIONID': 'abclb5hQxbM3Zd-ZT1Ghw', 'Hm_lpvt_694e61985b4752f4e7a0e5223195635f': '1519954736',
                   'Hm_lvt_694e61985b4752f4e7a0e5223195635f': '1519895511'}
    response = requests.get("http://baidu.com", data=params,cookies=cookies)
    # 获取网页编码
    encoding = responses.encoding
    # 将编码转utf-8
    responses = responses.text.decode(encoding).encode("utf-8")
    html = BeautifulSoup(responses, 'html5lib')
    print html

# url解码,解析unicode编码过的url
def percent_decode(string):
    url = urllib.unquote(string)
    return url
