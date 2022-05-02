
import requests
import json
import time
import datetime

header={
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
    'Token': 'NTYwMDhhNmI5MjE0NDU0Yzg4NWY4NDkzMzQ3N2ZjMDVfMTAzODM3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'

}
url='https://yqms.istarshine.com/v4/api/search/all'


listkwds=[]
datakwz=['黄牛','霸坐','动车吸烟','高铁吸烟']
s=requests.Session()

# 第一层关键词搜索
def getdata(kwz):
    sj=datetime.datetime.now()-datetime.timedelta(minutes=10)
    begintime=str(datetime.datetime.timestamp(sj)*1000).split('.')[0]
    endtime=datetime.datetime.now()
    endtime=str(datetime.datetime.timestamp(endtime)*1000).split('.')[0]
    data={
        # "timeRange":"3",
        'beginTime':begintime,
        'endTime':endtime,
        "attitude":[],
        "typeList":["content","title","comment"],
        "mediaType":[],
        "isOcr":"",
        "weiboType":[],
        "weiboAttestType":[],
        "weiboState":"",
        "customCondition":[],
        "keywords":kwz,
        "pageSize":30,
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
    l=[]
    for i in json.loads(res.text)['data']['records']:
        xinxi=[]
        timeStamp = int(i['warningTime'])
        timeArray = time.localtime(timeStamp/1000)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        xinxi.append('标题:'+ i['title'] + '\n')
        xinxi.append('摘要:'+ i['summary'] + '\n')
        xinxi.append('链接:'+i['url'] + '\n')
        xinxi.append('作者:'+i['author'] + '\n')
        xinxi.append('时间:'+ otherStyleTime + '\n')
        xinxi.append('平台:'+ i['webName'] + '\n')
        l.append(xinxi)
       
    return l  


for d in datakwz:
    data=getdata(d)
    d=getcontent(data)
    print(d)

