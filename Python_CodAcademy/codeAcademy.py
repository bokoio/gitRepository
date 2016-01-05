"""
     Operadores Booleanos
------------------------
True and True e True
True and False e False
False and True e False
False and False e False

True or True e True
True or False e True
False or True e True
False or False e False

Not True e False
Not False e True

"""


  if answer == "left" or answer == "l":
        print "Esta e a sala de Abuso Verbal, seu monte de caca de papagaio!"
    elif answer == "right" or answer == "r":
        print "E claro que esta e a Sala das Discussoes. Eu ja disse isso!"
    else:
        print "Voce nao escolheu esquerda ou direita. Tente de novo."



# Atribua True ou False conforme apropriado nas linhas abaixo!

# (20 - 10) > 15
bool_one = False    # Fizemos esta para voce!

# (10 + 17) == 3**16
# Lembre-se que ** pode ser lido como 'elevado a'. 3**16 e cerca de 43 milhoes.
if ((10 + 17) == 3**16):
    bool_two = True
else:
    bool_two = False
# 1**2 <= -1
if 1**2 <= -1:
    bool_three = True
else:    
    bool_three = False

# 40 * 4 >= -4
if 40 * 4 >= -4:
    bool_four = True
else:
    bool_four = False

# 100 != 10**2
if 100 != 10**2:
    bool_five = True
else:
    bool_five = False

# Crie declaracoes comparativas conforme apropriado nas linhas abaixo!

# Torne-me verdade!
bool_one = 3 < 5  # Ja fizemos este para voce!

# Torne-me falso!
bool_two = 1**25 == 25 * 10

# Torne-me verdade!
bool_three = (15 / 5) <= (15 / 5)

# Torne-me falso!
bool_four = 77 * 3 < 189

# Torne-me verdade!
bool_five = 1 == 1


bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100**0.5 >= 50 or False

bool_four = True or True

bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1

def using_control_once():
    if True or not 31 + 31 == 61:
        return "Successo #1"

def using_control_again():
    if 45 + 45 == 90 or True:
        return "Successo #2"

print using_control_once()
print using_control_again()

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


# Tenha certeza que the_flying_circus() retorna True
def the_flying_circus():
    if "Monster" == "Tronca" and 31 * 2 <= 62:   # Comece seu codigo aqui!
        return False
        print "False"
        # Nao esqueca de recuar
        # o codigo dentro deste bloco!
    elif "Monster" == "Moster" or True:
        return True
        print "True"
        # Continue aqui.
        # Voce vai querer adicionar tambem a declarao else!
    else:
        return True
        print "Indiferente"

#exibir numeros pares entre 0 e 50
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

Pig Latin é um jogo linguístico, em que você move a primeira letra da palavra para o final e adiciona "ay". Então, "Python" se torna "ythonpay". Eis as etapas que você deverá realizar para escrever um tradutor de Pig Latin em Python.

    Peça ao usuário para inserir uma palavra em inglês.
    Garanta que o usuário inseriu uma palavra válida.
    Converta a palavra do inglês para o Pig Latin.
    Exiba o resultado da tradução.
...


print "Pig Latin"

----------
print 'Bem-vindo ao Tradutor de Pig Latin!'

# Comece seu codigo aqui!
original = raw_input("Qual o seu nome?")
print original

----------
print 'Bem-vindo ao Tradutor de Pig Latin!'

# Comece seu codigo aqui!
original = raw_input("Qual o seu nome?")
if len(original) > 0:
    print original
else:
    print "empty"
----------
"""
Na primeira linha, criamos uma string com letras e números.

A segunda linha então executa a função isalpha() que retorna False, já que a string contém caracteres que não são letras.
"""

print 'Bem-vindo ao Tradutor de Pig Latin!'

# Comece seu codigo aqui!
original = raw_input("Qual o seu nome?")
if len(original) > 0 and original.isalpha():
    print original
else:
    print "empty"
----------------
print 'Bem-vindo ao Tradutor de Pig Latin!'
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    print original
    print word
    print first
else:
    print 'empty'
-------------------

print 'Bem-vindo ao Tradutor de Pig Latin!'
pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print original
    print word
    print first
    print new_word
else:
    print 'empty'

---------------
print 'Bem-vindo ao Tradutor de Pig Latin!'
pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'

--------------------
def tax(bill):
    """Soma 8% de imposto a uma conta de restaurante."""
    bill *= 1.08
    print "Com imposto: %f" % bill
    return bill

def tip(bill):
    """Soma uma gorjeta de 15% a uma conta de restaurante."""
    bill *= 1.15
    print "com gorjeta de: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

------------------

