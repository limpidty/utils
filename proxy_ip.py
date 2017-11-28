# -*-coding:utf-8-*-
# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用

from bs4 import BeautifulSoup
import requests
import random
import time


# 获取代理ip池
def get_ip_list(target_url, my_headers):
    # 创建字典保存之前存储和当前抓取的ip
    ip_dic = {}
    # 读取之前录入的有效ip
    for ip_str in open("resources/ip_valid.txt", "rb").readlines():
        ip_str = ip_str.strip()
        if len(ip_str) > 0:
            ip_dic[ip_str] = 0
            # 有效ip池
    valid_file = open("resources/ip_valid.txt", "wb")
    html = requests.get(target_url, headers=my_headers)
    soup = BeautifulSoup(html.text, 'lxml')
    ips = soup.find_all('tr')
    # 遍历获取的ip
    for ip_index in xrange(0, len(ips)):
        ip_info = ips[ip_index]
        tds = ip_info.find_all('td')
        if len(tds) == 0:
            continue
        speed_div = tds[6].select("div.fast")
        connect_div = tds[7].select("div.fast")
        # 筛选连接速度和连接速度为fast的ip
        if len(speed_div) == 1 and len(connect_div) == 1:
            ip_str = tds[1].text + ':' + tds[2].text
            ip_str = ip_str.encode("utf-8")
            if ip_str not in ip_dic:
                ip_dic[ip_str] = 0
    for need_ip in ip_dic:
        if ip_is_valid(need_ip):
            valid_file.write(need_ip + "\n")
    valid_file.close()


# 验证代理ip是否可用
def ip_is_valid(test_ip):
    try:
        # 如果超时或无法访问则返回False
        requests.get('http://wenshu.court.gov.cn/', proxies={"http": "http://" + test_ip},
                     timeout=1)
        return True
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.ConnectionError:
        return False


def get_random_ip(ip_list):
    proxy_list = []
    for p_ip in ip_list:
        proxy_list.append('http://' + p_ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/{0}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    get_ip_list(url.format(str(2)), headers)
    # for i in xrange(1, 10):
    #     time.sleep(random.randint(0, 10))
        # get_ip_list(url, headers)
        # for i in open('resources/ip_valid.txt', 'rb').readlines():
        #     ip = i.strip()
        #     print ip_is_valid(ip)
        #     # proxies = get_random_ip(ip_list)
        #     # print(proxies)
        # print random.randint(0, 10)
