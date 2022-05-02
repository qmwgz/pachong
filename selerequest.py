
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

# listkwds=[
#     "炸了","烧了","卧轨","自杀","霸座","占座","杀人",
#     "咸猪手","骚扰","猥亵","流氓","色狼","示威","堵门",
#     "挡门","猥琐","变态","霸占","执勤","警员","站警",
#     "偷拍派出所 炸掉","占了","占位","强占","逃票","被占",
#     "爆炸","燃烧","打人","打架","打起来","烟雾报警","降速",
#     "起火","吸烟","抽烟","逼停","烟瘾","电子烟","抽了","吸了",
#     "一根烟","乞讨","要钱","聋哑","残疾","借钱","装聋","残障",
#     "残废","讨钱","讨要","骗钱","行乞","骗子","被骗","行骗","推销",
#     "诈捐","骗捐","诈骗","骗了","叫卖","没收","装聋作哑","态度恶劣",
#     "骗人","欺诈","揽客","拉客","骗局","丢了","被偷","掉了","偷了",
#     "丢失","遗失","要饭","骗我","位置","警察","小偷","火大","火气",
#     "神经病","安检","黑车","燃了","临停","临时停车","坏了","火灾",
#     "故障","晚点","闹事","炸火车","航拍","黄牛","吵架","二手烟",
#     "动不了","无人机","紧急停车","抹黑","顺走","精神病","死了",
#     "票贩子","蹲点","撞汽车","汽车撞","被坑","不动","不走","停了","停在"]
# datakwz=['列车','动车', '高铁', '火车站', '高铁站', '车站', '动车站', 
# '快铁站', '北站', '南站','东站' ,'西站' ,'铁路', '复兴号' ,'和谐号',
#  '铁轨', '车厢', '站台', '出站口', '候车厅', '候车室', '车站派出所' ]

def readkwd(file):
    with open(file,'r',encoding='utf-8') as f:
        res=f.read()
        kwdlist=res.split(' ')[:-1]
        return kwdlist

listkwds=readkwd('kwd2.txt')
datakwz=readkwd('keword1.txt')
print(listkwds)
print(datakwz)

l=set()
s=requests.Session()

# 第一层关键词搜索
def getdata(kwz):
    sj=datetime.datetime.now()-datetime.timedelta(minutes=5)
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
    print(json.loads(res.text)['data']['total'])
    for i in json.loads(res.text)['data']['records']:
        xinxi=[]
        timeStamp = int(i['warningTime'])
        timeArray = time.localtime(timeStamp/1000)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        for k in listkwds:
            if k in i['summary']:
                xinxi.append('标题:'+ i['title'] + '\n')
                xinxi.append('摘要:'+ i['summary'] + '\n')
                xinxi.append('链接:'+i['url'] + '\n')
                xinxi.append('作者:'+i['author'] + '\n')
                xinxi.append('时间:'+ otherStyleTime + '\n')
                xinxi.append('平台:'+ i['webName'] + '\n')
        
        l.add(''.join(xinxi))
        print(''.join(xinxi))
    
    return l

# while 1:
#     for d in datakwz:
#         data=getdata(d)
#         d=getcontent(data)
#         print(d)

#     time.sleep(20)
#     print('---'*100)
# for d in datakwz:
#     data=getdata(d)
#     d=getcontent(data)
    # print(d)

