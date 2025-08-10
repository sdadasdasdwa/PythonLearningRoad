import requests
import re
import csv
import time
import random

def fetch_page(url, headers):
    """获取网页源码"""
    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()  # 检查请求是否成功
        return res.text
    except requests.RequestException as e:
        print(f"[ERROR] 请求失败: {e}")
        return ""

def parse_movies(html):
    """用正则解析电影信息"""
    pattern = re.compile(
        r'<li>.*?<div class="item">.*?<span class="title">(?P<moviename>.*?)'
        r'</span>.*?<p>.*?<br>(?P<movieyear>.*?)&nbsp.*?'
        r'class="rating_num" property="v:average">(?P<moviestar>.*?)</span>.*?'
        r'<p class="quote">.*?<span>(?P<moviequote>.*?)</span>',
        re.S
    )
    results = []
    for it in pattern.finditer(html):
        dic = it.groupdict()
        dic['movieyear'] = dic['movieyear'].strip()
        results.append(dic)
    return results

def save_to_csv(filename, rows):
    """保存数据到 CSV 文件"""
    with open(filename, mode="w", newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(["电影名", "年份", "评分", "短评"])  # 表头
        for row in rows:
            writer.writerow(row.values())

def main():
    base_url = "https://movie.douban.com/top250?start={}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

    all_movies = []
    for start in range(0, 101, 25):  # start=0,25,50,75,100 共 5 页
        url = base_url.format(start)
        print(f"[INFO] 正在爬取: {url}")
        html = fetch_page(url, headers)
        if html:
            movies = parse_movies(html)
            all_movies.extend(movies)
            print(f"[INFO] 本页获取 {len(movies)} 条数据，累计 {len(all_movies)} 条")
        else:
            print(f"[WARN] 第 {start//25 + 1} 页获取失败")
        
        # 防反爬，随机等待
        delay = random.uniform(1, 3)
        print(f"[INFO] 等待 {delay:.2f} 秒后继续爬取...")
        time.sleep(delay)

    save_to_csv("./Spider/Chapter02/doubanMovie.csv", all_movies)
    print("[SUCCESS] 数据已保存到 doubanMovie.csv")

if __name__ == "__main__":
    main()