pilha = []

pilha.append("Youtube")
pilha.append("Instagram")
pilha.append("Facebook")

print(pilha)

print("Última página visitada: ", pilha[-1])

ultimo_item = pilha[-1]
pilha = pilha[:-1]
pilha = [ultimo_item] + pilha

print("Nova ordem de histórico: ", pilha)

primeiro_item = pilha[0]
pilha = pilha[1:]
pilha = pilha + [primeiro_item]

print("Nova ordem de histórico após voltar a página: ", pilha)