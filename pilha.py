#Pilha

#Iniciando uma pilha vazia
pilha = []

#Empilhando elementos

pilha.append(10)
pilha.append(74)
pilha.append(54)

#Mostrar a pilha
#print(pilha)

#Mostrar o topo da pilha
#print("Topo da pilha", pilha [-1])

#Remove o item que está no topo
#print("Removido: ", pilha.pop())
#print(pilha)

#Mostra se a pilha está vazia
print("Pilha está vazia?", len(pilha) == 0) #false

print("Removido: ", pilha.pop())
print("Topo da pilha", pilha [-1])

print("Pilha está vazia?", len(pilha) == 0) #false

print("Removido: ", pilha.pop())
print("Topo da pilha", pilha [-1])

print("Pilha está vazia?", len(pilha) == 0) #true
