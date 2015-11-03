#Tuto parte 1: Data types
#-------------------------------------------------------------
print('--------------------------------------------------')
print('TUTO1 Data types. Elemental operations.')
print('--------------------------------------------------')
x=3
print type(x)			#Imprime el tipo de dato
print x				#Imprime x
print x+1			#Imprime SUMA X+1
print x-1			#Imprimxe RESTA X-1
print x*2			#Imprime PRODUCTO x*2
print x ** 2			#Imprime EXPONENCIAl x ^ 2
x+=1				#Incrementa x en uno
print x
x*=2				#Multiplica x por 2
print x
y=2.5
print type(y)
print y, y+1, y*2, y**2 	#Imprime y+1, y*2, y**2
#-------------------------------------------------
#OPEARCIONES BASICAS OPERANDOS:
#+, -, *, **, /, type,
#
#
#-------------------------------------------------

print ('--------------BOOLS-------------------------')
t=True
f=False
print type(t)			#Imprime el tipo de dato
print t and f			# t AND f
print t or f			# t OR f
print not t			# NOT t
print t!=f			# t XOR f

print ('--------------CHARS-------------------------')
hello = 'hello'
world = 'world'
print hello			#Imrpime variable CHARS hello
print len(hello)		#DA LONITUD cadena CHARS
hw=hello+''+world		#CONCATENA 2 chars

s='hello'
print s.capitalize()		#Primera letr en MAY
print s.upper()			#MAYUSCULAS toda la cadena
print s.rjust(7)		#JUSTIFICACION DERECHA
print s.center(7)		#JUSTIFICACION CENTRAL	
print s.replace('l', '(ell)')	#REPLACE l=ell en la cadena
print '        world       '.strip()

#-------------------------------------------------
#OPERACIONES BASICAS CON STRINGS:
#len, type, capitalize, upper, rjust, center, replace...
#
#--------------------------------------------------------------------------------------------


#Tuto parte 2: CONTAINERS: LISTS
#-------------------------------------------------------------
print('--------------------------------------------------')
print('TUTO2 CONTAINERS: LISTS')
print('--------------------------------------------------')
#LISTS is like an Array. But resizable and can contain elements of diferent types.
#Como un Array pero de 1D
xs = [3, 1, 2]			#crea lista de 3 elementos
print xs, xs[2]			#Imprime toda la lista y el segundo #elemento
print xs[-1]			#Indice negativo Va restando a elemento0
xs[2]='foo'			#carga 2ndo elemetno con valor foo
print xs
#Falta ejemplo append
x=xs.pop()			#REMUEVE el ultimo elemento de la lista
print x, xs
#Falta ejemplo anadir

print ('--------------ACCESO A DATOS en LISTAS::-------------------------')
nums = range(5)			#RANGE=crea lista integers
print nums			#[0,1,2,3,4]
print nums [2:4]		#Del 2 al 4 = [2,3]
print nums [2: ]		#Del 2 al FINAL = [2,3,4]
print nums [ :2]		#Del INICIO al 2 = [0,1]
print nums [ : ]		#Todo = [0,1,2,3,4]
print nums [ :-1]		#del inicio al -1 (ultimo elemento)= [0,1,2,3]
nums[2:4]=[8,9]			#Del 2 al 4 carga con valor 8 y 9 (2 y 3 escribe)
print nums			# =[0,1,8,9,4]

print ('--------------ACCESO A DATOS: LOOPS en LISTAS::-------------------------')
#Acceso BASICO
animals = ['cat', 'dog', 'monkey']		
for animal in animals:
	print animal
#Prints CAT, DOG, MONKEY in diferent lines

#Acceso mostrando posicion
animals
animals = ['cat', 'dog', 'monkey']		
for idx, animal in enumerate(animals):
	print '#%d: %s' % (idx+1, animal)
#prints: "#1:Cat, #2:Dog, #3:Monkey"

#Acceso, operando y escribiendo en otra LISTA
nums = [0,1,2,3,4]				#Carga LISTA
squares=[]					#Crea LISTA vacia
for x in nums:		
	squares.append(x**2)			#con Append anade la potencia del valor concreto de la lista (nums) y los va grabando en lista (Squares)
print squares


#Otra manera de hacer lo mismo:
squares=[x**2 for x in nums]
print squares
#prints [0,1,4,9,16]

