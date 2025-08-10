import re,requests
import csv

url = "https://movie.douban.com/top250?start=0"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

# 获取静态网页源代码
res =  requests.get(url=url,headers=headers)
page_content = res.text

# 关闭请求连接
res.close()

# 预加载正则表达式
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<moviename>.*?)'
                 r'</span>.*?<p>.*?<br>(?P<movieyear>.*?)&nbsp.*?'
                 r'class="rating_num" property="v:average">(?P<moviestar>.*?)</span>.*?'
                 r'<p class="quote">.*?<span>(?P<moviequote>.*?)</span>',re.S)

# 查找返回迭代器
result = obj.finditer(page_content)  

# 创造一个CSV写入对象，用来把数据写入到一个已经打开的文件中
f = open("./Spider/Chapter02/doubanMovie.csv",mode="w",newline='',encoding='utf-8-sig')
csvwritter = csv.writer(f)

# 遍历寻找
for it in result:
    # 创造字典准备将数据写入csv
    # .groupdict() 把所有命名组的内容取出来
    dic = it.groupdict()
    dic['movieyear'] = dic['movieyear'].strip()
    csvwritter.writerow(dic.values())
    # print(it.group("moviename"), end=" ")
    # print(it.group("movieyear").strip(), end=" ")
    # print(it.group("moviestar").strip(), end=" ")
    # print(it.group("moviequote").strip())
f.close()