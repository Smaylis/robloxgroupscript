import requests
import time
groupId = 5574524
cursor = ''
limit = 10
sortOrder = 'Asc'
counter = 0
file = open(r'C:\Users\Covid_transmitter\Desktop\people.txt', 'w')
#file = open(r"SPECIFY THE FILE NAME HERE", "w")
user_req = requests.get(f"https://groups.roblox.com/v1/groups/{groupId}/users?limit={limit}&sortOrder={sortOrder}")
user_data = user_req.json()
print(user_data)
print(user_data["nextPageCursor"])
cursor = user_data["nextPageCursor"]
file.write("hallo")

ask = 'y'
for i in range(limit):
    #print(user_data['data'][i]['user']['username'])
    file.write(user_data['data'][i]['user']['username'] + '\n')
    print(user_data['data'][i]['user']['username'])
while True:
    try:
        user_req = requests.get(f'https://groups.roblox.com/v1/groups/{groupId}/users?limit={limit}&cursor={cursor}&sortOrder={sortOrder}')
        user_data = user_req.json()
        cursor = user_data["nextPageCursor"]
        
        for i in range(limit):
            #print(user_data['data'][i]['user']['username'])
            file.write(user_data['data'][i]['user']['username'] + '\n')
            print(user_data['data'][i]['user']['username'])

        counter += limit
        print(counter)
        
    except:
        print(user_data)
        ask = str(input("A bug occured, proceed? y/n"))
        if ask != 'y':
            exit()
file.close()
exit()
