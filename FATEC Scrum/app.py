from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/master')
def master():
    return render_template('master.html')

@app.route('/dev')
def quemsomos():
    return render_template('dev.html')

@app.route('/artefatos')
def artefatos():
    return render_template('artefatos.html')

@app.route('/beneficios')
def beneficios():
    return render_template('beneficios.html')

@app.route('/productowner')
def productowner():
    return render_template('productowner.html')

@app.route('/cerimonias')
def cerimonias():
    return render_template('cerimonias.html')

@app.route('/formulário')
def formulário():
    return render_template('formulário.html')