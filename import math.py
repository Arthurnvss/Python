import math

def calcular_hipotenusa(cateto_a, cateto_b):
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    return hipotenusa

# Exemplo de uso
cateto_a = float(input("Digite o comprimento do cateto a: "))
cateto_b = float(input("Digite o comprimento do cateto b: "))

hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
print(f"A hipotenusa é: {hipotenusa:.2f}")
