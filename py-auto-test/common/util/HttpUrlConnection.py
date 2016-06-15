# -*- coding:utf-8 -*-
import requests
from common.util.logger import logger


class HttpUrlConnection(object):
    '''
    :function __init__: 构造方法
    :function request: 不带cookie的请求
    :function request_with_cookies: 带cookie的请求
    '''

    # 处理预置数据
    def __init__(self, url=None, method="GET", parameters=None, cookies=None, headers={}, get_cookie_url=None,
                 get_cookie_method=None, get_cookie_request_data=None,
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
        self.__url = url
        self.__method = method
        self.__parameters = parameters
        self.__cookies = cookies
        self.__headers = headers
        self.__get_cookie_url = get_cookie_url
        self.__get_cookie_method = get_cookie_method
        self.__get_cookie_request_data = get_cookie_request_data
        self.__get_cookie_headers = get_cookie_request_data
        self.__session_object = requests.Session()
        if self.__get_cookie_method == "GET":
            response_oject_with_cookie = self.__session_object.get(url=self.__get_cookie_url,
                                                                   data=self.__get_cookie_request_data)
        if self.__get_cookie_method == "POST":
            response_oject_with_cookie = self.__session_object.post(url=self.__get_cookie_url,
                                                                    data=self.__get_cookie_request_data,
                                                                    headers=self.__get_cookie_headers)

    # 发送普通请求
    def request(self):
        try:
            if self.__method == "GET":
                response = requests.get(url=self.__url, params=self.__parameters)
            else:
                if self.__headers == {"Content-type": "application/json"}:
                    response = requests.post(url=self.__url, json=self.__parameters)
                else:
                    response = requests.post(url=self.__url, data=self.__parameters)
            return response
        except:
            logger.exception("发送普通请求错误:")

    # 使用requests发送带cookies的请求
    def request_with_cookies(self):
        try:
            if self.__method == "GET":
                response = self.__session_object.get(url=self.__url, params=self.__parameters)
            else:
                if self.__headers == {"Content-type": "application/json"}:
                    response = self.__session_object.post(url=self.__url, json=self.__parameters)
                else:
                    response = self.__session_object.post(url=self.__url, data=self.__parameters)
            return response
        except:
            logger.exception("带cookies请求错误：")

    # 获得带cookie对象
    def get_session_object(self):
        try:
            return self.__session_object
        except:
            logger.exception("获取带cookie对象错误")