def square(n):
    """Retorna o quadrado de um numero."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    
# Chame a funcao quadrado na linha 9! Tenha certeza de
# incluir o numero 10 entre os parenteses.
square(10)

------------------

def power(base,exponent):  # Adicione seus parametros aqui!
    result = base**exponent
    print "%d elevado a %d e %d." % (base, exponent, result)

power(37,4)  # Adicione seus argumentos aqui!

------------------
-----------------------------
def one_good_turn(n):
    return n + 1
    
def deserves_another(m):
    return one_good_turn(m) + 2


-----------------
def cube(number):
    return number * (number * number)

def by_three(number):
    if cube(number) % 3 == 0:
        return cube(number)
    else:        
        return False
---------------

# Peça ao Python para exibir sqrt(25) na linha 3.
import math
print math.sqrt(25)

# Importe *apenas* a função sqrt de math na linha 3!

from math import sqrt

# Importe *tudo* do módulo math na linha 3!

from math import *
------------------------------------
import math            # Importa o modulo math
everything = dir(math) # Converte tudo em uma lista de coisas de math
print everything       # Exibe tudo!

------------------
def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

----------------------
# Iguale maximum ao valor maximo de qualquer conjunto de numeros na linha 3!

maximum = max(123,345,999,899.9,998.9)

print maximum

# Iguale minimum ao menor valor de qualquer conjunto de numeros na linha 3!

minimum = min(-99,-100,1,0,10,-101)

print minimum

absolute = abs(-42)

print absolute
---------------
# Exiba os tipos de um inteiro (integer), um número de ponto flutuante (float),
# e uma string em linhas separadas abaixo.
print type(99)
print type(9.9)
print type('Pippo')

---------------------------
def shut_down(s):
    if s == "yes":
        return "Desligando"
    elif s == "no":
        return "Desligamento abortado"
    else:
        return "Desculpe"


--------------
from math import sqrt

print sqrt(13689)

----------------

def distance_from_zero(dfz):
    if type(dfz) == int or type(dfz) == float:
       return abs(dfz)
    else:
        return "Nao"
-----------------------------
def hotel_cost(nights):
    return 140 * nights

-----------------------------
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
------------------------------
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    cost_day = days * 40
    if days >= 7:
        cost_day -= 50
        return cost_day
    elif days >= 3 and days < 7:
        cost_day -=20
        return cost_day
    else:
        return cost_day        
---------------------------
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    cost_day = days * 40
    if days >= 7:
        cost_day -= 50
        return cost_day
    elif days >= 3 and days < 7:
        cost_day -=20
        return cost_day
    else:
        return cost_day
def trip_cost(city,days):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) 
----------------
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    cost_day = days * 40
    if days >= 7:
        cost_day -= 50
        return cost_day
    elif days >= 3 and days < 7:
        cost_day -=20
        return cost_day
    else:
        return cost_day
def trip_cost(city,days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + trip_money(spending_money)

def trip_money(spending_money):
    return spending_money

-----------------------------
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    cost_day = days * 40
    if days >= 7:
        cost_day -= 50
        return cost_day
    elif days >= 3 and days < 7:
        cost_day -=20
        return cost_day
    else:
        return cost_day
def trip_cost(city,days, spending_money):
    print trip_cost(city,days, spending_money)
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + trip_money(spending_money)

def trip_money(spending_money):
    return spending_money
------------
numbers = [5, 6, 7, 8]

print "Somando os numeros nos indices 0 e 2..."
print numbers[0] + numbers[2]
print "Somando os numeros nos indices 1 e 3..."
# Seu codigo vem aqui!
print numbers[1] + numbers[3]
------------
zoo_animals = ["pangolin", "casuar", "preguica", "tigre"]
# Noite passada a preguica do zoologico atacou brutalmente 
# o pobre tigre e o devorou inteiro.

# A feroz preguica foi substituida por uma amigavel hiena.
zoo_animals[2] = "hiena"

# Que animal deveria preencher o vazio deixado pelo pobre tigre falecido?
# Seu codigo aqui!
zoo_animals[3] = "Pippo"
------------
suitcase = []
suitcase.append("oculos escuros")

# Seu codigo aqui!
suitcase.append("biquini")
suitcase.append("Sunga")
suitcase.append("Boia")


list_length = len(suitcase) # Iguale ao comprimento da valise

print "Ha %d itens na valise." % (list_length)
print suitcase
-------------------
suitcase = ["oculos escuros", "chapeu", "passaporte", "laptop", "camisa", "sapatos"]

first  = suitcase[0:2]  # O primeiro e segundo itens (indices zero e um)
middle = suitcase[2:4]  # Terceiro e quarto itens (indices dois e tres)
last   = suitcase[4:6]  # Os ultimos dois itens (indices quatro e cinco)

------------------

animals = "catdogfrog"
cat  = animals[:3]   # Os tres primeiros caracteres de animals
dog  = animals[3:6]  # O quarto ate sexto caracteres
frog = animals[6:]   # A partir do setimo caractere ate o final
----------------

my_list = [1,9,3,8,5,7]

for number in my_list:
    print number * 2

---------------

start_list = [5, 3, 1, 2, 4]
square_list = []

# Seu codigo aqui!
for number in start_list:
    square_list.append(number**2)
    square_list.sort()
print square_list
-----------------
# Atribuir um dicionario com tres pares chave-valor para residentes:
residents = {'Fradinho' : 104, 'Preguica' : 105, 'Piton de Burma' : 106}

print residents['Fradinho'] # Exibe o numero do quarto do fradinho
print residents['Preguica'] # Exibe o numero do quarto do Preguica
print residents['Piton de Burma'] # Exibe o numero do quarto do Burma

# Seu codigo aqui!
------------------

menu = {} # Empty dictionary
menu['Frango Alfredo'] = 14.50 # Adicionando um novo par chave-valor
print menu['Frango Alfredo']

# Seu codigo aqui: Adicione alguns pares prato-preco a menu!
menu['Arroz'] = 2.99
menu['Feijão'] = 2.44
menu['Carne'] = 1.44



print "Ha " + str(len(menu)) + " itens no cardapio."
print menu

---------------
# key - animal_name : value - location 
zoo_animals = { 'Unicornio' : 'Casa de Algodao Doce',
'Preguica' : 'Exibicao da Floresta Tropical',
'Tigre de Bengala' : 'Casa da Selva',
'Fradinho do Atlantico' : 'Exibicao Artica',
'Pinguim Saltador da Rocha' : 'Exibicao Artica'}
# Uma declaracao de dicionario (ou lista) pode ocupar mais de uma linha

# Removendo a entrada 'Unicornio'( Unicornios sao incrivelmente caros).
del zoo_animals['Unicornio']

# Seu codigo aqui!
del zoo_animals['Preguica']
del zoo_animals['Tigre de Bengala']
zoo_animals['Pinguim Saltador da Rocha'] = 'Inibido de Pular'

print zoo_animals

-----------------------------
backpack = ['xilofone', 'adaga', 'tenda', 'pedaco de pao']
backpack.remove('adaga')
print backpack

--------------
inventory = {
    'gold' : 500,
    'pouch' : ['silex', 'barbante', 'pedra preciosa'], # Atribuido uma nova lista a chave 'pouch'
    'backpack' : ['xilofone','adaga', 'saco de dormir','pedaco de pao']
}

# Adicionando uma chave 'burlap bag' a atribuindo uma lista a ela
inventory['burlap bag'] = ['maca', 'pequeno rubi', 'bicho preguica']

# Organizando a lista encontrada sob a chave 'pouch'
inventory['pouch'].sort() 

# Seu codigo aqui
inventory ['pocket'] = ['concha', 'amora estranha', 'sujeira']
inventory['backpack'].sort()
inventory['backpack'].remove('adaga')
inventory['gold'] = inventory['gold'] + 50
--------------
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for it in names:
    print len(names)
    print it

-------------
prices{
    "banana": 4,
    "maca": 2,
    "laranja": 1.5,
    "pera": 3,
    "uva": 4.99,
    "melancia": 9.99
}
----------------
prices = {
    "banana": 4,
    "maca": 2,
    "laranja": 1.5,
    "pera": 3,
    "uva": 4.99,
    "melancia": 9.99
}

stock = {
    "banana": 6,
    "maca": 0,
    "laranja": 32,
    "pera": 15,
    "uva": 55,
    "melancia": 77
}

-------------
total = 0
prices = {
    "banana" : 4,
    "maca"  : 2,
    "laranja" : 1.5,
    "pera"   : 3,
}
stock = {
    "banana" : 6,
    "maca"  : 0,
    "laranja" : 32,
    "pera"   : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    total += prices[key] * stock[key]

print total
---------------------
groceries = ["banana","laranja","maca"]

------------------

shopping_list = ["banana", "laranja", "maca"]

stock = {
    "banana": 6,
    "maca": 0,
    "laranja": 32,
    "pera": 15
}
    
prices = {
    "banana": 4,
    "maca": 2,
    "laranja": 1.5,
    "pera": 3
}

# Escreva seu codigo abaixo!
def compute_bill(food):
    total = 0
    for xx in food:
        if (stock[xx] > 0):
          total += prices[xx]
          stock[xx] -= 1
          print total
    return total

#Crie três dicionários: "lloyd", "alice", e "tyler".
#Crie em cada dicionário as chaves "name", "homework", "quizzes", e "tests" (nome, lição de casa, questionários e provas).
#Faça na chave "name" o nome do estudante (isto é, o "name" de "lloyd" deve ser "Lloyd"), e as outras chaves devem ser uma lista vazia (as preencheremos muito em breve!)

#Abaixo do seu código, crie uma lista chamada students que contenha lloyd, alice, e tyler.


lloyd = {
    'name': 'Lloyd',
    'homework':[],
    'quizzes': [],
    'tests': []
}
alice = {
    'name': 'Alice',
    'homework':[],
    'quizzes': [],
    'tests': []

}
tyler = {
    'name': 'Tyler',
    'homework':[],
    'quizzes': [],
    'tests': []
}

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [lloyd,alice ,tyler]


#Crie três dicionários: "lloyd", "alice", e "tyler".
#Crie em cada dicionário as chaves "name", "homework", "quizzes", e "tests" (nome, lição de casa, questionários e provas).
#Faça na chave "name" o nome do estudante (isto é, o "name" de "lloyd" deve ser "Lloyd"), e as outras chaves devem ser uma lista vazia (as preencheremos muito em breve!)

#Abaixo do seu código, crie uma lista chamada students que contenha lloyd, alice, e tyler.

#Para (for) cada aluno (student) em sua lista students, exiba os dados daquele aluno (student), como abaixo:

#    Exiba (print) o nome (name) do aluno (student)
#    Exiba (print) a nota de lição de casa (homework) do aluno (student)
#    Exiba (print) a nota dos questionários (quizzes) do aluno (student)
#    Exiba (print) a nota das provas (tests) do aluno (student)

#Escreva uma função average que toma uma lista de números e retorna a média.

    #Defina uma função chamada average que tem um argumento, numbers.
    #Dentro dessa função, chame a função embutida sum() com a lista numbers como parâmetro. Armazene o resultado em uma variável chamada total.
    #Como no exemplo acima, use float() para converter total e armazenar o resultado em total.
    #Divida total pelo comprimento da lista numbers. Use a função embutida len() para fazer esse cálculo.
    #Retorne esse resultado.

#Escreva uma função chamada get_average que toma o dicionário de estudantes (como lloyd, alice, ou tyler) como entrada e retorna (return) sua media ponderada.

    #Defina uma função chamada get_average que tome um argumento chamado student.
    #Crie uma variável homework que armazene a média (average()) de student["homework"].
    #Repita a etapa 2 para "quizzes" (questionários) e "tests" (provas).
    #Multiplique as 3 médias pelso seus pesos e retorna a soma das três. O peso de lição de casa é 10%, de questionários é 30% e de provas é 60%.


#Defina uma nova função chamada get_letter_grade que tenha um argumento chamado score. Espere que score seja um número.

    #Dentro de sua função, teste score usando uma cadeia de declarações if: / elif: / else: assim:

    #Se score for 90 ou mais: return "A"
    #Ou se score for 80 ou mais: return "B"
    #Ou se score for 70 ou mais: return "C"
    #Ou se score for 60 ou mais: return "D"
    #Caso contrário: return "F"

    #Finalmente, teste sua função! Chame sua função get_letter_grade com o resultado de get_average(lloyd). Exiba a nota no formato de letra.



#Defina uma função chamada get_class_average com um argumento students. você pode esperar que students seja uma lista contendo seus três estudantes.
    #Primeiro, crie uma lista vazia chamada results.
    #Para cada item student na lista class, calcule get_average(student) e então chame results.append() com esse resultado.
    #Finalmente, retorne o resultado de chamar average() com results.



lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [lloyd,alice ,tyler]


for x in students:
    print x["name"]
    print x["homework"]
    print x["quizzes"]
    print x["tests"]


def average(numbers):
    total = float(sum(numbers))
    total = total / len(numbers)
    return total 

def get_average(student):
    homework = (average(student["homework"]))
    quizzes = (average(student["quizzes"]))
    tests = (average(student["tests"]))
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6

def get_letter_grade(score):
    if score >= 90:
      return "A"
    elif score >= 80 and score < 90:
      return "B"
    elif score >= 70 and score <= 80:
      return "C"
    elif score >= 60 and score <= 70:
      return "D" 
    else:
      return "F" 

get_letter_grade(get_average(lloyd)) 
print get_letter_grade(get_average(lloyd)) 

#Defina uma função chamada get_class_average com um argumento students. você pode esperar que students seja uma lista contendo seus três estudantes.
    #Primeiro, crie uma lista vazia chamada results.
    #Para cada item student na lista class, calcule get_average(student) e então chame results.append() com esse resultado.
    #Finalmente, retorne o resultado de chamar average() com results.

def get_class_average(students):    
    results = []
    for x in students:        
        results.append(get_average(x))
    return average(results)


#Escreva uma função chamada string_function que toma um argumento string (s) e então retorna (return) 
 #aquele argumento concatenado com a palavra "mundo". Não adicione um espaço antes de mundo!
n = "Ola"
# Sua funcao aqui!
def string_function(s):
    s = s + "mundo"
    return s
print string_function(n)


#Você passa uma função do mesmo modo que passa qualquer outro argumento para uma função.
def list_function(x):
    return x

n = [3, 5, 7]
print list_function(n)



def get_class_average(students):
    for student in students:
        results = []
        x = get_average(students)
        results.append(x)
        return average(results)

def getclassaverage(students):
results=[]
for student in students:
a = get_average(student)
results.append(a)
return average(results)

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

#Mude list_function de modo que:

  #Some 3 ao item no índice um da lista.
  #Armazene o resultado no índice um.
  #Retorne a lista.

def list_function(x):
    x[1] = x[1] + 3
    return x

n = [3, 5, 7]
print list_function(n)

#Defina uma função chamada list_extender que tenha um parâmetro lst.
#Dentro da função, adicione o número 9 a lst.
#Então, retorne a lista modificada.

def list_extender(lst):
    lst.append(9)
    return lst

#Defina uma função chamada print_list que tenha um argumento chamado x.
#Dentro daquela função, exiba todos os elementos, um por um. Use o código já existente como base.
#Então, chame sua função com o argumento n.
n = [3, 5, 7]
def print_list(x):
  for i in range(0, len(x)):
    print x[i]

print print_list(n)

#Crie uma função chamada double_list que toma um único argumento x (que será uma lista)
  # e multiplique cada elemento por 2 e retorne aquela lista.
  # Use o código já existente como andaime.
n = [3, 5, 7]

for i in range(0, len(n)):
    n[i] = n[i] * 2
# Nao se esqueca de retornar sua nova lista!

print double_list(n)

--------------------------------
Codigo novo
n = [3, 5, 7]
def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
# Nao se esqueca de retornar sua nova lista!
  return x

print double_list(n)


#Na linha 6, substitua o ____ por um range()
#que retorna uma lista contendo [0, 1, 2].

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(0,3))
print my_function(range(2))
print my_function(range(1,2))
print my_function(range(2,3))
print my_function(range(1,3))
print my_function(range(1,3))


#Crie uma função que retorne a soma de uma lista de números.

#Na linha 3, defina uma função chamada total, que aceite um argumento chamado numbers. Ele será uma lista.
#Dentro da função, crie uma variável chamada result, com valor zero.
#Usando um dos dois métodos acima, percorra a lista numbers.
#Adicione cada número a result.
#Finalmente, retorne result.
#Crie uma função chamada total que some todos os elementos de uma lista arbitrária 
#e retorne essa contagem, usando o código já existente como uma dica. 
#Use um laço for para que ela possa ser usada com listas de qualquer tamanho.
n = [3, 5, 7]

def total(numbers):
    result = 0
    for a in range(len(numbers)):
        result = result + numbers[a]
    return result

#Crie uma função que concatene strings.

    #Defina uma função chamada join_strings que aceita um argumento chamado words. ele será uma lista.
    #Dentro da função, crie uma variável chamada result e iguale-a a "", uma string em branco.
    #Percorra a lista wordse adicione cada palavra a result.
    #Finalmente, retorne (return) result.

n = ["Michael", "Lieberman"]
# Adicione sua funcao aqui
def join_strings(words):
    result = ""
    for w in words:
        result = result + w
    return result

print join_strings(n)


from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Vamos jogar Batalha Naval!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Tudo a partir daqui deve ir dentro do laco!
turn = 0
for turn in range(4):
# Tenha certeza de recuar quatro espacos!
        turn = turn + 1
        print turn
        guess_row = int(raw_input("Adivinhe a Linha:"))
        guess_col = int(raw_input("Adivinhe a Coluna:"))

        if guess_row == ship_row and guess_col == ship_col:
            print "Parabens, voce afundou meu couracado!"
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, isso nao e nem mesmo no oceano."
            elif(board[guess_row][guess_col] == "X"):
                print "Joce ja tentou esse."
            else:
                print "Voce errou meu couracado!"
                board[guess_row][guess_col] = "X"
            # Exiba aqui (turn + 1)!
            print_board(board)
 ----------------------------------------------------
 fruits = ['banana', 'maca', 'laranja', 'tomate', 'pera', 'uva']

print 'Voce tem...'
for f in fruits:
    if f == 'tomate':
        print 'O tomate nao e uma fruta!' # (Na verdade, e sim.)
    print 'A', f
else:
    print 'Uma excelente selecao de frutas!'

collors = ['azul', 'verde', 'laranja', 'amarelo', 'preto', 'bege']

for n in collors:
    if n == 'laranja':
        print 'Laranja também é uma fruta'
    print 'As cores escolhidas', n
else:
    print 'Belas cores '



todas as classes censor fazem a mesma coisa.
def censor(text, word):
    sword = text.split()
    for word in sword:
        sword += '*'
        " ".join(sword)
    return sword


def censor(text, word):
    lst = text.split()
    while word in lst:
        index = lst.index(word)
        lst.remove(word)
        lst.insert(index,'*' * len(word))

def censor(text,word):
    text=list(text)

    for n in range(0,len(text)):
        i=0
        while 1==1:
            for i in range(0,len(word)):
                if  text[n+i]==word[i]:
                    i+=1
                else:
                    break
            if i==len(word):
                for m in range(0,i):
                    text[n+m]='*'
            else:
                break
        n+=i
    return "".join(text)

print censor("this hack is wack hack", "hack")

-----------------------------------------------

#Separar Pares e inmpares
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
-----------------------------------------------
#Defina uma função chamada purify que toma uma lista de números, remove todos os números ímpares da lista, e retorna o resultado.

#Por exemplo, purify([1,2,3]) retornaria [2].

#Não modifique diretamente a lista que você recebe como entrada; em vez disso retorne uma nova lista com apenas os número pares.

def purify(lList):
    tList = []
    for x in lList:
        if x % 2 == 0:
            tList.append(x)
    return tList
------------------------------------------------

#Defina uma função chamada product que toma uma lista de inteiros como entrada e retorna o produto de todos os elementos da lista.
#Por exemplo: product([4, 5, 5]) deve retornar 100 (porque 4 * 5 * 5 é 100).
#Não se preocupe se a lista estiver vazia.
#Sua função deve retornar um inteiro.
def product(numbers):
    total = 1
    for each in numbers:
        total *= each
    return total

------------------------------------------------
#Escreva uma função remove_duplicates que toma uma lista e remove da lista elementos que sejam iguais.

#Por exemplo: remove_duplicates([1,1,2,2])
#deve retornar [1,2].

#Não remova todas as ocorrências, já que você precisa manter uma única ocorrência de um número.
#A ordem na qual você apresenta sua saída não importa. Então, retornar [1,2,3] é o mesmo que retornar [3,1,2].
#Não modifique a lista que você toma como entrada! Em vez disso, retorne uam nova lista.

def remove_duplicates(numbers):
    tList = []
    for x in numbers:
        if x not in tList:
            tList.append(x)
    return tList

----------------------------------------------
#A mediana é o valor médio em uma sequência organizada de números.

#Encontrar a mediana de [7,12,3,1,6] deve consistir primeiro de organizar a sequência em [1,3,6,7,12] e então
#localizando o valor no meio, que seria 6.

#Se você tiver uma sequência com um número par de elementos, você deve tirar a média dos dois elementos ao redor do meio.

#Por exemplo, a mediana da sequência [7,3,1,4] é 3.5, já que os elementos médios depois de organizarmos a lista são 3 e 4 e (3 + 4) / (2.0) é 3.5.

#Você pode organizar a sequência usando a função `sorted(), assim:
sorted([5, 2, 3, 1, 4])
       [1, 2, 3, 4, 5]

#Escreva uma função chamada median que tome uma lista como entrada e retorne o valor da mediana da lista.

#Por exemplo: median([1,1,2]) deveria retornar 1.

#A lista pode ter qualquer tamanho e não há garantia de que os números estarão em qualquer ordem em particular.
#Se a lista contiver um número par de elementos, sua função deve retornar a média dos dois elementos do meio.

def median (numbers):
    #numbers = sorted([numbers]) #não funciona aqui
    if len(numbers) % 2 == 0:
        return (sorted(numbers)[(len(numbers) / 2)] + sorted(numbers)[(len(numbers) / 2) - 1] / 2.0)
    else:
        return (round(len(numbers) / 2 + 1))




def median (numbers):
    sNumbers = sorted([numbers]) #4,4,5,5
    if len(numbers) % 2 == 0: #4
        ehPar = len(snumbers) / 2 #2
        return (snumbers[ehPar] + snumbers[ehPar - 1]) / 2.0
        #(numbers[len(numbers) / 2]#2 + numbers[(len(numbers) / 2) + 1]#3 / 2.0)
    else:
        return snumbers[ehPar]



def median (numbers):
    numbers = sorted([numbers]) #4,4,5,5
    if len(numbers) % 2 == 0: #4
        ehPar = len(numbers) / 2 #2
        nTemp = numbers[ehPar] + numbers[ehPar +1]
        nTemp += nTemp / 2.0
        return nTemp
        #(numbers[len(numbers) / 2]#2 + numbers[(len(numbers) / 2) + 1]#3 / 2.0)
    else:
        return (round(len(numbers) / 2 - 1))



def median (numbers):
    sNumbers = sorted([numbers]) #4,4,5,5
    if len(numbers) % 2 == 0: #4
        return str(sNumbers[len(sNumbers) / 2] + sNumbers[(len(sNumbers) / 2) - 1]) / 2.0
    else:
        return str(round(len(sNumbers) / 2 +1))

def median (p):
    if len(p)%2==0:
        return  (sorted(p)[(len(p)+1)/2] + sorted(p)[(len(p)-1)/2]) /2.0
    return sorted(p)[len(p)/2]
--------------------------

#Defina uma função na linha 3 chamada print_grades() com um argumento, uma lista chamada grades.
#Dentro da função, percorra grades e exiba cada item em uma linha separada.
#Depois da sua função, chame print_grades() com a lista grades como parâmetro.

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(g):
    for i in g:
        print i

print_grades(grades)


#Na linha 3, defina uma função grades_sum() que faça o seguinte:

#Tome uma lista de notas, scores
#Calcule a soma das notas
#Retorne a coma calculada
#Chame a recém-criada função grades_sum() com a lista de notas e exiba (print) o resultado.

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(g):
    total = 0
    for i in g:
        total = total + i
    return total
print grades_sum(grades)



#Defina uma função grades_average(), abaixo da função grades_sum() que faça o seguinte:

#Tenha um argumento, grades, uma lista
#Chame grades_sum com grades
#Calcule a média das notas dividindo essa soma por float(len(grades)).
#Retorne a média.
#Chame a recém-criada função grades_average() com a lista de notas e exiba o resultado.


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def grades_sum(g):
    total = 0
    for i in g:
        total = total + i
    return total


def grades_average(h):
    return grades_sum(h) / float(len(h))

print grades_average(graqdes)




#Na linha 18, defina uma nova função chamada grades_variance() que aceita um argumento, scores, uma lista.
#Primeiro, crie uma variável average e armazene o resultado da chamada a grades_average(scores).
#A seguir, crie outra variável variance e iguale-a a zero. Nós a usaremos para a soma móvel.
#Para (for) cada nota em scores: Calcule sua diferença ao quadrado: (average - score) ** 2 e some isso a variance.
#Divide the total variance by the number of scores.
#Então, retorne esse resultado.
#Finalmente, depois do código da sua função, exiba (print) grades_variance(grades).
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    variance = 0
    average = grades_average(scores)
    for i in scores:
        variance += (average - i) ** 2
    return variance / float(len(scores))
print grades_variance(grades)

#Defina uma função grades_std_deviation(variance).
#Retorne (return) o resultado de variance ** (1/2)
#Depois da função, crie uma nova variável chamada variance e armazene o resultado da chamada a grades_variance(grades).
#Finalmente, exiba (print) o resultado da chamada a grades_std_deviation(variance).
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    variance = 0
    average = grades_average(scores)
    for i in scores:
        variance += (average - i) ** 2
    return variance / float(len(scores))

def grades_std_deviation(variance):
    return float(variance ** (0.5))

variance = grades_variance(grades)

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)


"""
to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']


