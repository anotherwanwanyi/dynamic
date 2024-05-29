import request.zhihu as zhihu

def process(data_list):
    for row in data_list:
        userID = row["user_id"]
        output_data = zhihu.getZhihuPeopleActivities(userID)

        if output_data is None:
            print(f"zhihu的用户{userID}信息获取失败")
            continue

        with open(f"./cache/zhihu/{userID}.json", "w") as file:
            file.write(output_data)
