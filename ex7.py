pilha = []

pilha.append("Chamada 1")
pilha.append("Chamada 2")
pilha.append("Chamada 3")

print("Próxima chamada para ser atendida: ", pilha[0])

print("Chamada atendida: ", pilha.pop())

print("A lista de chamada está vazia?", len(pilha) == 0)

print("Próxima chamada para ser atendida: ", pilha[0])

print("Chamada atendida: ", pilha.pop())

print("A lista de chamada está vazia?", len(pilha) == 0)

print("Próxima chamada para ser atendida: ", pilha[0])

print("Chamada atendida: ", pilha.pop())

print("A lista de chamada está vazia?", len(pilha) == 0)

print("Não há chamadas em espera")