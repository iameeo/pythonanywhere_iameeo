import requests

def slackMessage(text):
    text = text
    url = 'https://hooks.slack.com/services/TMGE25VGT/B05GZRKLRU1/'
    url = url + '78IBMFJojDSDx6ON7wEXiOe7'
    payload = { "text" : text }

    requests.post(url, json=payload)

siteList = ['https://iameeo.pythonanywhere.com']

for i in siteList:
    try:
        response = requests.get(i)
        if response.status_code != 200 :
            slackMessage(str(i) + " : " + str(response.status_code))
    except:
        slackMessage("error : " + str(i))
        continue