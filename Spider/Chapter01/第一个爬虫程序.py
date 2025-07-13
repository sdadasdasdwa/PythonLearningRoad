from urllib.request import urlopen

# 爬虫百度

# 设置请求地址,发送请求
url = "https://www.baidu.com"
response = urlopen(url)

# 读取响应内容：打印出的内容大概是百度首页的 HTML 源码
# b'...' 表示这是 字节串（bytes 类型)
# 输出内容可能包含 Unicode 编码的中文，如 \u767e\u5ea6 表示“百度”。
# 如果你想以正常字符串形式打印内容，可以加上 .decode()

# print(response.read())
# print(response.read().decode())

with open("result.html", "w", encoding="utf-8") as f:
    f.write(response.read().decode())

print("over!")