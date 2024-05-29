import requests

def checkMethod(method):
    match method:
        case 'get':
            return requests.get
        case 'post':
            return requests.post
        case _:
            raise Exception("Undefined Request Method")

def basicRequest(method, url, payload={}, headers={}):
    """
    input: method url payload headers
    output: Response
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
        **headers
    }

    method = checkMethod(method)

    response = method(url=url, params=payload, headers=headers)

    response.raise_for_status()

    return response

def tryRequest(callback, method, url, payload={}, headers={}):
    """
    input: callback method url payload headers
    output: Response | None
    """
    try:
        response = basicRequest(method, url, payload, headers)
        return response
    except Exception as e:
        callback(e)
        return
