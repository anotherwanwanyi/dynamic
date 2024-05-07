import request.bilibili as bilibili

def process(uid, cookie, data_list):
    if cookie is None:
        output_data = bilibili.getBilibiliUserDynamic(uid)
    else:
        output_data = bilibili.getBilibiliUserDynamic(uid, cookie)

    if output_data is None:
        print("Bilibili的uid信息获取失败")
    else:
        with open("./cache/bilibili/uid.json", "w") as file:
            file.write(output_data)


    for row in data_list:
        userID = row["user_id"]
        output_data = bilibili.getBilibiliUpDynamic(userID, cookie)

        if output_data is None:
            print(f"Bilibili的用户{userID}信息获取失败")
            continue

        with open(f"./cache/bilibili/{userID}.json", "w") as file:
            file.write(output_data)
