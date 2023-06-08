import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test_function():
   return 'Это тестовая страничка, ответ сгенерирован в %s' % \
                     datetime.datetime.now().utcnow()

counter = 0
@app.route('/hello_world')
def hello_world():
    global counter
    counter += 1
    return f'Hello world. This page was opened {counter} times'
