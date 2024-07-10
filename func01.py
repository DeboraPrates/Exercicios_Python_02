def hello(nome, idade):
    print(f'Olá {nome}!')
    if (int(idade)) > 15:
        print("Você pode votar!")
    else:
        print("Você ainda não pode votar!")
hello("Joca", 19)
hello("Ana", "14")