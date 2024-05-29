import yaml
import lib.fetcher.bilibili as bilibili
import lib.fetcher.zhihu as zhihu

file_path = "./config/userId.yaml"

with open(file_path, "r") as file:
    yaml_content = file.read()

yaml_data = yaml.safe_load(yaml_content)

for platform in yaml_data:
    platformName = platform["platform_name"]
    cookie = platform["cookie"]
    data_list = platform["users"]
    match platformName:
        case "bilibili":
            bilibili.process(platform["uid"], cookie, data_list)
        case "zhihu":
            zhihu.process(data_list)
        case _:
            print(f"{platformName}: WIP")

