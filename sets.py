#Sets

sets.py

includes a data type for sets,
Curly braces or the set() function can be used to create sets,

basket = {'apple','orange','apple','pear','orange','banana'}
print(basket) 			#show that dupication have been removed

'ornage' in basket 				#fast membership testing 
'crabgrass' in basket 

Demostrate set operation on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a 								#unique letters in a 
a - b 							#letters in a but not in b
a | b 							#letters in a or b or both 
a & b 							#letters in both a and b
a ^ b 							#letters in a or b but not both 

x = set('23802348')
y = set('57839012')
x-y 
y-x
x * y
y | x
x & y 
x

a = {x for x in 'abracadabra' if x not in 'abc'}
a 

-------------

fruits = {'apple', 'banana', 'cherry', 'orange', 'kiwi','malon', 'mango'}
print ('cherry' in fruits)
fruits.add('cucumber')
fruits.update('grape')
frutis.remove('banana')
fruits.discard('kiwi')

>>>Dictionaries 
#Dictionaries 
#Another useful data type built into python is dictionary 


dict([('Mani', 11), ('Mgphyu', 22), ('Jack', 33)])

{x: x**5 for x in (10,20,30,50)}
{10: 100000, 20: 3200000, 30: 24300000, 50: 312500000}

for x  in 2,4,6:
...     print(x,x**2)
...
2 4
4 16
6 36


 knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k,v in knoghts.itemss():
...     print(k,v)

 for i,v in enumerate (['tic', 'tac', 'toe']):
...     print(i,v)
...
0 tic
1 tac
2 toe

