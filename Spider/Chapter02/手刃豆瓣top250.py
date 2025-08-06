import re,requests

url = "https://movie.douban.com/top250"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

res =  requests.get(url=url,headers=headers)
page_content = res.text

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<moviename>.*?)'
                 r'</span>.*?<p>.*?<br>(?P<movieyear>.*?)&nbsp.*?'
                 r'class="rating_num" property="v:average">(?P<moviestar>.*?)</span>.*?'
                 r'<p class="quote">.*?<span>(?P<moviequote>.*?)</span>',re.S)
result = obj.finditer(page_content)  
for it in result:
    print(it.group("moviename"), end=" ")
    print(it.group("movieyear").strip(), end=" ")
    print(it.group("moviestar").strip(), end=" ")
    print(it.group("moviequote").strip())
    