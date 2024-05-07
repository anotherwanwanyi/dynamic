from request.basic import basicRequest
from request.utils import getBiliJsonContent

def returnContent(url, payload, headers):
    content = basicRequest(url, payload, headers)
    return getBiliJsonContent(content)


def getBilibiliUpDynamic(upID, cookie):
    """
    input: upID cookie
    output: JSON Item or None
    """
    url = "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space"
    payload = { "host_mid": upID,
                "platform": "web",
                "features": "itemOpusStyle,listOnlyfans,opusBigCover,onlyfansVote" }
    headers = { "User-Agent": "",
                "Cookie": cookie }

    return returnContent(url, payload, headers)


def getBilibiliUserDynamic(uid, cookie=None):
    """
    input: uid cookie(Optional)
    output: JSON Item or None
    """
    url = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new"
    payload = { "uid": uid,
                "type_list": 268435455 }
    headers = { "User-Agent": "" }

    if cookie is not None:
        headers["Cookie"] = cookie

    return returnContent(url, payload, headers)
