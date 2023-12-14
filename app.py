from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    d = 3/2
    return 'Index'

@app.route("/contato")
def contato():
    return 'Contato'

def teste():
    return '<h3>Testando Flask</h3>'

app.add_url_rule("/teste","teste",teste)


if __name__ == '__main__':
    app.run(debug=True, port="3000")