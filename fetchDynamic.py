import json
import request.bilibili as bilibili

file_path = "./config/userId.json"

with open(file_path, "r") as file:
    json_data = file.read()

data = json.loads(json_data)

for platform in data:
    platformName = platform["platform"]
    data_list = platform["id_list"]
    for row in data_list:
        userID = row["userID"]
        match platformName:
            case "bilibili":
                output_data = bilibili.getBilibiliDynamic(userID)
            case "zhihu":
                output_data = None
                print("WIP")
            case _:
                output_data = None
                print("WIP")

        if output_data is None:
            print(f"{platformName}的用户{userID}信息获取失败")
            continue

        # 请先创建对应文件夹，如 cache/bilibili
        with open(f"./cache/{platformName}/{userID}.json", "w") as file:
            file.write(output_data)
