import requests, json
from flask import Flask, request
from os import environ
from googlesearch import search
from bs4 import BeautifulSoup
import threading

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


def google(query):
    url = ""
    for x in search(query, tld="co.in", stop=1):
        url = str(x)

    try:
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        first_paragraph = soup.find('p')
        response = first_paragraph.text
    except:
        response = "No result - Sorry!"

    return response


def msgToChannel(userId, channelId, message):
    global TOKEN_IN_USE
    url = "https://slack.com/api/chat.postMessage"

    message = message.lower()
    idx = message.find('search')

    data1 = {}
    if idx != -1:
        query = message[idx+6::]
        result = google(query)

        data1 = {'channel': channelId,
            'text': f'{result}',
            'token': TOKEN_IN_USE}
    else:
        data1 = {'channel': channelId,
            'text': f'Hello <@{userId}>',
            'token': TOKEN_IN_USE}

    response = requests.post(url, data=data1)
    return response.status_code

@app.route('/listen', methods=['POST'])
def listen():
    try:
        incoming = request.get_json()
        channelId = incoming['event']['channel']
        userId = incoming['event']['user']
        msg = incoming['event']['text']
        threading.Thread(target=msgToChannel, args=(userId, channelId, msg,)).start()
            
    except:
        return json.dumps({'success': False}), 200, {'ContentType':'application/json'}
    return json.dumps({'success': True}), 200, {'ContentType':'application/json'}


if __name__ == '__main__':
    app.run(host='0.0.0.0')