#-------------------------------------------------
#SI INCLUYE EL PRIMER ELEMENTO, NO EL ULTIMO
#OPERACIONES CON LISTS Y ACCESO A DATOS DE LIST
#[I,F]  I=Inicio (inclusive), F=Final(NO lo anade)
#enumerate, append
#--------------------------------------------------------------------------------------------


#Tuto parte 3: CONTAINERS: DICTIONARIES
#-------------------------------------------------------------
print('--------------------------------------------------')
print('TUTO3 CONTAINERS: DICTIONARIES')
print('--------------------------------------------------')
#Stores: (KEY, VALUE) PAIRS!!

d={'cat': 'cute', 'dog':'furry'}		#Carga diccionario
print d['cat']					#Iprime VALUE de KEY CAT
print 'cat' in d			#Comprueba si hay KEY=cat en Diction.
d['fish']='wet'				#Anade KEY fish con VALUE wet
print d['fish']				#Imprime VALUE de KEY fish
print d.get('monkey', 'N/A')		#Obtiene VALUE de KEY Monkey. si no esta imprime NA		
print d.get('fish', 'N/A')		#Obtiene VALUE de KEY Fish. si no esta imprime NA		
del d['fish']			#Remueve elemento con KEY = fish
print d.get ('fish', 'N/A')	#Obtiene VALUE de KEY Fish. si no esta imprime NA		

print ('--------------ACCESO A DATOS: LOOPS en DICTIONARIES::-------------------------')

#Acceso basico escribiendo variable con contenido del Dictionary
d={'person':2, 'cat':4, 'spider':8}
for animal in d:
	legs=d[animal]
	print 'A %s has %d legs' % (animal, legs)
#prints: "A person has 2 legs, A spider has 8 legs, A cat has 4 legs" in different lines

#Acceso usando: ITERITEMS
d={'person':2, 'cat':4, 'spider':8}
for animal, legs in d.iteritems():
	print 'A %s has %d legs' % (animal, legs)
#prints: "A person has 2 legs, A spider has 8 legs, A cat has 4 legs" in different lines


#Acceso, operando y escribiendo en dictionaries
nums = [0,1,2,3,4]
even_num_to_square = {x: x**2 for x in nums if x % 2 == 0}
print even_num_to_square
#Prints {0:0, 2:4, 4:16}

#-------------------------------------------------
#OPERACIONES CON DICTIONARIES 
#get, del, 
#iteritems
#
#--------------------------------------------------------------------------------------------


#Tuto parte 4: CONTAINERS: SETS
#-------------------------------------------------------------
print('--------------------------------------------------')
print('TUTO4 CONTAINERS: SETS')
print('--------------------------------------------------')
#Coleccion de distintos elementos. (Como List pero mezclando elementos)

animals={'cat','dog'}		#Carga SET	
print 'cat' in animals		#Comprueba si existe elemento cat (devuelve True o False)
print 'fish' in animals		#Comprueba si existe elemento fish
animals.add('fish')		#ANADE fish
print 'fish' in animals		#Comprueba si existe elmento fish
print len(animals)		#Imprime longitud del SET animals
animals.add('cat')		#ANADE elemento que ya existia
print len(animals)		#La longitud es igual, ya existia, no anade
animals.remove('cat')		#BORRA  elemento cat
print len(animals)

print ('--------------ACCESO A DATOS: LOOPS en SETS::-------------------------')

#Acceso basico
animals={'cat','dog','fish'}	
for idx, animal in enumerate(animals):
	print '#%d: %s' % (idx+1,animal)
#prints "#1:fish, #2:dog, #3:cat'


from math import sqrt
nums={int(sqrt(x)) for x in range(30)}
print nums

#-------------------------------------------------
#OPERACIONES CON SETS 
#len, enumerate, 
#
#--------------------------------------------------------------------------------------------


#Tuto parte 5: FUNCTIONS
#-------------------------------------------------------------
print('--------------------------------------------------')
print('TUTO5 FUNCTIONS')
print('--------------------------------------------------')
#Uso de funciones en Python
#se declaran usando el keyword "def"
def sign (x):				#Define funcion
	if x > 0:
		return 'positive'
	if x < 0:
		return 'negative'
	else:
		return 'zero'

for x in [-1, 0, 1]:			#Da valores(-1,0,-1) a funcion e imprime
	print sign(x)
