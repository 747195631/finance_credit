# coding=utf-8
###########################################
# File: HttpUrlConnection_old.py
# Desc: http接口工具类
# Author: zhangyufeng
# History: 2015/11/15 zhangyufeng 新建
###########################################
import sys

import simplejson

if sys.version_info[0] == 2:
    import httplib as http_client
    import urllib as urllib_parse
    import urllib2 as urllib_request
    import cookielib as ckjar

if sys.version_info[0] == 3:
    from http import client as http_client
    from http import cookiejar as ckjar
    import urllib.parse as urllib_parse
    import urllib.request as urllib_request

from common.util.logger import logger


class HttpUrlConnection(object):
    '''
    :function __init__: 构造方法
    :function request: 不带cookie的请求
    :function request_with_cookies: 带cookie的请求
    :function get_host: 提供外部host数据
    :function get_path: 提供外部path数据
    :function get_parameters_urlencode_deal: 提供外部经过ulrencode处理后的数据
    '''

    # 处理预置数据
    def __init__(self, url=None, method="GET", parameters=None, cookie=None, headers={}, get_cookie_url=None,
                 get_cookie_request_data=None,
                 get_cookie_headers=[('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]):
        '''
        :param url: 请求使用的url，由于发送cookie的请求方法可以单独传url故此参数非必填。使用request方法请求时必填。
        :param method: 请求的方法
        :param parameters: 请求的参数
        :param cookie: cookie
        :param headers: 请求头
        :param get_cookie_url: 获取cookie的url,如果调用request_with_cookies时此参数必须传
        :param get_cookie_request_data: 获取cookie时需要传的参数
        :param get_cookie_headers: 获取cookie时需要加的请求头
        '''
        try:
            # 解析url
            if url is None:
                self.__url = None
            else:
                try:
                    if type(url) == bytes:
                        self.__url = url.decode("utf-8")
                    if type(url) == str:
                        self.__url = url
                except:
                    self.__url = url
                logger.debug(self.__url)
                scheme, rest = urllib_parse.splittype(self.__url)
                # 拆分域名和路径
                logger.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                self.__host_absolutely, self.__path = urllib_parse.splithost(rest)
                host_list = self.__host_absolutely.split(":")
                if len(host_list) == 1:
                    self.__host = host_list[0]
                    self.__port = 80
                elif len(host_list) == 2:
                    self.__host = host_list[0]
                    self.__port = host_list[1]
            # 对所传参数进行处理
            self.__method = method
            self.__data = parameters
            self.__cookie = cookie
            if parameters != None:
                self.__parameters_urlencode_deal = urllib_parse.urlencode(parameters)
            else:
                self.__parameters_urlencode_deal = ""
            self.__jdata = simplejson.dumps(parameters, ensure_ascii=False)
            self.__headers = headers
            self.__opener = None
            self.__get_cookie_request_data = None
            if get_cookie_url is not None:
                cj = ckjar.CookieJar()
                self.__opener = urllib_request.build_opener(urllib_request.HTTPCookieProcessor(cj))
                self.__opener.addheaders = get_cookie_headers
                if get_cookie_request_data is not None:
                    self.__get_cookie_request_data = urllib_parse.urlencode(get_cookie_request_data).encode("utf-8")
                self.__opener.open(get_cookie_url, self.__get_cookie_request_data)
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 发送普通请求,要求完全满足http协议规则
    def request(self):
        try:
            conn = http_client.HTTPConnection(self.__host, self.__port)
            if self.__method == "GET":
                self.path = self.__path + self.__parameters_urlencode_deal
                conn.request(self.__method, self.__path)
            if self.__method == "POST":
                if self.__headers == {"Content-type": "application/json"}:
                    conn.request(self.__method, self.__path, self.__jdata, self.__headers)
                if self.__headers == {"Content-type": "application/x-www-form-urlencoded"}:
                    conn.request(self.__method, self.__path, self.__data, self.__headers)

            response = conn.getresponse()
            result_origin = response.read()
            try:
                result = result_origin.decode("gb2312").encode("utf8")
            except:
                result = result_origin
            return result
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 使用urllib.request发送带cookie的请求
    def request_with_cookies(self, url=None, parameters=None):
        '''
        :param url: 请求的url
        :param parameters: 请求的参数
        :return: 返回响应对象

        e.g.
            post_data = {'username': 'admin@suolong', 'password': '123456'}
            loginUrl = "http://test2.ishop-city.com/reconciliation/admin/user/login.json"
            testUrl = 'http://test2.ishop-city.com/reconciliation/repayCheck/gethuizong.json'
            http_object = HttpUrlConnection(get_cookie_url=loginUrl, get_cookie_request_data=post_data)
            result=http_object.request_with_cookies(testUrl)
            print(result.readlines())
        '''
        try:
            # 实例化HttpUrlConnection时如果没传url则将request_with_cookies的url赋给self.__url
            if self.__url is None:
                self.__url = url
            # 实例化HttpUrlConnection时如果没传parameters则将request_with_cookies的parameters赋给self.__url
            if self.__data is None:
                self.__data = parameters
            # 已带cookie的对象必须存在且请求的链接url必传
            if self.__opener is not None and self.__url is not None:
                html = self.__opener.open(self.__url, self.__data)
                return html
            else:
                return 0
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 提供外部host数据    
    def get_host(self):
        try:
            return self.__host
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 提供外部path数据
    def get_path(self):
        try:
            return self.__path
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 提供外部经过ulrencode处理后的数据
    def get_parameters_urlencode_deal(self):
        try:
            return self.__parameters_urlencode_deal
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 提供可以直接使用的带cookie的opener
    def get_opener(self):
        try:
            return self.__opener
        except:
            logger.exception(u"捕获到错误如下:")
