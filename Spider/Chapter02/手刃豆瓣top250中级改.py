import requests
import random
import time
import re
import csv

class DoubanSpider:
    def __init__(self):
        self.base_url = "https://movie.douban.com/top250?start={start}"
        self.headers_pool = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
            "(KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
            # 你可以自己加更多User-Agent
        ]
        self.proxies_pool = [
            "http://123.123.123.123:8080",
            "http://111.111.111.111:3128",
            # 你需要准备有效代理IP，格式"http://IP:PORT"
            # 注意免费代理不稳定，建议用自己的代理池或付费代理
        ]

    def get_proxy(self):
        if not self.proxies_pool:
            return None  # 没有代理时返回None
        return {"http": random.choice(self.proxies_pool), "https": random.choice(self.proxies_pool)}

    def get_headers(self):
        return {"User-Agent": random.choice(self.headers_pool)}

    def fetch_page(self, start):
        url = self.base_url.format(start=start)
        headers = self.get_headers()
        proxy = self.get_proxy()
        try:
            # response = requests.get(url, headers=headers, proxies=proxy, timeout=10) 代理池还未配置好
            response = requests.get(url, headers=headers, timeout=10)
            print(f"[INFO] 正在爬取: {url}")
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"请求失败: {e}，start={start}, proxy={proxy}")
            return None

    def parse(self, html):
        pattern = re.compile(
            r'<li>.*?<div class="item">.*?<span class="title">(?P<moviename>.*?)</span>.*?<p>.*?<br>(?P<movieyear>.*?)&nbsp.*?class="rating_num" property="v:average">(?P<moviestar>.*?)</span>.*?<p class="quote">.*?<span>(?P<moviequote>.*?)</span>', 
            re.S
        )
        return pattern.finditer(html)

    def save_to_csv(self, data_list, filename):
        with open(filename, mode="w", newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(["电影名", "年份", "评分", "短评"])  # 表头
            for data in data_list:
                writer.writerow(data)

    def run(self, pages=4):
        all_data = []
        for i in range(pages):
            start = i * 25
            html = self.fetch_page(start)
            if not html:
                print(f"跳过第{i+1}页数据")
                continue
            results = self.parse(html)
            for it in results:
                dic = it.groupdict()
                dic['movieyear'] = dic['movieyear'].strip()
                data_row = list(dic.values())
                all_data.append(data_row)
            print(f"[INFO] 累计获取 {len(all_data)} 条")
            # 防止请求太快，降低被封风险
            delay = random.uniform(1.5, 3.5)
            print(f"[INFO] 等待 {delay:.2f} 秒后继续爬取...")
            time.sleep(delay)
        self.save_to_csv(all_data, "./Spider/Chapter02/douban_top250_中级.csv")
        print("爬取完成，数据已保存到 ./Spider/Chapter02/douban_top250_中级.csv")

if __name__ == "__main__":
    spider = DoubanSpider()
    spider.run(pages=4)
