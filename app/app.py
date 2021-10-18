from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/implementacion/<string:name>')
def implementacion(name):
    nombre = name + '.html'
    return render_template('Implementaciones/' + nombre)

if __name__ == '__main__':
    app.run(debug=True, port=6060)
