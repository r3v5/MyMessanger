import apiai, json
import time
from datetime import datetime
from flask import Flask, request, abort

#Мой чат-бот.Для его создания я применил ИИ и написал скрипт
#Oн создан ради общения и веселья
def textMessage(message):
    request = apiai.ApiAI('7f01246612e64e3f89264a85a965ddd3').text_request()
    request.lang = 'ru'
    request.session_id = 'Lookgram_13OT'
    request.query = message
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    input(responseJson['result']['fulfillment']['speech'])
    return responseJson['result']['action']

print('Напишите сообщение и отправьте"exit"')
message = input()
action = None
while message != 'exit':
    textMessage(message)
    message(input)


app = Flask(__name__)
db = [
    {
        'name': 'Jack',
        'text': 'Привет всем!',
        'time': time.time()
    }, {
        'name': 'Mary',
        'text': 'Привет, Jack',
        'time': time.time()
    }
]


@app.route("/")
def hello():
    return "Lookgram"


@app.route("/status")
def status():
    dt = datetime.now()

    from collections import defaultdict
    d = defaultdict(int)
    for message in db:
        d[message['text']] += 1

    return{
        'status': True,
        'name': "Lookgram",
        'time': dt.strftime('%Y/%m/%d %H:%M'),
    }


@app.route("/send", methods=['POST'])
def send_message():
    if not isinstance(request.json, dict):
     return abort(400)

     name = request.json['name']
     text = request.json['text']

     if not (isinstance(name, str)
            and isinstance(text, str)
            and name
            and text):
        return abort(400)

     new_message = {
         'name': name,
         'text': text,
         'time': time.time()
    }
    db.append(new_message)

    return {'ok': True}


@app.route("/messages")
def get_messages():
    try:
        after = float(request.args.get('after', 0))
    except ValueError:
        return abort(400)

    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return {'messages': messages}


app.run()

