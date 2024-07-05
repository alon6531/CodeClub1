import os
import requests
import json


def is_malicious(file_path):
    url = "https://www.virustotal.com/api/v3/files"

    files = {"file": open(str(file_path), "rb")}

    headers = {
        "accept": "application/json",
        "x-apikey": "e3cc230bd0d1b392b828bb5c277a540d88f131fa66285bae2291fd4bc44652e2"
    }

    response = requests.post(url, files=files, headers=headers)

    uid = json.loads(response.text)["data"]["id"]

    url = "https://www.virustotal.com/api/v3/analyses/" + uid

    response = requests.get(url, headers=headers)

    x = json.loads(response.text)['data']['attributes']['stats']['malicious']
    return True if x > 0 else False


def check_al(path, x):
    if os.path.exists(path):
        if os.path.isfile(path):
            print("checking: " + path)
            if is_malicious(path):
                print("virus! 😱: " + path)
                x += 1
                return x
        if os.path.isdir(path):
            for item in os.listdir(path):
                check_al(path + "\\" + item, x)
            return x


def check_all(path):
    print("you have: " + str(check_al(path, 0)) + " virus!")


check_all("E:\programming projects\AlonFly")