O índice padrão de início é 0.
O índice de término padrão é o fim da lista.
O passo padrão é 1.

"""


#Use o fatiamento de lista para exibir (print) todos os elementos ímpares de my_list do início ao fim.
#Omita os índices de início e final. Você precisa especificar apenas um passo (stride).

my_list = range(1, 11) # List of numbers 1 - 10
print my_list[::2]

"""
Um passo negativo percorre a lista da direita para a esquerda.

letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
No exemplo acima, exibimos ['E', 'D', 'C', 'B', 'A'].
"""
#Crie uma variável chamada backwards e iguale-a à versão invertida de my_list.
#Tenha certeza de inverter a lista no editor, percorrendo sua lista com um passo negativo, como no exemplo acima.

my_list = range(1, 11)
backwards = my_list[::-1]
print backwards 

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

#Crie uma lista, to_21, que contem simplesmente os números de 1 a 21, inclusive.
#Crie uma segunda lista, odds, que contém apenas os números ímpares da lista to_21 (1, 3, 5, e assim por diante). Use fatiamento de lista para isso em vez de compreensão de lista.
#Finalmente, crie uma terceira lista middle_third, igual ao terço médio de to_21, de 8 a 14, inclusive.

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14:1]
print odds
print middle_third


------------------------
"""
Funções lambda são definidas usando a seguinte sintaxe:

