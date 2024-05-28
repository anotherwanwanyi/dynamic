import requests

def checkMethod(method):
    match method:
        case 'get':
            return requests.get
        case 'post':
            return requests.post
        case _:
            raise Exception("Undefined Request Method")

def basicRequest(method, url, payload, headers):
    """
    input: method url payload headers
    output: Response body or None
    """

    method = checkMethod(method)

    response = method(url=url, params=payload, headers=headers)

    if response.status_code == 200:
        return response.content

    else:
        print("Request failed with status code:", response.status_code)
        print("Body: ", response.content)
        return
