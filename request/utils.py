import json
import hashlib
from lib.utils import memoize
from request.basic import basicRequest
from request.lib.g_encrypt import encrypt

def dumpJson(data):
    return json.dumps(data, indent=4, ensure_ascii=False)

def excepitonPrint(route: str):
    def exception(e: Exception):
        print(f"Error when fetching {route}: ", e)
    return exception

def getCookieValue(cookies, cookieName):
    for key, value in cookies.iteritems():
        # print(f"{key}: {value}")
        if key == cookieName:
            return value
    return None

@memoize
def getDC0():
    with basicRequest(method="post", url="https://www.zhihu.com/udid") as response:
        cookies = response.cookies
        dc0 = getCookieValue(cookies, 'd_c0')
        if not dc0:
            raise Exception('Failed to extract `d_c0` from cookies')
        # print("Get DC0: ", dc0)
        return dc0

def getSignedHeader(api_path: str):
    dc0 = getDC0()

    # 参考自RSSHub中zhihu路由相关的utils中get_signed_header实现
    # 计算 x-zse-96，参考 https://github.com/srx-2000/spider_collection/issues/18
    xzse93 = '101_3_3.0'
    f = f"{xzse93}+{api_path}+{dc0}"
    xzse96 = '2.0_' + encrypt(hashlib.md5(f.encode('utf-8')).hexdigest())

    return {
        'cookie': f"d_c0={dc0}",
        'x-zse-96': xzse96,
        'x-app-za': 'OS=Web',
        'x-zse-93': xzse93,
    }
