import requests, json
from flask import Flask, redirect, request, session, jsonify

app = Flask(__name__)

# ved - U01BS2H2QVC
# api channel - C01BVMCRA21
MY_TOKEN = 'xoxp-1419442495793-1403724219829-1430726323008-cf3201578ab203af447820cda15d102e'
BOT_TOKEN = "xoxb-1419442495793-1413075542628-dQ8XrGmqaxn9iqnhF0fGcrj5"

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


