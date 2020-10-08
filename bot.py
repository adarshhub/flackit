import requests, json
from flask import Flask, request
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
            'text': 'Hehehe....',
            'token': TOKEN_IN_USE}
    response = requests.post(url, data=data1)
    if response.status_code == 200
        return json.dumps({'success': True}), 200, {'ContentType':'application/json'}
    else:
        return json.dumps({'success': False}), 200, {'ContentType':'application/json'}

@app.route('/listen', methods=['POST'])
def listen():
    incoming = request.get_json()
    channel = incoming['channel']
    msgToChannel(channel)
    return json.dumps({'success': True}), 200, {'ContentType':'application/json'}


if __name__ == '__main__':
    app.run(host='0.0.0.0')


