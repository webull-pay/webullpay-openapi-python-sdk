# Copyright 2025 Webullpay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8

"""
This file borrowed some of its methods from a  modified fork of the
https://github.com/aliyun/aliyun-openapi-python-sdk/blob/master/aliyun-python-sdk-core/aliyunsdkcore/http/http_response.py
which was part of Alibaba Group.
"""

import os
import logging
from webullpaysdkcore.vendored.requests import Request, Session
from webullpaysdkcore.http.request import Request as HttpRequest
from webullpaysdkcore.http import protocol_type as PT
from webullpaysdkcore.vendored.requests import status_codes


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
ch = logging.StreamHandler()
logger.addHandler(ch)

DEFAULT_CONNECT_TIMEOUT = 5

ENV_DEBUG = "WEBULL_PAY_API_DEBUG"
DEBUG_VAL = "sdk"

class Response(HttpRequest):
    def __init__(
        self,
        host="",
        url="/",
        method="GET",
        headers={},
        protocol=PT.HTTP,
        content=None,
        port=None,
        key_file=None,
        cert_file=None,
        read_timeout=None,
        connect_timeout=None,
        verify=None):
        HttpRequest.__init__(
            self,
            host=host,
            url=url,
            method=method,
            headers=headers)
        self.__ssl_enable = False
        if protocol is PT.HTTPS:
            self.__ssl_enable = True
        self.__key_file = key_file
        self.__cert_file = cert_file
        self.__port = port
        self.__connection = None
        self.__read_timeout = read_timeout
        self.__connect_timeout = connect_timeout
        self.__verify = verify
        self.set_body(content)

    def set_ssl_enable(self, enable):
        self.__ssl_enable = enable

    def get_ssl_enabled(self):
        return self.__ssl_enable

    @staticmethod
    def prepare_http_debug(request, symbol):
        base = ''
        for key, value in request.headers.items():
            base += '\n%s %s : %s' % (symbol, key, value)
        return base

    def do_http_debug(self, request, response):
        # logger the request
        request_base = '\n> %s %s' % (self.get_method().upper(), self.get_url())
        request_base += '\n> Host : %s' % self.get_host()
        logger.debug(request_base + self.prepare_http_debug(request, '>'))

        # logger the response
        response_base = '\n< %s %s' % (
            response.status_code, status_codes._codes.get(response.status_code)[0].upper())
        logger.debug(response_base + self.prepare_http_debug(response, '<'))

        logger.debug("\n<\n" + response.text)

    def get_verify_value(self):
        if self.__verify is not None:
            return self.__verify
        return os.environ.get('WEBULL_PAY_API_CA_BUNDLE', True)

    def get_response_object(self):
        with Session() as s:
            current_protocol = 'https://' if self.get_ssl_enabled() else 'http://'
            host = self.get_host()
            if host.startswith('https://') or\
                    not host.startswith('https://') and current_protocol == 'https://':
                port = ':%s' % self.__port if self.__port != 80 and self.__port != 443 else ''
            else:
                port = ':%s' % self.__port if self.__port != 80 else ''

            if host.startswith('http://') or host.startswith('https://'):
                url = host + port + self.get_url()
            else:
                url = current_protocol + host + port + self.get_url()

            req = Request(method=self.get_method(), url=url,
                          data=self.get_body(),
                          headers=self.get_headers(),
                          )
            prepped = s.prepare_request(req)

            proxy_https = os.environ.get('HTTPS_PROXY') or os.environ.get(
                'https_proxy')
            proxy_http = os.environ.get(
                'HTTP_PROXY') or os.environ.get('http_proxy')

            proxies = {
                "http": proxy_http,
                "https": proxy_https,
            }

            response = s.send(prepped, proxies=proxies,
                              timeout=(self.__connect_timeout, self.__read_timeout),
                              allow_redirects=False, verify=self.get_verify_value(), cert=None)

            http_debug = os.environ.get(ENV_DEBUG)

            if http_debug is not None and http_debug.lower() == DEBUG_VAL:
                # http debug information
                self.do_http_debug(prepped, response)

            return response.status_code, response.headers, response.content, response