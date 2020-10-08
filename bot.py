import requests, json
from flask import Flask, request
from os import environ

app = Flask(__name__)

# MY_TOKEN = environ['MY_TOKEN']
# BOT_TOKEN = environ['BOT_TOKEN']
MY_TOKEN = 'xoxp-1419442495793-1403724219829-1405794636342-a85c786b064214c7ba726ec5ea57bcdb'
BOT_TOKEN = 'xoxb-1419442495793-1413075542628-mKalOzt7rrWxCw8fwuatkSlB'

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

@app.route('/listen', methods=['POST'])
def listen():
    incoming = request.get_json()
    return json.dumps({'challenge': incoming['challenge']}), 200, {'ContentType':'application/json'}


if __name__ == '__main__':
    app.run()


