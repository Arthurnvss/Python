# Solicita ao usuário que insira um número
numero = int(input("Digite um número para ver sua tabuada: "))

# Exibe a tabuada do número fornecido
print(f"\nTabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
