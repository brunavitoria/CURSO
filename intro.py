########### Iniciando em Python ###########

# Variáveis
nome = "Bruna" # str - texto
notaProva1 = 7.8 # float - real
notaProva2 = 9 # int - inteiro
verdadeiro = True # bool - booleano
# Variável de um cálculo
media = (notaProva1+notaProva2)/2 
# Variável informada pelo usuário
nomedousuario  = input("Qual seu nome?") 
# Estruturas de dados
numeros = [1, 2, 3, 4, 5] # list - lista
numeros2 = 1, 2, 3, 4, 5 # tuple - tuplas
numeros3 = {'Um': 1, 'Dois': 2, 'Três': 3} # dictionary - dicionário

# Criando uma Função
def seunome(nomeinformado):
    n = 'Seu nome é ' + nomeinformado
    return n

# Recebendo o retorno de uma função
nomeuser = seunome(nome)

# Contando caracteres
len(nomeuser)
print('Caracteres:', len(nomeuser)) # >> Caracteres: 16

# Tipo de dado
type(nomeuser)
print('Tipo:', type(nomeuser)) # >> Tipo: <class 'str'>

# Impressões

# Imprimindo texto
print("Olá mundo!")
# Imprimindo variável
print(notaProva1) # >> 9.5
# Imprimindo texto e variável formatada
print("Nota final: %.2f " %notaProva1)  # >> Nota final: 9.50
# O valor inserido antes do ponto ou depois 
# do ponto equivale a quantidade de casas decimais 
# que deseja exibir do valor final
print("Nota final: %0.2f " %notaProva1) # >> Nota final: 9.50
print("Nota final: %.5f " %notaProva1) # >> Nota final: 9.50000
# Caso o valor informado de casas antes seja maior 
# que o numero ele insere espaços
print("Nota final: %4.0f " %notaProva1) # >> Nota final:   10 
# Imprimindo texto e variável de tipo string
print("Olá", nome ,"seja bem-vinda!") # >> Olá Bruna seja bem-vinda!
print("Olá %s seja bem-vinda!" % nome) # >> Olá Bruna seja bem-vinda!
# Imprimindo texto e variável
print("A media das notas ", notaProva1, " e ", notaProva2, " é ", media) # >> A media das notas  7.8  e  9  é  8.4
# Imprimindo texto e resultado de uma expressão
print("A metade de um dia equivale a ", 24/2, " horas.") # >> A metade de um dia equivale a  12.0  horas.

# Imprimindo uma função
print(seunome(nome)) # >> Seu nome é Bruna
print(nomeuser) # >> Seu nome é Bruna

# Comandos de condições
if notaProva1 > notaProva2:
    print("A nota da prova 1 é maior que a nota da prova 2")
elif notaProva1 == notaProva2:
    print("A nota da prova 1 é igual a nota da prova 2")
else:
    print("A nota da prova 1 não é maior que a nota da prova 2")
    print(len(nome))
    print(5/5)

# Comandos de repetições
# Imprimindo números de 1 ao 10
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in numero:
    print(n)

n = 1
while n <= 10:
    print(n)
    n += 1

########### Uso de bibliotecas ###########

# Importando bibliotecas
import retangulo
import retangulo as ret

# Utilizando bibliotecas
retangulo = ret
print(retangulo.area(5,10)) # >> 50
print(retangulo.comprimento(5,10)) # >> 30

########### Uso da biblioteca NumPy ###########
import numpy
import numpy as np

# Matriz unidimensional
numeros1d = np.array([1, 2, 3, 4, 5])
# Matriz bidimensional
numeros2d = np.array([
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1]
])

# shape, informa a quantidade de valores e dimensões
print(numeros1d.shape)
print(np.arange(6))