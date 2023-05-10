import requests
import json


def getBilibiliDynamic(upID):
    """
    input: upID
    output: JSON Item or None
    """
    url = "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space"
    payload = {"host_mid": upID}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        data = json.loads(response.content)
        data = json.dumps(data, indent=4, ensure_ascii=False)
        return data

    else:
        return
