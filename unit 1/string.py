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

#FORMATAÇAO DE STRING
"""
idade = 21
algo = "meu nome e keven, e eu tenho {}"
print(algo.format(idade)) 
"""
idade = 21
peso = 55
altura = 1,72
algo = "meu nome e keven e tenho {} tenho o peso de {} e minhas altura e {}"
print(algo.format(idade, peso, altura)) # utilizado para juntar as informaçoes

#todos os metodos
"""
Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""