my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)
Lambdas são úteis quando você precisa de uma função rápida para realizar alguma tarefa para você.

Se você estiver planejando criar uma função que usara repetidas vezes, é melhor usar def e dar um nome a essa função.
"""
#Preencha a primeira parte da função filter com um lambda. O lambda deve garantir que apenas "Python"
#seja retornado pelo filter. 2 Preencha a segunda parte da função filter com languages, a lista a ser filtrada.

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python" ,languages)
-------------------------

#Crie uma lista, squares, que consista dos quadrados dos números 1 a 10. Compreensão de lista pode ser útil aqui!
#Use as expressões filter() e lambda para exibir (print) apenas os quadrados entre 30 e 70 (inclusive).

squares =  [x**2 for x in range(1, 11)]
print filter(lambda x: x>=30 and x<=70, squares)

-------------------------
#Use compreensão de lista para criar uma lista, threes_and_fives, que consiste apenas 
#dos números entre 1 e 15 (inclusive) que são divisíveis por 3e 5.
#exemplo:
#squares = [x**2 for x in range(5)]


threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]


-------------------------

#Fatiamento de Listas
#Ótimo! A seguir: fatiamento de listas.

#str = "ABCDEFGHIJ"
#start, end, stride = 1, 6, 2
#str[start:end:stride]

#A string no editor é misturada de duas maneiras:

#Primeiro, nossa mensagem está de trás para frente;
#Segundo, a letra que queremos é alternada.
#Uma fatiamento de listas para extrair a mensagem e salvá-la em uma variável chamada message.

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
print message

-------------------------

#Expressões Lambda
#Por último mas não menos importante, vamos examinar alguns lambdas.

my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)
#Demos a você outro garbled (um pouco diferente). Organize-o com um filter() e um lambda.
#Crie uma nova variável chamada message.
#Atribua a ela o resultado da chamada de filter() com o lambda apropriado que removerá os "X"s. O segundo argumento será garbled.
#Finalmente, exiba (print) message no console.

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda y:y <> 'X' garbled)
print message

-------------------------

#Apenas um BIT
#Bem-vindo a uma explicação introdutória sobre as operações no nível dos bits em Python!

#As operações no nível dos bits podem parecer um pouco esotéricas e complicadas no começo, mas você vai pegar o jeito delas muito rápido.

#Operações no nível dos bits são operações que manipulam diretamente os bits.
#Em todos os computadores, números são representados por bits, uma série de zeros e uns.
#De fato, tudo nos computadores é representado por bits.
#Esta aula introduzirá as operações binárias básicas e então mostrará o que se pode fazer com elas.

#Operações no nível dos bits muitas vezes tendem a confundir os novos programadores, então não se preocupe se ficar um pouco perdido no começo. 
#Para ser honesto, você não vai ver operações no nível dos bits em programas comuns.
#Entretanto, elas aparecem de vez em quando, e quando isso acontecer, você deve ter uma ideia geral do que está acontecendo.

print 5 >> 4  # Desloca para a Direita
saida 0
print 5 << 1  # Desloca para a Esquerda
saida 10
print 8 & 5   # AND no nível dos bits
saida 0
print 9 | 4   # OR no nível dos bits
saida 13
print 12 ^ 42 # XOR no nível dos bits
saida 38
print ~88     # NOT no nível dos bits
saida -89



#Lição I0: O Sistema Numérico de Base 2
#Quando contamos, geralmente fazemos isso em base 10. Isso significa que cada posição em um número pode ter um de dez valores, 0-9.
#Em binário, contamos em base dois, em que cada posição pode ter um de dois valores: 0 ou 1.
#O padrão de contagem é o mesmo da base 10, exceto quando você "sobe" um valor para uma nova coluna;
#em binário, você deve "subir" o valor sempre que uma casa assume um valor maior do que um (o que acontece quando o valor excede 9 em base 10).

#Por exemplo, os números um e zero são iguais em base 10 e em base 2.
#Mas em base 2, quando você chega ao número 2, você deve "subir" o um, resultando na representação "10".
#Somar um novamente resulta em "11" (3), e somar um novamente resulta em "100" (4).

#Ao contrário da contagem em base 10, em que cada casa decimal representa uma potência de 10, cada casa em um número binário representa uma potência de dois (ou um bit). 
#O bit mais à direita é o bit dos 1s (dois elevado a zero), o bit seguinte é o bit dos 2's (dois elevado à primeira potência), 
#depois 4, 8, 16, 32, e assim por diante.

#O número binário "1010" é 10 na base 2, porque o bit dos 8s e o bit dos 2s estão "ligados":

bit dos 8s  bit dos 4s  bit dos 2s  bit dos 1s
     1               0                1               0
     8       +      0        +      2       +      0  = 10
#Em Python, você pode escrever números em formato binário iniciando o número com "0b".
#Fazendo isso, os números podem ser operados como qualquer outro número!

print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11 #4
print 0b11 * 0b11 #9

-------------------------
#Posso contar até 100!
#Muito bom! Hora de praticar contar em binário.

#Para garantir que você pegou o jeito, preencha o resto dos números até o doze. Não use o método str() ou quaisquer outras funções externas.

#Aqui estão alguns números que é bom saber para prosseguir:

2**0 = 1
2**1 = 2
2**2 = 4
2**3 = 8
2**4 = 16
2**5 = 32
2**6 = 64
2**7 = 128
2**8 = 256
2**9 = 512
2**10 = 1024
#Talvez você reconheça esses números. Você tem um sistema de 32 ou 64 bits? Seu computador tem um disco rígido de 256GD? Computadores pensam em binário!

#Instruções
#Preencha o resto dos números com seus valores binários correspondentes até doze no editor à direita, usando o formato 0bxxx.

um = 0b1
dois = 0b10
tres = 0b11
quatro = 0b100
cinco = 0b101
seis = 0b110
sete = 0b111
oito = 0b1000
nove = 0b1001
dez  = 0b1010
onze = 0b1011
doze = 0b1100
--------------------------------------
#A Função bin()
#Excelente! O maior obstáculo que você deve superar para compreender os operadores no nível dos bits é aprender como contar em base 2. Com, sorte, a lição será mais fácil daqui para frente.

#Há funções Python que podem ajudá-lo com operações no nível dos bits. Para exibir um número em sua forma binária, você pode usar a função bin(). bin() toma como entrada um número inteiro e retorna a representação binária daquele número inteiro em uma string (Tenha em mente que depois de usar a função bin, você não pode mais operar o valor como um número).

#Você também pode representar números nas bases 8 e 16 usando as funções oct() e hex(). (Mas não vamos abordá-las aqui).


#Fornecemos no editor um exemplo da função bin. 
#Vá em frente e use print e bin() para exibir as representações binárias dos números 2 a 5, cada uma em uma linha separada.
print bin(1)
0b1
print bin(2)
0b10
print bin(3)
0b11
print bin(4)
0b100
print bin(5)
0b101
-------------------------------
#Segundo Parâmetro de int()
#O Python tem uma função int() que você já viu algumas vezes antes. Ela por converter uma entrada não-inteira em um número inteiro, assim:

int("42")
# ==> 42
#O que você pode não saber é que a função int na verdade tem um segundo parâmetro opcional.

#int("110", 2)
# ==> 6
#Ao receber uma string que contém um número e a base em que este número está, a função retornará o valor daquele número convertido em base dez.

#Instruções
#No console, há diversos modos diferentes pelos quais você pode usar o segundo parâmetro da função int.

#Na linha 7, use int para exibir (print) na base 10
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Exiba o equivalente decimal do numero binario 11001001.
print int("11001001",2)
--------------------------------
#Deslize para a Esquerda! Deslize para a Direita!
#As próximas duas operações de que vamos falar são as operações de deslocamento de bit para a esquerda e para a direita. Esses operadores funcionam deslocando os bits de um número um número designado de posições.

#O bloco abaixo mostra como esses operadores funcionam no nível dos bits. Note que no diagrama, o deslocamento é sempre positivo:

# Deslocamento de Bit para a Esquerda (<<)
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)

# Deslocamento de Bit para a Direita (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)
#Essas operações são matematicamente equivalentes a uma divisão por 2 arredondada para o menor inteiro mais próximo e multiplicação por 2 (respectivamente), pois sempre que você desloca, mas muitas vezes é mais fácil pensar nisso como deslocar todos os 1s e 0s para a esquerda ou para a direita um número especificado de posições.

#Note que você só pode realizar operações no nível dos bits em números inteiros. Tentar realizá-las em strings ou números de ponto flutuante resultará em uma saída sem sentido!

#Instruções
#Desloque a variável shift_right para a direita duas vezes (>> 2) e desloque a variável shift_left para a esquerda duas vezes (<< 2).
#Tente adivinhar qual será a saída exibida (print) será!
shift_right = 0b1100
shift_left = 0b1

# Seu codigo aqui!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
0b11 == 3
print bin(shift_left)
0b100 == 4
-------------------------------

#Um Pouco Disso e Daquilo
#O operador no nível dos bits AND (&) compara dois número no nível dos bits e retorna um número no qual os bits de cada número são iguais a 1 se os bits 
#correspondentes dos dois núemros são 1. Por exemplo:

     a:   00101010   42
     b:   00001111   15
===================
 a & b:   00001010   10
#Como você pode ver, os bits na 2a e 8a posições são os únicos que são iguais a 1 em a e b, então, a & b contém apenas aqueles bits.
#Note que usar o operador & pode resultar apenas em um número menor ou igual ao menor dos dois valores.

#Então lembre-se, para cada bit em a e b:

0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
#Portanto,

 0b111 (7) & 0b1010 (10) = 0b10
#o que é igual a dois.

#Instruções
#Exiba (print) o resultado de aplicar bin() a 0b1110 & 0b101.

#Veja se você pode adivinhar qual será a saída!
print bin(0b1110 & 0b101)
0b100
-----------------------------------
#Um Pouco Disso OU Daquilo
#O operador em nível dos bits OR (|) compara dois números no nível dos bits e retorna um número no qual os bits sao iguais a 1 se
#qualquer um dos bits correspondentes dos dois números for igual a 1. Por exemplo:

    a:  00101010  42
    b:  00001111  15
================
a | b:  00101111  47
#Note que o operador no nível dos bits | pode gerar apenas resultados que são maiores ou iguais ao maior das duas entradas inteiras.

#Então lembre-se, para cada bit em a e b:

0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1
#O que significa 
110 (6) | 1010 (10) = 1110 (14)

#Instruções
#Para praticar, exiba (print) o resultado de usar | em
 #0b1110 e 0b101
 #como uma string binária. 
 #Tente fazer isso por conta própria sem usar o operador | se puder evitar.
 print bin(0b1111)
----------------------------------------
#Isso XOR Aquilo?

#O operador XOR (^) ou ou exclusivo compara dois números no nível dos bits e retorna um número no qual
#os bits são 1 de um dos bits correspondentes dos dois números for 1, mas não os dois.

    a:  00101010   42
    b:  00001111   15
================
a ^ b:  00100101   37
#Tenha em mente que se um bit for 0 nos dois números, o resultado será 0. 
#Note que usar XOR em um número com ele mesmo sempre resultará em 0.

#Então, lembre-se, para cada bit em a e b:

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
#Portanto:

 111 (7) ^ 1010 (10) = 1101 (13)
#Instruções
#Para praticar, exiba (print) o resultado de usar ^ em 0b1110 e 0b101 como uma string binária.
#Tente fazer isso por conta própria, sem usar o operador ^.
0b1110
0b 101
0b1011

print bin(0b1011)
-----------------------------------------
#Viu? Não é TÃO Difícil!
#O operado no nível dos bits NOT (~) simplesmente inverte os bits em um único número.
#O que isso significa para o computador, na verdade, muito complicado, então não vamos falar disso.
#Saiba apenas que matematicamente isso é equivalente a somar 1 ao número e então torná-lo negativo.

#E assim, você viu todos os operadores básicos no nível dos bit! Vamos ver o que podemos fazer com eles na próxima seção.

#Instruções
#Clique em Salvar e Enviar Código e observe o que o console exibe.
print ~1
-2
print ~2
-3
print ~3
-4
print ~42
-43
print ~123
-124
----------------------------------------
#O Homem Por Trás da Máscara de Bits
#Uma máscara de bits é apenas uma variável que ajuda você com operações no nível dos bits.
#Uma máscara de bits pode ajudá-lo a ativar alguns bits, desativar outros, ou apenas coletar dados sobre quais bits estão ativados ou desativado
#em um número inteiro.

num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
    print "O bit estava ativado"
#No exemplo acima, queremos saber se o terceiro bit a partir da direita está ativo.

#Primeiro, criamos uma variável num, contendo o número 12, ou 0b1100.
#Depois, criamos uma máscara (mask) com o terceiro bit ativado.
#Então, usamos uma operação and no nível dos bits para ver se o terceiro bit a partir da direita de num está ativo.
#Se desired for maior do que zero, então o terceiro bit de num deve ser um.

#Instruções
#Defina uma função, check_bit4, com um argumento input, um inteiro.
#Ela deve verificar se o quarto bit a partir da direita está ativo.
#Se o bit estiver ativo, retorne (return) "ativo"(não useprint`!)
#If the bit is off, return "off".
#Leia a Dica para ver alguns exemplos!

def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "ativo"
    return "inativo"
---------------------------------------------------
#Ativando
#Você também pode usar máscaras para inverter um bit em um número usando |.
#Por exemplo, digamos que queremos garantir que bit mais à direita do número a esteja ativo.
#Eu poderia fazer isso:

a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7

#Usar o operador no nível dos bits | ativará o bit correspondente se ele estiver inativo e o deixará como está se ele já estiver ativo.

#Instruções
#Há no editor uma variável, a.
#Use uma máscara de bits e o valor a para atingir um resultado em que o terceiro bit a partir da direita está ativo.
#Tenha certeza de exibir (print) sua resposta como uma string bin()!
a = 0b10111011
mask = 0b100
desired = a | mask
print bin(desired)
------------------------------------------------------
#É Só Inverter
#Usar o operador XOR (^) é muito útil para inverter bits.
#Usar ^ em um bit com o número um retornará um resultado em que aquele bit está invertido.

#Por exemplo, digamos que eu quero inverter todos os bits em a. Eu poderia fazer isso:

a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1

#Instruções
#Há no editor uma variável de 8 bits a.
#Use uma máscara de bits e o valor a para alcançar um resultado em que todos os bits em a sejam invertidos.
#Tenha certeza de exibir sua resposta como uma string bin()!
a = 0b11101110
print(bin(a ^ 0b11111111))
-----------------------------------------------------------
#Escorregar e Deslizar
#Finalmente, você pode também usar os operadores deslocamento para a esquerda (<<) e para a direita (>>) para colocar as máscaras na posição.

a = 0b101
# Mas cara no decimo bit
mask = (0b1 << 9)  # Um a menos do que dez
desired = a ^ mask
#Digamos que eu queira inverter o 10o bit a partir da direita do inteiro a.

#Em vez de escrever o número inteiro, deslizamos um bit usando o operador <<.

#Usamos 9 porque precisamos apenas deslizar a máscara nove posições a partir do primeiro bit para atingir o décimo bit.

#Instruções
#Defina uma função chamada flip_bit que toma as entradas (number, n).
#Inverta o n-ésimo bit (Com o bit menso significativo sendo o primeiro bit) e armazene-o em result.
#Retorne o resultado de bin(result).
def flip_bit(number, n):
    mask = 0b1 << (n - 1)
    desired = number ^ mask
    return bin(desired)
--------------------------------------------
#Por Que Usar Classes?
#O Python é uma linguagem de programação orientada a objetos, o que significa que ela manipula construtos de programação chamados objetos. Você pode pensar em um objeto como uma estrutura de dados única que contém dados, além de funções; funções de objetos são chamadas métodos. Por exemplo, sempre que você usa

len("Eric")
#O Python está verificando se o objeto string que você passou tem um comprimento, e se tiver, retorna o valor associado a esse atributo. Quando você chama

my_dict.items()
#O Python verifica semy_dict tem um método items() (que todos os dicionários têm) e executa esse método se o encontrar.

#Mas o que faz de "Eric" uma string e de my_dict um dicionário? O fato de que eles são instâncias das classes str e dict, respectivamente. Uma classe é apenas um modo de organizar e produzir objetos com atributos e métodos similares.

#Instruções
#Verifique o código no editor à direita. Nós definimos nossa própria classe, Fruit e criamos uma instância lemon.

#Quando estiver pronto, clique em Salvar e Enviar Código para começar a criar classes e objetos próprios.


class Fruit(object):
    """Uma classe que cria muitas frutas deliciosas."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "Sou uma %s %s e meu sabor e %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Sim! Sou comestivel."
        else:
            print "Nao me coma! Sou super venenoso(a)."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()
