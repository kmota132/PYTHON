#VARIAVEIS
"""
#variaveis
x = 3
y = "hello"
#para comentar utilizamos ### ou p
print(y)
################################
print(type(x))#utilizamos o type para nos verificarmos o tipo dos dados

"""

#MUITOS VALORES PARA VARIAVEIS
"""
x, y, z = "oranege", "dados", "carro"
print(x)
print(y)
print(z)
#podemos atribuir o mesmo valor a uma variavel """

#DESCONPACTAR

fruits = ["apple", "banana", "laranja"]
x, y, z = fruits
print(x)
print(y)
print(z)
#nos podemos extrair informaçoes de uma lista 

#VARIAVEIS DE SAIDA

x = "python e lindin",
y = '23'
z = 'NOS'
print(x, y + z)
#VARIAVEIS GLOBAIS


x = "dois"
def myfunc():
 x = "quatro"
 print("tudo" + x)
myfunc()
print("tudo" + x) #Se você criar uma variável com o mesmo nome dentro de uma função, esta variável será local, e só poderá ser utilizada dentro da função

