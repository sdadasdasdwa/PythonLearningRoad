import requests
import re

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
    

def save_to_csv():
    pass


def main():
    url = "https://www.dytt8899.com/"
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    }
    
    html = fetch_html(url,headers)
    
    # 存储热门电影栏目每条网页网址
    adresses = []
    adresses.extend(parse_html(html))
    print(adresses)
    
    save_to_csv()

if __name__ == "__main__":
    main()