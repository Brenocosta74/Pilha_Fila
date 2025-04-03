pilha = []

nome = input(str("Digite um nome: "))
pilha.append(nome)

resposta = input(str("Deseja adicionar mais um nome? (sim/nao): "))
if resposta == "sim":
    nome = input(str("Digite um nome: "))
    pilha.append(nome)
elif resposta == "nao":
    print("ok")

resposta = input ("Deseja remover o último nome? (sim/nao): ")
if resposta == "sim":
    if len(pilha) > 0:
        nome_removido = pilha.pop()
        print(f"Nome removido: {nome_removido}")
    else:
        print("Não há nomes para remover")
elif resposta == "nao":
    print("ok")

desfazer = input(str("Deseja desfazer a remoção? (sim/nao): "))
if desfazer == "sim":
    pilha.append(nome_removido)
    print(f"Nome desfeito: {nome_removido}")
elif desfazer == "nao":
    print("ok")

print(pilha)