--------------------------------------------
#Classes de Mais Classe
#Queremos que nossas classes façam mais do que... bem, nada, então temos que substituir pass por alguma coisa.

#Você pode ter notado em nosso exemplo do primeiro exercício que começamos nossa definição de classe com uma função um pouco estranha: __init__().
#Esta função é necessária para classes, e é usada para inicializar os objetos que cria. __init__() sempre toma pelo menos um argumento, self, que referencia o objeto sendo criado.
#Você pode em __init__() como a função que "inicializa" cada objeto que a classe cria.

#Instruções
#Remova a declaração pass em sua definição class, então avance e defina uma função __init__() para sua classe Animal.
#Por hora, passe-lhe o argumento self; vamos explicar como isso funciona em mais detalhes na próxima seção.
#Finalmente, coloque pass no corpo da definição de __init__(), já que se espera que esse seja um bloco recuado.
class Animal(object):
    def __init__(self):
        pass
------------------------------------------
#Não Vamos Ser Muito Egoístas
#Excelente! Vamos fazer mais um ajuste em nossa definição de classe, então avançar e instanciar (criar) nosso primeiro objeto.

#Até agora, __init__() toma apenas um parâmetro: self. Isto é uma convenção do Python; não há nada de mágico na palavra self.
#Entretanto, é extremamente comum usar self como primeiro parâmetro em __init__(), então você deve fazer isso, para que outras pessoas entendam seu código.

