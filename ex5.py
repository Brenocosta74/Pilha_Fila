from collections import deque

fila = deque()

fila.append(" Paciente 1")
fila.append("Paciente 2")
fila.append("Paciente 3")

print("Próximo paciente: ", fila[0])
print("Paciente atendido: ", fila.popleft())
print("Próximo paciente: ", fila[0])
print("Paciente atendido: ", fila.popleft())
print("Próximo paciente: ", fila[0])
print("Paciente atendido: ", fila.popleft())