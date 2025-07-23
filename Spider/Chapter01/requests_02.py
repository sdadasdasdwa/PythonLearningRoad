import requests

url = 'https://fanyi.baidu.com/sug'
query = input("请输入查询单词: ")
dat = {
    "kw" : query
}

resp = requests.post(url,data=dat)
print(resp.json()) # 将服务器返回的内容直接处理成json

resp.close()

