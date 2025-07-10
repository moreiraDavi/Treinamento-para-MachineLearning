# IFs

# x = int(input("Digite um número inteiro: "))

# y = int(input("Digite um segundo número inteiro: "))

# soma = x + y

# if soma > 0:
#     print("A soma é positiva")
# elif soma < 0:
#     print("A soma é negativa")
# else:
#     print("A soma é igual a 0!")


# FOR

# lista = [1,2,3,4,5]

# for item in list:
#     if item % 2 != 0:
#         item += item
#         print(item)


# WHILE

lista = [1,2,3,4,5,6,7,8,9,10]
i = 0

while i < len(lista) and lista[i] < 11:
    print(lista[i])
    i +=  1

contador = 0

while contador < 10:
    print(f'Ovalor do contador é: {contador}')
    contador += 1