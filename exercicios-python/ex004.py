valor = input('digite qualquer coisa')

if valor.isalpha():
    print('você escreveu letras')
elif valor.isnumeric():
    print('você escreveu um numero')
else:
    print('você escreveu letras e numeros')
    