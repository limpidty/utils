# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import urllib


def get_method(url):
    # url = 'http://www.chinaacc.com/wangxiao/teacher/'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    responses = requests.get(url, header)
    encoding = responses.encoding
    responses = responses.text.decode(encoding).encode("utf-8")
    html = BeautifulSoup(responses, 'html5lib')
    print html


def post_method(url):
    # url = 'http://www.chinaacc.com/wangxiao/teacher/'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    responses = requests.get(url, header)
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
