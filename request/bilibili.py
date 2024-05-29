from request.basic import tryRequest
from request.utils import excepitonPrint, dumpJson

def getBiliJsonContent(response):
    """
    input: response
    output: JSON Str or None
    """
    data = response.json()
    if data["code"] != 0:
        print(f"Code {data["code"]} found, returning None")
        # print(data)
        return

    return dumpJson(data)


def getBiliContent(excepitonStr, url, payload, headers):
    response = tryRequest(func=excepitonPrint(excepitonStr), method='get', url=url, payload=payload, headers=headers)

    if response is None:
        return

    return getBiliJsonContent(response)

def getBilibiliUpDynamic(upID, cookie):
    """
    input: upID cookie
    output: JSON Str or None
    """
    url = "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space"
    payload = { "host_mid": upID,
                "platform": "web",
                "features": "itemOpusStyle,listOnlyfans,opusBigCover,onlyfansVote" }
    headers = { "Cookie": cookie }

    return getBiliContent(f"bilibili up {upID}", url, payload, headers)

def getBilibiliUserDynamic(uid, cookie=None):
    """
    input: uid cookie(Optional)
    output: JSON Str or None
    """
    url = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new"
    payload = { "uid": uid,
                "type_list": 268435455 }
    headers = {}

    if cookie is not None:
        headers["Cookie"] = cookie

    return getBiliContent(f"bilibili uid {uid}", url, payload, headers)
