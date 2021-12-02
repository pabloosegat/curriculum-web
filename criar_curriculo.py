from util import database

mysql = database.SQL('root', '', 'programacao_web')

#Tabela de formação
cmd = 'DROP TABLE IF EXISTS tb_formacao;'
if mysql.executar(cmd, ()):
    print('Tabela de formação excluída!')

cmd = '''
    CREATE TABLE tb_formacao(
        id_formacao INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(20) NOT NULL,
        data_formacao VARCHAR(17) NOT NULL,
        universidade VARCHAR(30) NOT NULL);
'''
if mysql.executar(cmd, ()):
    print('Tabela de formação criada!')

#Tabela de competência
cmd = 'DROP TABLE IF EXISTS tb_competencia;'
if mysql.executar(cmd, ()):
    print('Tabela de competências excluída!')

cmd = '''
    CREATE TABLE tb_competencia(
        id_competencia INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(20) NOT NULL);
'''
if mysql.executar(cmd, ()):
    print('Tabela de competencias criada!')

#Tabela de experiência
cmd = 'DROP TABLE IF EXISTS tb_experiencia;'
if mysql.executar(cmd, ()):
    print('Tabela de experiência excluída!')

cmd = '''
    CREATE TABLE tb_experiencia(
        id_experiencia INT AUTO_INCREMENT PRIMARY KEY,
        empresa VARCHAR(20) NOT NULL,
        data_experiencia VARCHAR(17) NOT NULL,
        funcao VARCHAR(20) NOT NULL,
        desc_exp TEXT NOT NULL);
'''
if mysql.executar(cmd, ()):
    print('Tabela de experiência criada!')