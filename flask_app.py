from flask import Flask, app, json, render_template, request, jsonify
from json import load

from time import sleep

application = Flask(__name__, static_folder='assets')

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        file = request.files['file']
        file.save('now.json')
        return render_template('res.html')


@application.route('/api/getNews')
def getNews():
    with open('now.json', encoding='utf-8') as file:
        json = load(file)
    return jsonify(json['news'])


@application.route('/api/getName')
def getName():
    sleep(3)
    return 'Вакцины от COVID-19'


@application.route('/api/getTags')
def getTags():
    return jsonify('нии интерфакс эфир инфекция александр роспотребнадзор екатеринбургский семён март москва вакцина "эхо вирусный понедельник центр'.split())


if __name__ == '__main__':
    application.run()