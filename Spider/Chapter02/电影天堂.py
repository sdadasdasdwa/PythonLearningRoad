import requests

url = "https://www.dytt8899.com/"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

resp = requests.get(url=url,headers=headers,verify=False)   # verify=False去掉安全验证
resp.encoding = "gbk"
print(resp.text)