import re

# findall: 匹配字符串中所有符合正则的内容，返回列表
list = re.findall("\d+","我的电话是：10123，我男朋友电话是：123123")
print(list)

# finditer: 匹配字符串中所有的内容，返回的是迭代器，比返回列表快
it = re.finditer("\d+","我的电话是：10123，我男朋友电话是：123123")
for i in it:
    print(i.group())
    
# search,找到一个结果就返回，返回的是match对象，拿数据要.group()
s = re.search("\d+","我的电话是：10123，我男朋友电话是：123123")
print(s.group())

# match,默认从头开始匹配，与^相当
s = re.match("\d+","10123，我男朋友电话是：123123")
print(s.group())

# 预加载正则表达式
obj = re.compile("\d+")
ret = obj.findall("10123，我男朋友电话是：123123")
print(ret)

# 例子
s = """
<div class='kaisa'><span id='1'>凯撒</span></div>
<div class='sakura'><span id='2'>路明非</span></div>
<div class='chuzihang'><span id='3'>楚子航</span></div>
<div class='turtle'><span id='4'>象龟</span></div>
"""
obj = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>",re.S)  # re.S代表让.匹配换行符
result = obj.finditer(s)  
for it in result:
    print(it.group())