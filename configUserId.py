import json

# 注意将config文件夹中的sample重命名为userId.json
file_path = "./config/userId.json"

with open(file_path, "r") as file:
    json_data = file.read()

data = json.loads(json_data)

for platform in data:
    print("当前平台：" + platform["platform"])

    input_list = platform["input_list"]

    while True:
        user_input = input("请输入用户ID（输入'q'退出）: ")

        if user_input.lower() == "q":
            break

        input_data = {"userID": user_input}

        input_list.append(input_data)

    platform["input_list"] = input_list

json_data = json.dumps(data, indent=4, ensure_ascii=False)

with open(file_path, "w") as file:
    file.write(json_data)
