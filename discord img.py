# same as discord spam.py except it also can send a image
import requests
import time

while True:
    header = {
    'Authorization': "Your key here",
    }


    files = {
    "file" : ("file path", open("file path", 'rb'))
    }

# Optional message
    payload = {
    "content": "made by @clafan"
    }

    channel_id = "your channel id"


    r = requests.post(f"https://discord.com/api/v9/channels/channel id hereeeeeee/messages", data=payload, headers=header, files=files)
    time.sleep(601)