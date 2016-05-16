from flask import Flask
from flask import render_template
from flask import request

import requests

app = Flask('technical-test')


def get_channels():
    url = 'https://api.dubtrack.fm/room'
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return True
    return False


def get_channel_info(channel):
    url = 'https://api.dubtrack.fm/room' + channel
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return True
    return False


@app.route('/', method='POST')
def index():
    if request.method == 'POST':
        channel = get_channel_info(request.form['channel'])
        if channel:
            return render_template('search.html', channel=channel)
        else:
            return render_template('error.html')
    channels = get_channels()
    return render_template('index.html', channels=channels)


@app.route('/<int:channel_id>')
def show_channel_info(channel_id):
    ch = get_channel_info(channel_id)
    if ch:
        return render_template('channel.html')
    return render_template('error.html')


if __name__ == '__main__':
    app.run()
