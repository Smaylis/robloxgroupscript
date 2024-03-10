import requests
import time
groupId = 5574524
cursor = ''
limit = 100
sortOrder = 'Desc'
count = 0
file = open(r"SPECIFY THE FILE NAME HERE", "w")
user_req = requests.get(f"https://groups.roblox.com/v1/groups/{groupId}/users?limit={limit}&sortOrder={sortOrder}")
user_data = user_req.json()
print(user_data)
def users():
    for i in range(100):
        file.write(user_data["data"][i]["user"]["username"] + '\n')
        print(user_data["data"][i]["user"]["username"] + '\n')
try:
    while user_data["nextPageCursor"] != None:
        users()

        user_req = requests.get(
            f"https://groups.roblox.com/v1/groups/{groupId}/users?limit={limit}&sortOrder={sortOrder}")
        cursor = user_data["nextPageCursor"]
except:
    print("An error has occured")
    time.sleep(5)