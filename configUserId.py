import os
import yaml

filePath = "./config/userId.yaml"
sampleFilePath = "./config/userId.yaml"

if os.path.exists(filePath):
    with open(filePath, "r") as file:
        yaml_content = file.read()
else:
    with open(sampleFilePath, "r") as file:
        yaml_content = file.read()

yaml_data = yaml.safe_load(yaml_content)

# TODO

for platform in yaml_data:
    print("当前平台：" + platform["platform"])

    id_list = platform["id_list"]

    while True:
        user_input = input("请输入用户ID（输入'q'退出）: ")

        if user_input.lower() == "q":
            break

        input_data = {"userID": user_input}

        id_list.append(input_data)

    platform["id_list"] = id_list

yaml_content = yaml.dump(yaml_data)

with open(filePath, "w") as file:
    file.write(yaml_content)
