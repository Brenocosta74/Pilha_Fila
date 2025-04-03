from collections import deque

fila = deque()

fila.append("Documento 1")
fila.append("Documento 2")
fila.append("Documento 3")

print("Documento a ser impresso: ", fila[0])

print("Documento impresso: ", fila.popleft())

print("Documento a ser impresso: ", fila[0])

print("Documento impresso: ", fila.popleft())

print("Documento a ser impresso: ", fila[0])

print("Documento impresso: ", fila.popleft())