data_nascimento = '05-10-1976'
idade_numerica = 46
altura = 1.74

# Descubra o tipo de dado de cada variável acima
print(type(data_nascimento))
print(type(idade_numerica))
print(type(altura))

# Realize uma operação entre dados do tipo string e inteiro
print(idade_numerica, data_nascimento)

# Realize uma operação entre dados do tipo inteiro e float
arredondamento = idade_numerica / altura

print(round(arredondamento, 2))