from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    d = 3/2
    return 'Index'


@app.route("/contato")
def contato():
    return 'Contato'

@app.route("/hello/")
@app.route("/hello/<nome>/")
def hello(nome=""):
    return "<h1>Hello World!</h1>\n<h3>Um olá especial do Flask</h3>\n<h4>{}</h4>".format(nome)



if __name__ == '__main__':
    app.run(debug=True, port="3000")