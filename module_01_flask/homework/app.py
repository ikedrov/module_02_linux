import datetime
from flask import Flask
import random
import os
import re

app = Flask(__name__)


@app.route('/hello_word')
def test_function():

   return 'Привет, мир!'


cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
@app.route('/cars')
def test_function():

   global cars
   return (', '.join(map(str, cars)))


cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
@app.route('/cats')
def test_function():

   return random.choice(cats)


@app.route('/get_time/now')
def test_function():

   current_time = datetime.datetime.now()
   return f'Точное время: {current_time}'


@app.route('/get_time/future')
def test_function():

   current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
   return f'Точное время через час будет {current_time_after_hour}'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

with open(BOOK_FILE) as book:
    words = book.read().split()

@app.route('/get_random_word')
def test_function():

    global words
    word = random.choice(words)
    return re.sub(r'[^\w\s]', '', word)

counter = 0
@app.route('/counter')
def test_function():
    global counter
    counter += 1
    return f'This page was opened {counter} times'
