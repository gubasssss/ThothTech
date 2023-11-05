from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import RadioField, validators


app = Flask(__name__)
app.config['SECRET_KEY'] = 'matheusvemnareuniao'  # Substitua por sua própria chave secreta


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



class AvaliacaoForm(FlaskForm):
    scrum_carac1 = RadioField('Característica 1', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])
    scrum_carac2 = RadioField('Característica 2', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])
    scrum_carac3 = RadioField('Característica 3', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])
    scrum_carac4 = RadioField('Característica 4', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])
    # Adicione campos para outras características do Scrum Master
    # ...
    product_owner_carac1 = RadioField('Característica 1', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])
    product_owner_carac2 = RadioField('Característica 2', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])
    product_owner_carac3 = RadioField('Característica 3', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])
    product_owner_carac4 = RadioField('Característica 4', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])
    # Adicione campos para outras características do Product Owner
    # ...
    dev_team_carac1 = RadioField('Característica 1', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])
    dev_team_carac2 = RadioField('Característica 2', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])
    dev_team_carac3 = RadioField('Característica 3', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])
    dev_team_carac4 = RadioField('Característica 4', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                             validators=[validators.InputRequired()])

@app.route('/formulário', methods=['GET', 'POST'])
def autoavaliacao():
    form = AvaliacaoForm(request.form)
    
    if request.method == 'POST' and form.validate():
        # Coleta as notas para Scrum Master
        scrum_carac1 = int(form.scrum_carac1.data)
        scrum_carac2 = int(form.scrum_carac2.data)
        scrum_carac3 = int(form.scrum_carac3.data)
        scrum_carac4 = int(form.scrum_carac4.data)

        # Coleta as notas para Product Owner
        product_owner_carac1 = int(form.product_owner_carac1.data)
        product_owner_carac2 = int(form.product_owner_carac2.data)
        product_owner_carac3 = int(form.product_owner_carac3.data)
        product_owner_carac4 = int(form.product_owner_carac4.data)

        # Coleta as notas para Dev Team
        dev_team_carac1 = int(form.dev_team_carac1.data)
        dev_team_carac2 = int(form.dev_team_carac2.data)
        dev_team_carac3 = int(form.dev_team_carac3.data)
        dev_team_carac4 = int(form.dev_team_carac4.data)
        
        # Realiza o cálculo da maior nota e determina o cargo
        cargo = calcular_cargo(scrum_carac1, scrum_carac2, scrum_carac3, scrum_carac4,
                              product_owner_carac1, product_owner_carac2, product_owner_carac3, product_owner_carac4,
                              dev_team_carac1, dev_team_carac2, dev_team_carac3, dev_team_carac4)
        return render_template('resultado.html', cargo=cargo, form=form)
    
    return render_template('formulário.html', form=form)

def calcular_cargo(scrum_carac1, scrum_carac2, scrum_carac3, scrum_carac4, 
                   product_owner_carac1, product_owner_carac2, product_owner_carac3, product_owner_carac4, 
                   dev_team_carac1, dev_team_carac2, dev_team_carac3, dev_team_carac4):
    pontuacao_scrum = scrum_carac1 + scrum_carac2 + scrum_carac3 + scrum_carac4
    pontuacao_product_owner = product_owner_carac1 + product_owner_carac2 + product_owner_carac3 + product_owner_carac4
    pontuacao_dev_team = dev_team_carac1 + dev_team_carac2 + dev_team_carac3 + dev_team_carac4
    
    # Determinando a categoria com a maior pontuação
    if (pontuacao_scrum > pontuacao_product_owner) and (pontuacao_scrum > pontuacao_dev_team):
        return 'Scrum Master'
    elif (pontuacao_product_owner > pontuacao_scrum) and (pontuacao_product_owner > pontuacao_dev_team):
        return 'Product Owner'
    elif (pontuacao_dev_team > pontuacao_scrum) and (pontuacao_dev_team > pontuacao_product_owner):
        return 'Dev Team'
    else:
        return 'Empate'  # Lida com empates ou outras situações conforme necessário