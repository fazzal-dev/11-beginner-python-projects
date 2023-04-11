import schedule
import requests
import time


def send_message():
    resp = requests.post('http://textbelt.com/text', {
        'phone': '+92(320)5489211',
        'message': 'Hey, this message is being sent through a python automation program',
        'key': 'textbelt'})
    print(resp.json())


schedule.every(1).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
