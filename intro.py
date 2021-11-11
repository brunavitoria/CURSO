# Variáveis
# nome = "Bruna" # str - texto
# Funções
# Criando uma função
# def seunome(nomeinformado):
#     n = 'Seu nome é ' + nomeinformado
#     return n
# Recebendo o retorno de uma função
# nomeuser = seunome(nome)
# nomeuser2 = seunome('Fulano')
# Outras funções
# print(nomeuser2)
# Imprimindo uma função
# print(nomeuser)
# >> Seu nome é Bruna
# >> Seu nome é Fulano
# Contando caracteres
# len(nomeuser)
# print('Caracteres:', len(nomeuser))
# >> Caracteres: 16
# type(nomeuser2)
# print('Tipo:', type(nomeuser2))
# >> Tipo: <class 'str'>
# notaProva1 = 7.8 # float - real
# notaProva2 = 9 # int - inteiro
# verdadeiro = True # bool - booleano
# Variável de um cálculo
# media = (notaProva1+notaProva2)/2 
# Variável informada pelo usuário
# nomedousuario  = input("Qual seu nome?") 
# Estruturas de dados
# numeros = [1, 2, 3, 4, 5] # list - lista
# numeros2 = 1, 2, 3, 4, 5 # tuple - tuplas
# numeros3 = {'Um': 1, 'Dois': 2, 'Três': 3} # dictionary - dicionário
# print(numeros)
# print(numeros2)
# print(numeros3)
# >> [1, 2, 3, 4, 5]
# >> (1, 2, 3, 4, 5)
# >> {'Um': 1, 'Dois': 2, 'Três': 3}
# print(nomedousuario)
# # >> Qual seu nome? Bruna
# # >> Bruna
# # nota = 9.5
# # Imprimindo texto
# print("Olá mundo!")
# python3 nomedoprograma.py
# >> Olá mundo!
# # Impressões
# nota = 9.5
# nome = "Bruna"
# # Imprimindo variável
# print(nota)
# # Imprimindo texto e variável formatada
# print("Nota final: %.2f " %nota) 
# # O valor inserido antes do ponto ou depois 
# # do ponto equivale a quantidade de casas decimais 
# # que deseja exibir do valor final
# print("Nota final: %0.2f " %nota) 
# print("Nota final: %.5f " %nota) 
# # Caso o valor informado de casas antes seja maior 
# # que o numero ele insere espaços
# print("Nota final: %4.0f " %nota)
# # Imprimindo texto e variável de tipo string
# print("Olá", nome ,"seja bem-vinda!")
# print("Olá %s seja bem-vinda!" % nome)
# # Imprimindo texto e variável
# print("A media das notas ", notaProva1, " e ", notaProva2, " é ", media)
# # Imprimindo texto e resultado de uma expressão
# print("A metade de um dia equivale a ", 24/2, " horas.")

# # >> 9.5
# # >> Nota final: 9.50 
# # >> Nota final: 9.50 
# # >> Nota final: 9.50000 
# # >> Nota final:   10 
# # >> Olá Bruna seja bem-vinda!
# # >> Olá Bruna seja bem-vinda!
# # >> A media das notas  7.8  e  9  é  8.4
# # >> A metade de um dia equivale a  12.0  horas.

# # Comandos e expressões
# if notaProva1 > notaProva2:
#     print("A nota da prova 1 é maior que a nota da prova 2")
# elif notaProva1 == notaProva2:
#     print("A nota da prova 1 é igual a nota da prova 2")
# else:
#     print("A nota da prova 1 não é maior que a nota da prova 2")
#     print(len(nome))
#     print(5/5)
# print("""\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)
# print("""
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)
# print("Let's not go to %s. 'Tis a silly." % nome)

import retangulo
import numpy as np

# print(retangulo.area(5,10))
# print(retangulo.comprimento(5,10))
numeros = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
print(numeros.shape)
a = np.arange(6).reshape((3, 2))
print(a)
print(numeros.reshape(3, 2))