#A parte que é mágica é o fato de que self é o primeiro parâmetro passado para __init__().
#O Python usará o primeiro parâmetro que __init__() recebe para se referir ao objeto sendo criado; é por isso que muitas vezes ele é chamado self ("eu mesmo", em tradução livre),
#já que este parâmetro dá ao objeto sendo criado sua identidade.

#Instruções
#Vamos fazer duas coisas no editor:

#Forneça a __init__() um segundo parâmetro, name.
#No corpo de __init__(), deixe a função saber que name se refere ao nome do objeto criado digitando self.name = name. (Isso ficará claro como água na próxima seção).
class Animal(object):
    def __init__(self,name):
        self.name = name
------------------------------------------
#Instanciando seu Primeiro Objeto
#Perfeito! Agora estamos prontos para começar a criar objetos.

#Podemos acessar os atributos de nossos objetos usando notação de ponto. Eis como isso funciona:

class Square(object):
  def __init__(self):
    self.sides = 4

my_shape = Square()
print my_shape.sides

#Primeiro, criamos uma classe chamada Square com um atributo sides.
#Fora da definição de classe, criamos uma nova instância de Square chamada my_shape e acessamos esse atributo usando my_shape.sides.

#Instruções
#Fora da definição da classe Animal, crie uma variável chamada zebra e iguale-a a Animal("Jeffrey").
#Então, exiba (print) o nome de zebra.

