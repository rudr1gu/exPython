valorReais = float(input("Digite o valor em reais na carteira: "))

cotacaoDolar = 3.27

quantidadeDolares = valorReais / cotacaoDolar

print(f"Com R${valorReais:.2f} você pode comprar US${quantidadeDolares:.2f}")