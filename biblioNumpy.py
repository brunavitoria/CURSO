########### Uso da biblioteca NumPy ###########
import numpy
import numpy as np

# Matriz unidimensional
numeros1d = np.array([1, 2, 3, 4, 5])

# shape -> informa a quantidade de valores e dimensoes
print(numeros1d.shape)
# arange -> cria uma matriz unidimensional com base nos dados informados
# arange ( [ inicio , ] fim , [ espacamento , ] dtype = None , * , like = None )
print(np.arange(6)) # [0, 1, 2, 3, 4, 5]
print(np.arange(0, 10, 2)) # [0 2 4 6 8]
# reshape((dimencoes, elementos)) -> redimensiona uma matriz
a = np.arange(6).reshape((2, 3)) # [0, 1, 2, 3, 4, 5] ficou [[0, 1, 2],[3, 4, 5]]
print(a)

# Acessando matriz pelo indice
print(numeros1d[0]) # >> 1
print(a[0][2]) # >> 2

# Alterando dados de um indice da matriz
numeros1d[0] += 5
print(numeros1d) # >> 5

# Imprimindo uma parcela da matriz
print(numeros1d[2:4]) # Imprime do indice 2 ao 4 (nao inclui o 4) >> [3, 4]

# empty() -> cria uma matriz vazia
x = np.empty([3], dtype = int) 
print(x)

# zeros() -> cria uma matriz com valores = 0
matriz_zeros = np.zeros((5)) 
print(matriz_zeros)

# ones() -> cria uma matriz com valores = 0
matriz_ones = np.ones((5)) 
print(matriz_ones)

# random.random() -> cria uma matriz de valores aleatorios
matriz_random = np.random.random((5)) 
print(matriz_random)


# Matriz bidimensional
numerosa = np.array([
    [6, 8],
    [10, 9]
])
numerosb = np.array([
    [1, 2],
    [5, 3]
])

# Realizando operacoes basicas com matrizes numpy
print('Soma = ', numerosa+numerosb)
print('Subtracao = ', numerosa-numerosb)
print('Multiplicacao = ', numerosa*numerosb)
print('Divisao = ', numerosa/numerosb)

# Algumas operacoes matematicas
print('Multiplicacao de matrizes = ', numerosa.dot(numerosb))
print('Media = ', numerosa.mean())
print('Soma = ', sum(numerosa))