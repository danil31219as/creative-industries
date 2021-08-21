from flask import Flask, app, json, render_template, request, jsonify
from json import load

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
    

    res = []
    for i in json:
        for article in i['news']:
            res.append(article['headline'])
    return jsonify(res)


@application.route('/api/getName')
def getName():
    return 'Вакцины от COVID-19'


@application.route('/api/getTags')
def getTags():
    return jsonify('интерфакс социалист досрочный майя молдавия четверг выборы заседание глава большинство правительство пост санда утверждение президент март кишинёв парламентский кандидат парламент партия суд владимир посол дата назначение конституционный случай головатюк россия настаивать гроса премьер-министр игорь заявить новый депутат кворум состояться отсутствие фракция получить право назначить ситуация'.split())


if __name__ == '__main__':
    application.run()