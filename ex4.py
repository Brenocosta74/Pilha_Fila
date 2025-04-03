from collections import deque

fila = deque()

fila.append(1)
fila.append(2)
fila.append(3)

print("Primeiro da fila: ", fila[0])

print("Removido: ", fila.popleft())

print("Fila está vazia?", len(fila) == 0)