#prints "negative, zero, positive"


def hello(name, loud=False):		#Define funcion
	if loud:
		print 'HELLO, %s' % name.upper()
	else:
		print 'HELLO, %s!' % name
hello('Bob')				#LLama a funcion con name=Bob
hello('Fred', loud=True)		#LLama a funcion con name=Fred y loud=True
#Prints: HELLO, Bob!, Hello Fred


#Tuto parte 6: CLASSES
#-------------------------------------------------------------
#print('--------------------------------------------------')
#print('TUTO6 CLASSES')
#print('--------------------------------------------------')
#Uso de clases en Python
#class Greeter:
	#Constructor
#		def __init__(self, name):
#		self.name = name 		

	#Instance Method
#		def greet(self, loud=False)
#			if loud:
#				print 'HELLO %s!' %self.name.upper()
#			else:
#				print 'Hello, %s' % self.name
#	g=Greeter('Freed')	
#	g.greet()
#	g.greet(loud=true)
#--------------------------------------------------------------------------------------------


##Tuto parte 7: NUMPY
#-------------------------------------------------------------
print('--------------------------------------------------')
print('TUTO 7:NUMPY')
print('--------------------------------------------------')
#scientific computing in Pyhton.High performance multidimensional array objects
#number of dimensions = RANK of Array
#Shape = TUPLE of integers giving the SIZE of the array along each dimension

import numpy as np
a=np.array([1,2,3])		#Crea array RANK 1
print type(a)			#Imprime el tipo
print a.shape			#Imprime Shapes (n de elementos, len)..
print a[0], a[1], a[2]		#Imprime el valor de sus posiciones 0,1,2
a[0]=5				#Carga valor. a[0]=5
print a				#Imprime todo el array

print ('--------------FUnciones para crear ARRAYS-------------------------')
a=np.zeros((2,2))		#Array full of zeros (2filas, 2 col)
print a
b=np.ones((1,2))		#Array full of ones (1fila, 2col)
print b
c=np.full((2,2),7)		#Array con todo valor 7 (2filas, 2cols)
print c
d=np.eye(2)			#Array identitario (2filas, 2 cols)
print d
e=np.random.random((2,2))	#Array con valores aleatorios (2filas, 2 cols)
print e

print ('--------------ARRAY Indexing-------------------------')
print ('SLICING!!!')
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print a
#[1 2 3 4   ]
#[5 6 7 8   ]
#[9 10 11 12]

print ('Slicing para sacar de las 2 primeras filas las columnas 1 y 2')
b=a[ :2 , 1:3]		# [ ,2]= de la fila 0 a la 2 (filas o y 1). 2 no Inclusive
print b			# [1,3]= de la columna 1 a la 3 (cols 1 y 2). 3 no inclusive
#[2 3]
#[6 7]

print('Slicing para sacar los dos ultimos elementos de las 2 ultimas filas')
b2=a[ 1:3, 2: ]		# [1,3]= de la fila 1 a la 3 (filas 1 y 2). 3 no Inclusive
print b2		# [2, ]= de la columna 2 a Fin (cols 2 y 3). Fin(3)Inclusive
#[7,8]
#[11,12]

print('Slicing para sacar los dos primeros elementos de las 2 primeras filas')
b3=a[ :2, :2 ]		# [1,3]= de la fila 1 a la 3 (filas 1 y 2). 3 no Inclusive
print b3		# [2, ]= de la columna 2 a Fin (cols 2 y 3). Fin(3)Inclusive
#[1 2]
#[5 6]

print('Slicing2 para sacar los dos primeros elementos de las 2 primeras filas')
b4=a[1:3, 1:3 ]		# [1,3]= de la fila 1 a la 3 (filas 1 y 2). 3 no Inclusive
print b4		# [2, ]= de la columna 2 a Fin (cols 2 y 3). Fin(3)Inclusive




#SI INCLUYE EL PRIMER ELEMENTO, NO EL ULTIMO
#-------------------------------------------------
#OPERACIONES CON ARRAYS y ACCESO A DATOS DE LIST
#[Fi:Ff, Ci:Cf]  Fi=Filera inicio, F=Filera fin (no inclusive), Ci=Col.Inicio, Cc=Col.Fin (No inclusive)
#--------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------









































 




















