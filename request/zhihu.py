from request.basic import tryRequest
from request.utils import callback, dumpJson, getSignedHeader

def getZhihuPeopleActivities(id):
    """
    input: uid cookie(Optional)
    output: JSON Str or None
    """
    apiPath = f'/api/v3/moments/{id}/activities?limit=7&desktop=true'
    signedHeaders = getSignedHeader(apiPath)

    url = f"https://www.zhihu.com{apiPath}"

    response = tryRequest(callback=callback(f"zhihu people {id}"), method='get', url=url, headers=signedHeaders)

    if response is None:
        return

    # print(response.text)

    return dumpJson(response.json())
