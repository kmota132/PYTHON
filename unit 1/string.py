#STRING(AS STRING EM PYTHON SAO COLOCADAS EM ASPAS "" OU '')
"""
print('hello')
print("hello")
"""
#ABRIBUIÇÃO DE VARIAVEL / STRING MULTIPLA
"""
a = "lambo"
print(a)
"""
#ARRAY
"""
a = "Hello, World!"
print(a[4])# o indice infomrado serve para buscar dentro do caracter espesifico
"""
#PERCORRENDO UMA STRING
for x in "Lanranja":
    print(x)

a = "banana, laranja"
print(len(a))#numero de caracteres

algo = "a lanranja da manda esta preta"
print("manda" in algo)# serve para confirma se algo existe em uma string 

algo = "a lanranja da manda esta preta"
if "manda" in algo:# pode usar o "not in" para verificar se nao esta 
    print("CLARO ") # SERVE PARA CONDICIONAIS 

#SLICING PYTHON [CORTANDO]
n = "Hello, mundo"
print(n[2:5])# ou seja nos definimos que queriamos algo entre o caractere 2 e 5

#MODIFY STRINGS
n = "Hello, mundo"# podemos usar o lower() para minusculas
print(n.upper())#faz com que as letras fiquem maiusculas

#REMOVAÇAO DE ESPAÇO VAZIO
n = "Hello, mundo" # o metodo sprit serve para remover /n
print(n.strip())

#SUBSTITUIR STRING
n = "Hello, mundo"
print(n.replace("H", "w"))# USADO PARA SUBSTITUIR UMA CARACTE

#SEPARAR
n = "Hello, mundo"
print(n.split(",")) #método divide a string em substrings se encontrar instâncias do separador

#CONCATENAÇAO
a = "tudo"
b = "dois"
c = a + b 
print(c)
