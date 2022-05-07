import uiautomation as auto
import time
from uiautomation.uiautomation import Bitmap


def sendworks(sendyun,works):
    wechatWindow = auto.WindowControl(searchDepth=1,className='WeChatMainWndForPC',Name='微信')
    # wechatWindow.SetTopmost(True)
    wechatWindow.SetActive() 
    button = wechatWindow.ButtonControl(Name='通讯录')
    button.Click()
    search = wechatWindow.EditControl(Name='搜索')
    search.Click()
    search.GetParentControl().GetChildren()[1].SendKeys(sendyun)
    searResult = wechatWindow.ListControl(Name='搜索结果').GetChildren()
    for sear in searResult:
        # print(sear.Name)
        if sear.Name == sendyun:
            sear.Click()
            break
    session = wechatWindow.ListControl(Name='会话')
    wechatWindow.ButtonControl(Name=sendyun)

    button =wechatWindow.ButtonControl(Name='聊天信息')

    wechatWindow.EditControl(Name='输入').SendKeys(works)
    wechatWindow.EditControl(Name='输入').SendKeys('{Ctrl}v')

    
    sendBtn = wechatWindow.ButtonControl(Name='sendBtn')
    sendBtn.Click()



def send_img(sendyun,works):
    wechatWindow = auto.WindowControl(searchDepth=1,className='WeChatMainWndForPC',Name='微信')
    # wechatWindow.SetTopmost(True)
    wechatWindow.SetActive() 
    button = wechatWindow.ButtonControl(Name='通讯录')
    button.Click()
    search = wechatWindow.EditControl(Name='搜索')
    search.Click()
    search.GetParentControl().GetChildren()[1].SendKeys(sendyun)
    searResult = wechatWindow.ListControl(Name='搜索结果').GetChildren()
    for sear in searResult:
        # print(sear.Name)
        if sear.Name == sendyun:
            sear.Click()
            break
    session = wechatWindow.ListControl(Name='会话')
    wechatWindow.ButtonControl(Name=sendyun)

    button =wechatWindow.ButtonControl(Name='聊天信息')

    # wechatWindow.EditControl(Name='输入').SendKeys(works)
    auto.SetClipboardBitmap(Bitmap.FromFile(works))
    wechatWindow.EditControl(Name='输入').SendKeys('{Ctrl}v')

    sendBtn = wechatWindow.ButtonControl(Name='sendBtn')
    sendBtn.Click()
   
    

if __name__=='__main__':
    cs='''
    成都局西昌处甘洛所
    标题：揭露西安火车站北广场地下停车场黑保安，指挥私家车远离接人位置，让黑车守在旅客出口，威胁恐吓暴力驱逐私家车#西安火车站
    摘要：揭露西安火车站北广场地下停车场黑保安，指挥私家车远离接人位置，让黑车守在旅客出口，威胁恐吓暴力驱逐私家车#西安火车站 西安火车站北广场地下黑保安，辱骂威胁恐吓过往旅客，黑车司机保护伞
    链接：https://www.iesdouyin.com/share/video/7094482239517510949/?schema_type=37
    时间：2022-05-06 12:54:36
    来源：抖音
    作者：桃子
    属性：敏感
    涉及关键词：火车站,黑车,暴力,威胁
    '''
    data=cs.replace("\n", "{ENTER}")

    sendworks('文件传输助手',data)
