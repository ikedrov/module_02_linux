"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from flask import Flask
from datetime import datetime

app = Flask(__name__)

weekdays = datetime.today().weekday()
days = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')
@app.route('/hello-world/<name>')
def hello_world(name):

    if weekdays in (0, 1, 3, 6):
        return f'Привет, {name}. Хорошего {days[weekdays]}!'
    else:
        return f'Привет, {name}. Хорошей {days[weekdays]}!'


if __name__ == '__main__':
    app.run(debug=True)