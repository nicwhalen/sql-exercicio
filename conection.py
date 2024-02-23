import sqlite3
import pandas as pd
import numpy as np

conexao = sqlite3.connect('exercicio')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto). 

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior. 

#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Maria Clara", 19, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Anna Luiza", 21, "Enfermagem")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Ana Julia", 22, "Ciência da Computação")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "João Lucas", 19, "Serviço Social")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "André Junior", 20, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (6, "Taynara Silva", 18, "Ciência da Computação")')

#3. Consultas Básicas 
#Escreva consultas SQL para realizar as seguintes tarefas: 
#a) Selecionar todos os registros da tabela "alunos". 

#cursor.execute('SELECT * FROM alunos') OK

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos. 

#cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética. 

#cursor.execute('SELECT * FROM alunos GROUP BY nome HAVING curso=="Engenharia"')

#d) Contar o número total de alunos na tabela 
alunos.count()

#4. Atualização e Remoção 
#a) Atualize a idade de um aluno específico na tabela. 

#cursor.execute('UPDATE alunos SET idade=20 WHERE nome="João Lucas"')

#b) Remova um aluno pelo seu ID. 

#cursor.execute('DELETE FROM alunos WHERE id=6')

#5. Criar uma Tabela e Inserir Dados Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

#cursor.execute('CREATE TABLE clientes(id INT NOT NULL PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Marcela", 32, 1200)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Clarisse", 25, 2230)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Lucas", 27, 2400)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Jamile", 33, 1980)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Paulo", 37, 2710)')

#6. Consultas e Funções Agregadas Escreva consultas SQL para realizar as seguintes tarefas: 
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos. 

#cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')

#b) Calcule o saldo médio dos clientes. 



#c) Encontre o cliente com o saldo máximo. 



#d) Conte quantos clientes têm saldo acima de 1000. 


dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')
for usuario in dados:
    print(usuario)

conexao.commit()
conexao.close