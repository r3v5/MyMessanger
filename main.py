import time
import datetime

message1 = {
    'name': 'Jack',
    'text': 'Привет всем!',
    'time': time.time()
}
message2 = {
    'name': 'Mary',
    'text': 'Привет, Jack',
    'time': time.time()
}

db = [message1, message2]


def send_message(name, text):
    new_message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    db.append(new_message)


def get_messages(after=0):
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return messages


def print_messages(messages):
    for message in messages:
        beauty_time = datetime.datetime.fromtimestamp(message['time'])
        beauty_time = beauty_time.strftime('%Y/%m/%d %H:%M')
        print(beauty_time, message['name'])
        print(message['text'])
        print()


print_messages(db)
