import json

def getBiliJsonContent(content):
    """
    input: content
    output: JSON Item or None
    """
    if content is not None:
        data = json.loads(content)
        if data["code"] != 0:
            print(f"Code {data["code"]} found, returning None")
            return None

        data = json.dumps(data, indent=4, ensure_ascii=False)
        return data
    else:
        return
