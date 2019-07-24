import random
from flask import Flask, render_template, request

# pip3 install flask

app = Flask(__name__)

@app.route('/')
def index():
    # вернуть страницу с тестом

    # добавить в форму поля ИМЯ, дата, CVC
    return render_template('fish.html')

@app.route('/save', methods=['POST'])
def save():
    r,h = request.form['r'],request.form['h']
    o=float(h)*3.14*(float(r))**2


    # добавить сохранение данных в файл
    # сказать пользователю кто он - Вупсень или Пупсень? (сделать шаблон)
    return "Объем цилиндра - {}".format(o)

# запускаем сайт
app.run(debug=True)