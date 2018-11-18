import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['userinfo']:

        NAME = p['name']
        EMAIL = p['email']
        PHONE = p['phone']
        MESSAGE = p['message']
        LINK_TO_MONITOR = p['url']
        INTERVAL = 120  # How many seconds to wait before checking for new properties
