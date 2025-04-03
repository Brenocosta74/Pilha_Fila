pilha = []

pilha.append(5)
pilha.append(10)
pilha.append(15)

print("Topo da pilha: ", pilha[-1])

print("Removido", pilha.pop())

print("Pilha vazia? ", len(pilha) == 0)