import requests, json
from flask import Flask
from os import environ

app = Flask(__name__)

MY_TOKEN = environ['MY_TOKEN']
BOT_TOKEN = environ['BOT_TOKEN']

TOKEN_IN_USE = BOT_TOKEN

@app.route('/msgToUser/<userId>', methods= ['GET','POST'])
def msgToUser(userId):
    global TOKEN_IN_USE
    url = "https://slack.com/api/conversations.open"
    data1 = {'token': TOKEN_IN_USE,
            'users': userId}
    response = requests.post(url, data=data1 )
    print(response.json())
    user_id = response.json()['channel']['id']


    url = "https://slack.com/api/chat.postMessage"
    data1 = {'token': TOKEN_IN_USE,
            'channel': user_id,
            'text': "Using Flask Python"}
    requests.post(url, data=data1 )

@app.route('/msgToChannel/<channelId>', methods= ['GET','POST'])
def msgToChannel(channelId):
    global TOKEN_IN_USE
    url = "https://slack.com/api/chat.postMessage"
    data1 = {'channel': channelId,
            'text': 'From Flask Python',
            'token': TOKEN_IN_USE}
    response = requests.post(url, data=data1)
    print(response)
    return response.json()


if __name__ == '__main__':
    app.run(debug=True)


