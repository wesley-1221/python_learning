# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月07日
"""
import urllib.request,urllib.error
import re
from bs4 import BeautifulSoup
import xlwt
import sqlite3

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    #savepath = "豆瓣电影Top250.xls"
    dbpath = "movie.db"
    #3.保存数据
    #saveData(datalist,savepath)
    saveData2DB(datalist,dbpath)

    #askURL("https://movie.douban.com/top250?start=")

#影片详情链接
findLink = re.compile(r'<a href="(.*?)">')  #创建正则表达式对象，表示规则
#影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)#re.S让换行符包含在字符中
#片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):       #调用获取页面信息的函数，10次
        url = baseurl + str(i*25)
        html = askURL(url)      #保存获取到的网页源码

        #2、逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):    #查找符合要求的字符串，形成列表
            data = []  #保存一部电影的所有信息
            item = str(item)

            #影片详情的链接
            link = re.findall(findLink,item)[0]   #re库用来通过正则表达式查找指定的字符串
            data.append(link)   #添加链接

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)        #添加图片

            titles = re.findall(findTitle,item)            #片名可能只有一个中文名
            if (len(titles)==2):
                ctitle = titles[0]            #添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/","")      #去掉无关符号
                data.append(otitle)     #外国名，
            else:
                data.append(titles[0])
                data.append(' ')    #外国名留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)            #添加评分

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)  #添加评价人数

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")    #去掉句号
                data.append(inq)        #添加概述
            else:
                data.append(" ")  #留空

            bd = re.findall(findBd,item)[0]           #影片相关内容
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)    #去掉<br/>
            bd = re.sub('/'," ",bd)  #替换/
            data.append(bd.strip())   #去掉前后的空格

            datalist.append(data)     #将处理好的一部电影信息收入datalist
    return datalist

#得到指定的一个URL的网页内容
def askURL(url):
    head = {      #模拟浏览器的头部消息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
               #用户代理表示搞事豆瓣服务器，是什么类型的机器，浏览器
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

# #保存数据
# def saveData(datalist,savepath):
#    print("save.....")
#    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
#    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  # 创建工作表
#    col = ('电影详情链接','图片链接','电影中文名','影片外国名','评分','评价数','概识','相关信息')
#    for i in range(0, 8):
#        sheet.write(0, i, col[i])  # 列名
#    for i in range(0, 250):
#        print("第%d条" % (i+1))
#        data = datalist[i]
#        for j in range(0, 8):
#            sheet.write(i+1, j, data[j])  # 数据
#
#
#    book.save(savepath)    #保存



def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
            sql = '''
                insert into movie250 (
                info_link,pic_link,cname,ename,score,rated,instroduction,info) 
                values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie250 
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric ,
        rated numeric ,
        instroduction text,
        info text
        )

    '''  # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
    #init_db("movietext.db")
    print("爬取完毕！")