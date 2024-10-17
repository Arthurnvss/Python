# Inicializa a variável para armazenar a soma
soma_pares = 0

# Usa um laço para percorrer os números de 1 a 50
for numero in range(1, 51):
    # Verifica se o número é par
    if numero % 2 == 0:
        soma_pares += numero  # Adiciona o número par à soma

# Exibe o resultado
print(f"A soma dos números pares entre 1 e 50 é: {soma_pares}")