class Animal(object):
    def __init__(self,name):
        self.name = name
zebra = Animal("Jeffrey")
print zebra.name
---------------------------------------
#Mais sobre __init__() e self
#Agora que você está começando a entender como as classes e objetos funcionam, vale a pena nos aprofundarmos um pouco mais em __init__() e self. Eles podem ser confusos!

#Como mencionado, você pode pensar em __init__() como o método que "inicializa" o objeto instância de uma classe: init é uma abreviação de "initialize" ("inicializar").

#O primeiro argumento que __init__() recebe é usado para referenciar o objeto instância, e por convenção, esse argumento é chamado self.
#Se você adicionou argumentos adicionais — por exemplo, um nome (name) e idade (age) para seu animal — igualar os dois,
#respectivamente, a self.name e self.age no corpo de __init__() fará com que quando você criar um objeto instância da sua classe Animal, você deva dar a cada instância um nome e uma idade, e estas serão associadas com a instância em particular que você criou.

#Instruções
#Leia os exemplos no editor.
#Percebe como __init__() "inicializa" cada objeto de modo que ele espere um nome e uma idade, então usa self.name e self.age para atribuir esses nomes e idades a cada objeto?
#Adicione um terceiro atributo, is_hungry a __init__(), e clique em Salvar e Enviar Código para ver os resultados.
# Definicao da classe

