from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html'); 

@app.route('/prueba')
def prueba():
    return render_template('/Implementaciones/lista_simple_PC.html'); 

if __name__ == '__main__':
    app.run(debug=True, port=6060)
