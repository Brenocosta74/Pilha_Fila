# Fila

# Importando collections.deque para o uso de fila
from collections import deque

# Iniciando uma fila vazia

fila = deque()

#Enfileirar elementos

fila.append(10)
fila.append(20)
fila.append(30)

#print(fila)

# Mostrar primeiro elemento da fila
print("Primeiro da fila", fila[0])

#Desinfileirando o primeiro o primeiro elemento
print("Removido: ", fila.popleft())

print("Primeiro da fila", fila[0])
print("Fila está vazia?", len(fila) == 0) #false

print("Removido: ", fila.popleft())
print("Primeiro da fila", fila[0])
print("Fila está vazia?", len(fila) == 0) #false

print("Removido: ", fila.popleft())
print("Fila está vazia?", len(fila) == 0) #true