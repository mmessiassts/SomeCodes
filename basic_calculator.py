print("Digite:\n\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n")

escolha = input("Digite sua escolha: ")

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if escolha == '1':
    print(a+b)

elif escolha == '2':
    print(a-b)

elif escolha == '3':
    print(a*b)

elif escolha == '4':
    print(a/b)

else:
    print("Escolha inválida")