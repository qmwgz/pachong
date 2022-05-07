import time
import uiautomation as auto
from uiautomation.uiautomation import Bitmap

wechatWindow = auto.WindowControl(
    searchDepth=1, Name="微信", ClassName='WeChatMainWndForPC')
# wechatWindow.SetActive()
search = wechatWindow.EditControl(Name='搜索')
edit = wechatWindow.EditControl(Name='输入')
messages = wechatWindow.ListControl(Name='消息')
sendButton = wechatWindow.ButtonControl(Name='sendBtn')


def selectSessionFromName(name, wait_time=0.1):
    wechatWindow.SetActive()
    search.Click()
    auto.SetClipboardText(name)
    edit.SendKeys('{Ctrl}v')
    # 等待微信索引搜索跟上
    time.sleep(wait_time)
    search.SendKeys("{Enter}")


def send_msg(content, msg_type=1):
    wechatWindow.SetActive()
    if msg_type:
        auto.SetClipboardText(content)
    else:
        auto.SetClipboardBitmap(Bitmap.FromFile(content))
    edit.SendKeys('{Ctrl}v')
    sendButton.Click()

if __name__=='__main__':
    name = "文件传输助手"
    selectSessionFromName(name)
    content = "小小明你好，收到这条消息说明你的程序已经成功---来自自动化测试程序"
    send_msg(content)
    content = r"baidu.png"
    send_msg(content, msg_type=0)