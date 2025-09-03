import requests
import bs4

class BSFour:
    
    def __init__(self):
        self.base_url = "http://wap.xinfadi.com.cn/getPriceData.html"
        self.headers = {
                "Host": "wap.xinfadi.com.cn",
                "Origin": "http://wap.xinfadi.com.cn",
                "Referer": "http://wap.xinfadi.com.cn/priceDetail.html",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36"
        }
        self.params = {
            "current":"",
            "pubDateStartTime":"2023/01/01",
            "pubDateEndTime":"",
            "prodPcatid":"",
            "prodCatid":"",
            "prodName":""
        }

    def fetch_html(self):
        url = self.base_url
        headers = self.headers
        params =  self.params
        res = requests.post(url, data=params, headers=headers, timeout=10)
        res.raise_for_status()  # 检查请求是否成功
        print(res.text)
    
    def parse_html(self):
        pass
    
    
if __name__ == "__main__":
    object = BSFour ()
    object.fetch_html()