valor = input('digite alguma coisa')

print('O tipo primitivo desse valor é', type(valor))
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('É alfanumérico?', valor.isalnum())
print('Está em maiúsculas?', valor.isupper())
print('Está em minúsculas?', valor.islower())
print('Está capitalizada?', valor.istitle())
print('É um decimal?', valor.isdecimal())
print('É um dígito?', valor.isdigit())
print('É um identificador?', valor.isidentifier())
    