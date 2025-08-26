import requests
import re
import time
import random
import csv

def fetch_html(url, headers):
    """获取网页源码"""
    try:
        res = requests.get(url, headers=headers, timeout=10)   # verify=False去掉安全验证
        res.encoding = "gbk"
        res.raise_for_status()  # 检查请求是否成功
        return res.text
    except requests.RequestException as e:
        print(f"[ERROR] 请求失败: {e}")
        return ""

def parse_html(html):
    """用正则解析电影信息"""
    pattern = re.compile(r'2025必看热片.*?<ul>(?P<hotmovie>.*?)</ul>',re.S)
    hotmovie = ''
    for it in pattern.finditer(html):
        hotmovie = it.group("hotmovie")
    patternhref = re.compile(r"href='(?P<href>.*?)'",re.S)
    results = []    # 将提取的网页网址部分放在这里
    for it in patternhref.finditer(hotmovie):
        results.append(it.group("href"))
    return results

def parse_children_html(children_html):
    """"用正则解析子页面信息"""
    pattern = re.compile(r'◎片　　名　(?P<moviename>.*?)<br />'
                         r'.*?上映日期　(?P<moviedate>.*?)<br />'
                         r'.*?<td style="WORD-WRAP: break-word".*?<a href="(?P<movieadress>.*?)">',re.S)
    results = []
    for it in pattern.finditer(children_html):
        dic = it.groupdict()
        results.append(dic)
    return results

def save_to_csv(filename, rows):
    
    with open(filename, mode="w", newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(["电影名", "年份", "网址"])  # 表头
        for row in rows:
            writer.writerow(row.values())

def main():
    url = "https://www.dytt8899.com/"
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    }
    
    html = fetch_html(url,headers)
    
    # 存储热门电影栏目每条网页网址
    adresses = []
    adresses.extend(parse_html(html))
    # print(adresses)
    
    # 对分网页地址进行逐条获取源代码
    all_movies = []
    for adress in adresses:
        child_href = url + adress.strip("/")
        child_html = fetch_html(child_href,headers)
        if child_html:
            movieInfo = parse_children_html(child_html)
            all_movies.extend(movieInfo)
            print(f"[INFO] 子网页 {child_href} 获取成功")
        else:
            print(f"[WARN] 子网页 {child_href} 获取失败")
        # 防反爬，随机等待
        delay = random.uniform(1, 3)
        print(f"[INFO] 等待 {delay:.2f} 秒后继续爬取...")
        time.sleep(delay)
        
    save_to_csv('./Spider/Chapter02/MovieHeaven.csv',all_movies)

if __name__ == "__main__":
    main()