# sends the same message every x seconds

import requests, time
data = {"content": "Bot made by @clafan (you forgot to input a message smarty)"}
head = {
'Authorization': 'your key'
}
while True:
    r = requests.post('https://discord.com/api/v9/channels/CHANEL ID HERE/messages', data=data, headers=head) #make sure to put your channel id
    time.sleep(601)