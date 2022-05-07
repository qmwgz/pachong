
import requests
import json
import time
import datetime
from selenium import webdriver


# from wechatautosend import sendworks,send_img
from fasong import send_msg,selectSessionFromName



header={
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
    'Token': 'NTYwMDhhNmI5MjE0NDU0Yzg4NWY4NDkzMzQ3N2ZjMDVfMTAzODM3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'

}
url='https://yqms.istarshine.com/v4/api/search/all'
def readkwd(file):
    with open(file,'r',encoding='utf-8') as f:
        res=f.read()
        kwdlist=res.split(' ')
        return kwdlist




l=[]
s=requests.Session()

# 第一层关键词搜索
def getdata(kwz,sj):
    sj=datetime.datetime.now()-datetime.timedelta(minutes=sj)
    begintime=str(datetime.datetime.timestamp(sj)*1000).split('.')[0]
    endtimesj=datetime.datetime.now()
    endtime=str(datetime.datetime.timestamp(endtimesj)*1000).split('.')[0]
    # print('开始时间:%s结束时间%s'%(str(sj),str(endtimesj)))
    data={
        # "timeRange":"3",
        'beginTime':begintime,
        'endTime':endtime,
        "attitude":['2'],
        "typeList":["content","title","comment"],
        "mediaType":[],
        "isOcr":"",
        "weiboType":['1'],
        "weiboAttestType":['1'],
        "weiboState":"",
        "customCondition":[],
        "keywords":kwz,
        "pageSize":90,
        "secondKeywords":"",
        "secondTypeList":["content","title","comment"],
        "searchMode":"2",
        "infoSource":"",
        "isCoutSearchNum":"",
        "sites":[],
        "orderBy":1,
        "isRepeat":"0",
        "offset":0,
        "limitNum":100,
        "timestamp":1651483989893
    }

    return json.dumps(data)



def getcontent(data):
    res=s.post(url=url,data=data,headers=header)
    resdata=json.loads(res.text)['data']['records']
    print('返回总共%s条，进行下一步过滤'%json.loads(res.text)['data']['total'])
    return resdata



def fenxi(datajson):
    for i in datajson:       
        timeStamp = int(i['warningTime'])
        timeArray = time.localtime(timeStamp/1000)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        for k in listkwds:
            if k in i['summary'] and len(i['summary'])<60:
                flagls=[]
                for pcc in paichuci:
                    if pcc in i['summary']:
                        flagls.append(1)
                    else:
                        flagls.append(0)
                        # print(pcc+'没有在信息中')
                # 已经排除了排除词
                if 1 not in flagls:
                    xinxi=[]
                    xinxi.append('成都局西昌处\n')
                    xinxi.append('标题:'+ i['title'] + '\n')
                    xinxi.append('摘要:'+ i['summary'] + '\n')
                    xinxi.append('链接:'+i['url'] + '\n')
                    xinxi.append('作者:'+i['author'] + '\n')
                    xinxi.append('时间:'+ otherStyleTime + '\n')
                    xinxi.append('平台:'+ i['webName'] + '\n')
                    zfc=''.join(xinxi)
                    if zfc not in l:
                        if len(xinxi) != 0 : 
                            print('第二个：'+ k)
                            print(zfc)
                            # sendworks('文件传输助手',zfc.replace("\n", "{ENTER}"))
                            selectSessionFromName('文件传输助手')
                            send_msg(zfc)
                            browser = webdriver.Chrome()
                            browser.get(i['url'])
                            # browser.maximize_window()
                            time.sleep(10)
                            browser.save_screenshot('baidu.png')
                            send_msg('baidu.png', msg_type=0)
                            browser.close()
                            time.sleep(5)
                    l.append(zfc)



# 第一层关键词搜索
def initdata(k1,k2,sj):
    sj=datetime.datetime.now()-datetime.timedelta(minutes=sj)
    begintime=str(datetime.datetime.timestamp(sj)*1000).split('.')[0]
    endtimesj=datetime.datetime.now()
    endtime=str(datetime.datetime.timestamp(endtimesj)*1000).split('.')[0]
    # print('开始时间:%s结束时间%s'%(str(sj),str(endtimesj)))
    data={
        # "timeRange":"3",
        'beginTime':begintime,
        'endTime':endtime,
        "attitude":['2'],
        "typeList":["content","title","comment"],
        "mediaType":[],
        "isOcr":"",
        "weiboType":['1'],
        "weiboAttestType":['1'],
        "weiboState":"",
        "customCondition":[],
        "keywords":k1,
        "pageSize":90,
        "secondKeywords":k2,
        "secondTypeList":["content","title","comment"],
        "searchMode":"2",
        "infoSource":"",
        "isCoutSearchNum":"",
        "sites":[],
        "orderBy":1,
        "isRepeat":"0",
        "offset":0,
        "limitNum":100,
        "timestamp":1651483989893
    }

    return json.dumps(data)

def parsedata(datajson):
    for i in datajson:       
        timeStamp = int(i['warningTime'])
        timeArray = time.localtime(timeStamp/1000)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
       
        flagls=[]
        for pcc in paichuci:
            if pcc in i['summary']:
                flagls.append(1)
            else:
                flagls.append(0)
                # print(pcc+'没有在信息中')
        # 已经排除了排除词
        if 1 not in flagls:
            xinxi=[]
            xinxi.append('成都局西昌处\n')
            xinxi.append('标题:'+ i['title'] + '\n')
            xinxi.append('摘要:'+ i['summary'] + '\n')
            xinxi.append('链接:'+i['url'] + '\n')
            xinxi.append('作者:'+i['author'] + '\n')
            xinxi.append('时间:'+ otherStyleTime + '\n')
            xinxi.append('平台:'+ i['webName'] + '\n')
            zfc=''.join(xinxi)
            if zfc not in l:
                if len(xinxi) != 0 : 
                    print(zfc)
                    # sendworks('文件传输助手',zfc.replace("\n", "{ENTER}"))
                    selectSessionFromName('文件传输助手')
                    send_msg(zfc)
                    browser = webdriver.Chrome()
                    browser.get(i['url'])
                    # browser.maximize_window()
                    time.sleep(10)
                    browser.save_screenshot('baidu.png')
                    send_msg('baidu.png', msg_type=0)
                    browser.close()
                    time.sleep(5)
            l.append(zfc)



while 1:
    listkwds=[i.replace('\n','') for i in readkwd('kwd2.txt')[:-1]]
    kw1=[i.replace('\n','') for i in readkwd('kwd1.txt')[:-1]]
    paichuci=[i.replace('\n','') for i in readkwd('pcc.txt')]
    tm=readkwd('sj.txt')[0]
    print('排除词：',paichuci)
    print(listkwds)
    # print(datakwz)
    print(listkwds)
    num=0
    for first in kw1:
        try:
            num+=1
            print('第%s个关键词：%s,查询时间为当前往前推%s分钟'%(str(num),first,tm))
            firstdata=getdata(first,int(tm))
            d=getcontent(firstdata)           
            fenxi(d)
        except:
            continue
        time.sleep(1)
    print('休息20秒,继续奋斗'+'---'*10)
    time.sleep(20)

    # for k1 in kw1:
    #     for k2 in listkwds:
    #         tishi='第一层关键词：%s,第二个关键词：%s,时间为%s分钟内'%(k1,k2,tm)
    #         print(tishi)
    #         requestdata=initdata(k1,k2,int(tm))
    #         resdata=getcontent(requestdata)
    #         parsedata(resdata)
    #         time.sleep(1)
   
            
    

    

