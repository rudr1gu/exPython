# Solicita a largura e altura da parede ao usuário
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Calcula a área da parede
area = largura * altura

# Calcula a quantidade de tinta necessária em litros
quantidadeTinta = area / 2

# Exibe o resultado
print(f"A área da parede é {area} metros quadrados.")
print(f"A quantidade de tinta necessária é {quantidadeTinta} litros.")