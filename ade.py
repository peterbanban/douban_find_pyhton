# _*_ coding:utf-8 _*_
#GVIM 添加汉字注释

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#以上定义字符集 使得代码可用汉字
#爬取豆瓣电影信息

import json
import urllib2
import urllib
from bs4 import BeautifulSoup
tags=[]
url='https://movie.douban.com/j/search_tags?type=movie'
request=urllib2.Request(url)
response=urllib2.urlopen(request,timeout=20)
result=json.loads(response.read())
tags=result['tags']

movies=[]
for tag in tags:
    limit=0
    print tag
    while(1):
        url='https://movie.douban.com/j/search_subjects?type=movie&tag='+unicode(tag)+'&sort=recommend&page_limit=20&page_start='+str(limit)
        request1=urllib2.Request(url=url)
        response1=urllib2.urlopen(request1,timeout=60)
        result1=json.loads(response1.read())
        result1=result1['subjects']
        if len(result1)==0:
            break
        limit+=20
        for item in result1:
            movies.append(item)
       
    for x in range(0,len(movies)):
        item=movies[x]
        request=urllib2.Request(url=item['url'])
        response=urllib2.urlopen(request,timeout=20)
        result=response.read()
        html=BeautifulSoup(result,'lxml')
        title=html.select('h1')[0]
        title=title.get_text()
        print title.encode("GBK",'ignore')
    movies=[]


