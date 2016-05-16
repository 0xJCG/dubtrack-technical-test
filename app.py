from flask import Flask
from flask import render_template
from flask import request

import requests
import json

app = Flask('technical-test')


def get_rooms():
    url = 'https://api.dubtrack.fm/room'
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return json.loads(response.text)
    return False


def get_room_info(room):
    url = 'https://api.dubtrack.fm/room/' + room
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return json.loads(response.text)
    return False


def get_room_history_playlist(room):
    url = 'https://api.dubtrack.fm/room/' + room + '/playlist/history'
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return json.loads(response.text)
    return False


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        room = get_room_info(request.form['room'])
        if room:
            return render_template('search.html', room=room)
        else:
            return render_template('error.html')
    rooms = get_rooms()
    return render_template('index.html', rooms=rooms)


@app.route('/playlist/<room_url>')
def show_room_info(room_url):
    room = get_room_info(room_url)
    if room:
        playlist = get_room_history_playlist(room['data']['_id'])
        return render_template('room.html', playlist=playlist)
    return render_template('error.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