class Animal(object):
    """Cria animais bonitinhos."""
    # Para inicializar nossas instancias de objetos
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry


# Note que self e usado apenas na definicao da funcao
# __init__(); nao quereomos passa-lo
# para nossas sinstancias de objetos.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry
-----------------------------------------
#Escopo da Classe
#Outro aspecto importante das classes do Python é o escopo. O escopo de uma variável é o contexto no qual ela é visível para o programa.

#Você pode ficar surpreso em saber que nem todas as variáveis são acessíveis a todas as partes de um programa Python a todo momento.
#Quando lidamos com classes, você pode ter variáveis visíveis o tempo todo (variáveis globais),
#variáveis que estão disponíveis apenas a membros de certas classes (variáveis membro) e variáveis que são disponíveis apenas a instâncias particulares de uma classe (variáveis instância).

#O mesmo vale para as funções: algumas estão disponíveis para todos, outras estão disponíveis apenas para membros de certas classes, e outras estão disponíveis apenas a certos objetos instância.

#Instruções
#Verifique o código no editor. Note que cada animal tem seu próprio nome (name) e idade (age) (já que eles são todos inicializados individualmente),
#mas todos têm acessos à variável membro is_alive, já que todos são membros da classe Animal. Clique em Salvar e Enviar Código para ver o resultado!
class Animal(object):
    """Cria animais bonitinhos."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive
Result:
Jeffrey 2 True
Bruce 1 True
Chad 7 True
----------------------------------
#Uma Abordagem Metódica
#Quando uma classe tem suas próprias funções, elas são chamadas métodos. Você já viu um deles: __init__().
#Mas você pode definir os seus próprios métodos!

#Instruções
#Adicione um método, description à sua classe Animal. Usando duas declarações print separadas, ele deve exibir o nome (name) e idade (age) do animal para o qual ele é chamado.
#Então, crie uma instância de Animal, hippo (com quaisquer nome e idade que quiser), e chame seu método description.
class Animal(object):
    """Cria animais bonitinhos."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print self.name
        print self.age

hippo = Animal("Lontra Feiosa", 8)
hippo.description
----------------------------------
#Eles Estão se Multiplicando!
#Uma classe pode ter qualquer número de variáveis membro. Essas são variáveis disponíveis a todos os membros de uma classe A.

hippo = Animal("Jake", 12)
cat = Animal("Boots", 3)
print hippo.is_alive
hippo.is_alive = False
print hippo.is_alive
print cat.is_alive

#No exemplo acima, criamos duas instâncias de Animal.
#Então, exibimos True, o valor padrão na variável membro is_alive do hipopótamo (hippo).
#A seguir, igualamos isso a False e o exibimos para garantir.
#Finalmente, exibimos True, o valor armazenado na variável membro is_alive do gato (cat). Apenas mudamos a variável em hippo, não em cat.
#Vamos adicionar outra variável membro a Animal.

#Instruções
#Depois da linha 3, adicione uma variável membro chamada health que contém a string "boa".
#Então, crie dois novos animais (Animals): sloth e ocelot. (Dê-lhes quaisquer nomes e idades que quiser).
#Finalmente, exiba (print) a saúde (health) de hippo, sloth, e ocelot em três linhas separadas.

class Animal(object):
    """Cria animais bonitinhos."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print self.name
        print self.age

hippo = Animal("Lontra Feiosa", 8)
hippo.description