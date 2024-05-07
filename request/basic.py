import requests

def basicRequest(url, payload, headers):
    """
    input: url payload headers
    output: Response body or None
    """

    response = requests.get(url, params=payload, headers=headers)

    if response.status_code == 200:
        return response.content

    else:
        print("Request failed with status code:", response.status_code)
        print("Body: ", response.content)
        return
