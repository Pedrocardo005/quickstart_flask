from flask import Flask

app = Flask(__name__)

@app.route('/projects/')
def projects():
    # Com barra no final aceita se você não por a barra no final
    return 'The project page'

@app.route('/about')
def about():
    # Sem a barra no final não identifica se você por depois no final
    return 'The about page'