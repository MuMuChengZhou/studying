'''
常见接口类型:
    http接口、RFC接口、web service接门、dubble接口、restful接口restful接口也是基于http协议。web service接口和dubble接口都是属于rfc接口。

    http接口: 同过http协议传输的接口，可以传输文本、表单数据、也可以传输ison类型数据或xml类型数据

    restful接口:是http接口的一种设计风格，将一切接口都视为资源，接口路径统一.

    rfc (远程方法调用) 接口: 主要应用于分布式系统。

    web service接口: 基于soap协议的一种rc实现方案。相对于http协议接口只传输文本请求或文本响应外,
    web service接口可以直接传输一个对象，并能够调用该对象的属性和方法，比http功能强大，但是效率低

    dubbo接口: 阿里开源的一种rfc远程服务调用方案。

http接口:
    http请求的组成:请求行、请求头、请求体
    请求行: url(接口地址)、http协议版本
    请求头: 包含服务器域名地址 (host) accept: 客户端接收哪些类型的信息
            accept lanquage:客户端接收的语言  cookie、 content-type: body编码格式
    请求体: 请求数据
http请求类型:
    get:向特定资源发起请求。
    post: 向指定资源提交数据处理请求(类似于增加数据)
    put: 向指定资源提交数据处理请求(类似于修改数据)
    delete: 请求服务器删除资源
    ead: 用于获取报文头，响应中没有具体内容。
    opions: 允许客户端查看服务器性能
'''

from pprint import pprint
import requests
'''
get请求示例：
'''
# # 参数放在URL里面
se = requests.session()
# url = 'https://www.baidu.com/s?wd=学习'
# resp1 = se.get(url)
# print(resp1.headers)             #获取请求头
# print(resp1.text)
# print(type(resp1.headers))
# print(resp1.cookies)             #获取cookies
# print(resp1.status_code)         #获取请求状态码
# print(resp1.raw)                 #获取原始响应体
# print(resp1.ok)                  #返回值为True或者False


# 参数不放在URL里面
url = 'https://www.baidu.com/'
param1 = {'wd':'学习'}
resp2 = se.get(url,params = param1)
print(resp2.text)
print(resp2.content)                            #去掉乱码影响
print(resp2.content.decode('utf-8'))            #返回结果进行utf-8处理
