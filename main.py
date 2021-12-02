from util import connectiondb
from flask import Flask, render_template, request, redirect, url_for
'''
set FLASK_DEBUG=1
set FLASK_ENV=development
set FLASK_APP=main.py
flask run
'''
app = Flask(__name__)

#------ Visualização do currículo ------
@app.route('/')
def curriculo():
    mysql = connectiondb.SQL('curriculum_pablo')

    cmd = 'SELECT * FROM tb_formacao;'
    cs = mysql.consultar(cmd, [])
    formacoes = cs.fetchall()

    cmd = 'SELECT * FROM tb_competencia;'
    cs = mysql.consultar(cmd, [])
    competencias = cs.fetchall()

    cmd = 'SELECT * FROM tb_experiencia;'
    cs = mysql.consultar(cmd, [])
    experiencias = cs.fetchall()

    return render_template('curriculum.html', formacoes=formacoes, competencias=competencias, experiencias=experiencias)

#------ Formulário ------
@app.route('/formularioIncluir')
def formulario():
    return render_template('formIncluir.html')

#------ Incluir dados ------
@app.route('/incluirForm', methods=['POST'])
def incluirForm():
    form = request.form['form']
    dta_form = request.form['dta_form']
    universidade = request.form['universidade']

    mysql = connectiondb.SQL('curriculum_pablo')
    cmd = "INSERT INTO tb_formacao(nome, data_formacao, universidade) VALUES (%s, %s, %s);"

    mysql.executar(cmd, [form, dta_form, universidade])

@app.route('/incluirComp', methods=['POST'])
def incluirComp():
    comp = request.form['comp']

    mysql = connectiondb.SQL('curriculum_pablo')
    cmd = "INSERT INTO tb_competencia(nome) VALUES (%s);"

    mysql.executar(cmd, [comp])

@app.route('/incluirExp', methods=['POST'])
def incluirExp():
    empresa = request.form['empresa']
    dta_exp = request.form['dta_exp']
    func = request.form['func']
    desc_exp = request.form['desc_exp']

    mysql = connectiondb.SQL('curriculum_pablo')
    cmd = "INSERT INTO tb_experiencia(empresa, data_experiencia, funcao, desc_exp) VALUES (%s, %s, %s, %s);"

    mysql.executar(cmd, [empresa, dta_exp, func, desc_exp])

#------ Excluir dados ------
@app.route('/excluir')
def excluirDados():
    mysql = connectiondb.SQL('curriculum_pablo')

    cmd = "TRUNCATE TABLE tb_formacao;"
    mysql.executar(cmd, [])
    cmd = "TRUNCATE TABLE tb_competencia;"
    mysql.executar(cmd, [])
    cmd = "TRUNCATE TABLE tb_experiencia;"
    mysql.executar(cmd, [])

    return redirect(url_for('curriculo'))

app.run()