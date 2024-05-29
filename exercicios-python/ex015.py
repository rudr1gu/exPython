diasAluguel = int(input("Digite o número de dias de aluguel: "))
kmRodados = float(input("Digite a quantidade de quilômetros rodados: "))

valorDiaria = 60.0
valorKm = 0.15

valorTotal = (diasAluguel * valorDiaria) + (kmRodados * valorKm)

print("O aluguel de {} dias com a Quilometragem {:.2f}km rodadas ficou um valor total a pagar de R$ {:.2f}".format(diasAluguel,kmRodados, valorTotal))