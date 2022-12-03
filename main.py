##Asignacion Multiple
#x,y = 1,2
#print(x,y)

## .FORMAT
#texto= input("Introduzca un texto: ")
#num= input("introduzca un numero: ")
#print("Un texto {t} y un numero {n}".format(n=num,t=texto))

#print( "{:^20}".format("palabra"))

#print("{:04d}".format(10))
#print("{:04d}".format(100))
#print("{:04d}".format(1000))

##BOOLEANOS (sin condicionales ni logicos no tienen mucho sentido)

#estaLoviendo=True
#estaHaciendoSol=False
#print(estaLoviendo)
#print(estaHaciendoSol)
#print(True * 3) #como vemos aqui la representacion aritmetica de True equivale a 1
#print(False * 1) # la representacion aritmetica de False es 0
#print(True * False)

##Operadores Logicos (sin condicionales no tienen mucho sentido)

# NOT = dice lo contrario de lo que es, es una negacion logica o como un cambio de sentido
#print(not True)
#print(not False)
#print(not True == False)

# AND es la conjuncion logica, es el 'y' logico ej: SI llueve y SI hace frio...(se dan las 2 cosas)

#print(True and True)
#print(False and True)
#print(False and False)
#a = 45
#a > 10 and < 20)# va
#c = "Hola Mundo"
#print(len(c) >= 20 and c[0] =="H")

# OR es lo contrario, en el momento que haya algo positivo o True, todo el conjunto es True.
#print (True or True)
#print(True or False)
#print(False or False)

##CAMBIANDO TIPOS DE VARIABLES
#Convertir variables de un tipo a otro se denomina CASTING, podemoscomprobar el timpo de una variable mediante la funcion type(), o bien mediante la funcion isInstance().

#a = 2.0
#b = 2
#print(type(a))
#print(type(b))

#print(isinstance(a,float))
#print(isinstance(a,int))
#print(isinstance(b,float))
#print(isinstance(b,int))

# Otras funciones que nos puede ayudar son:

#print(max(1,5,8,7))

#print(min(-1,1,0))

## LISTAS

# para añadir elementos al final de una lista utilizamos el metodo .append() .Nunca elimina informacion, pero el problema que tiene append es que si son varios elementos los añade como una sublista dentro de la lista.
#pares = [0,2,4,106,8,10]
#pares.append(12)
#print(pares)
#pares.append(7*2)
#print(pares)

# ahora si queres añadir elementos en la posicion que nosotros queramos tenemos la funcion .insert() .Nunca elimina informacion sino que va a la posicion que le indico y añade el elemento que establecemos.IMPORTANTE nosotros le decimos la posicion concreta:
#pares = [0,2,4,106,8,10]
#pares.insert(3,21)
#print(pares)

# tambien permite modificacion a traves del SLICING:

#nums=[10,20,30,40,50]
#print(nums)
#nums[0]=100
#print(nums)
#nums[1:3]=[200,300] #con esto le damos el rango apropiado para modificar las posiciones 1 y 2.
#print(nums)
#nums[1]= [666,777] #podemos añadir una lista y anidamos dentro.
#print(nums)

# y una peculiaridad, es que tambien aceptan ASIGNACION con Slicing para modificar varios items en conjunto:

#letras = ['a','b','c','d','e','f']
#print(letras[0:3]) #aqui le decimos que imprima el comienzo hasta la posicion 3
#letras[:3] = ['A','B','C']
#print(letras)

# y si queremso eliminar objetos de la lista podemos hacerlo de la siguiente manera:
#letras= ['a','b','c','d','e','f']
#letras = ["d","e","f"]
#print(letras)

# para poder determinar si un elemento se encuentra dentro de la lista o no,este operador "IN" es miuy simple y devuelve un TRUE o un FALSE, solo si esta en la lista o no independientemente de la cantidad:
#pares=[0,2,4,6,8,10,12,14]
#print (2 in pares)
#print (7 in pares)

# Listas dentro de listas (ANIDADAS)..

#a=[1,2,3]
#b=[4,5,6]
#c=[7,8,9]
#r=[a,b,c]
#print(r)

#print(r[0]) #primera sublista, no devuele un argumento simple sino que nos devuelve toda una lista
#print(r[-1]) #ultima sublista
#print(r[0][0]) #primera sublista, y de ella, primer item
#print(r[0][1]) #primera sublista, y de ella, segundo item
#print(r[0][2]) #primera sublista, y de ella, tercer item
#print(r[-1][-1]) #ultima sublista, y de ella, ultimo item

# y esto es un ejemplo de lo que se puede hacer en listas anidadas:
#nombres=["Cristian","Eva","Carlos"]
#edades=[20,30,50]
#alumnos=[nombres,edades]
#print(alumnos)
#print("El alumno", alumnos[0][0], "tiene",alumnos[1][1],"años")

##  TUPLAS
# Se trabaja exactamente igual que con las listas pero la unica diferencia es que son inmutables (no se puede modificar su contenido)

#numeros=(1,2,3,4)
#print(numeros)
#numeros=numeros + (5,6,7,8)
#print(numeros)

# A diferencia de las listas, no podemos modificar nada y por eso no integra el metodo .append() para añadir items al final de la lista.
# Tampoco acepta la asignacion con slicing para modificar varios items en conjunto.
# Si deja utiliar la bsuqueda con in y tambien utilizar len, y por supuesto tambien podemos anidar tuplas dentro de tuplas.

#a=(1,2,3)
#b=(4,5,6)
#c=(7,8,9)
#r=(a,b,c)

#print(r)
#print(r[0]) #primera subtupla
#print(r[-1]) #ultima subtupla
#print(r[0][0]) #primera subtupla, y de ella, el primer item
#print(r[1][1]) #segunda subtupla, y de ella, el segundo item
#print(r[2][2]) #tercera subtupla, y de ella, el tercer item
#print(r[-1][-1]) #ultima subtupla, y de ella, el ultimo item

## CONJUNTO
# Tipo compuesto de dato que puede almacenar distintos valores NO ordenados entre {} y separados por coma. Tienen 2 caracteristicas importantes:
# - Dentro de un conjunto, no hay orden
#numeros = {1, 2, 3, 4}
#print(numeros)
#nombres = {"Cristian", "Sara", "Daniel"}
#print(nombres)
#print(type(numeros))

# - La segunda caracteristica es que no puede haber duplicados
# Por otro lado aunque no se puede cambiar sus elementos SI se puede agregar nuevos utilizando:

# -) la funcion add() Para agregar un elemnto a un conjunto
# -) la funcion update() Para agregar mas de un elemtno a un conjunto

#lenguajes={"Python","C++","Java"}
#print (lenguajes)

#lenguajes.add("Javascript")
#print(lenguajes) # como se puede ver, el orden es totalmente aleatorio y decidido por el lenguaje.

# Funciones avanzadas. UNION, INTERSECCION y DIFERENCIA
#UNION -> la union se realiza con el caracter | y retonra un conjunto que contiene los elementos que se encuentran en al menos uno de los dos conjuntos involucrados en la operacion
#a={1,2,3,4}
#b={3,4,5,6}
#print(a|b)
#INTERSECCION ->la interseccion opera de forma analoga, pero con el operador &, y retorna un nuevo conjunto con los elementos que se encuentran en ambos
#print(a&b)
# DIFERENCIA -> retorna un nuevo conjunto que contiene los elemtos de A que no estan en B
#a={1,2,3,4}
#b={2,3}
#print(a-b)


# DICCIONARIOS

#Tipo compuesto de datos que puede almacenar distintos valores (pares de clave:valor) NO ordenados entre {} y separados con comas. La estructura principal es "Clave:Error"

#vehiculos={"brand":"Ford","model":"Mustang","year":1694}
#Accederemos a los elemtnos de un diccionario haciendo referencia a su CLAVE, y esto nos devolvera su VALOR correspondiente
#print(vehiculos["model"])

#valorQueMeInteresa=vehiculos["model"]
#print(valorQueMeInteresa)
#valorQueMeInteresa=vehiculos.get("model")
#print(valorQueMeInteresa)

#Operador "IN" solo actua sobre las claves, nos dice si esa clave existe o no
#print("model" in vehiculos)

# Podemos modificar un valor haciendo referencia a su clave
#vehiculos={"brand":"Ford","model":"Mustang","year":1694}
#print(vehiculos)
#vehiculos["year"]=2022
#print(vehiculos)

#vehiculos["year"]=vehiculos["year"]+5 #permite sumarle tambien a los valores del diccionario
#print(vehiculos)

#Agregar elementos al diccionario
# La adicion de un elemonto al diccionario se realiza utilizando una nueva clase de indice asignandole un valor
#vehiculos={"brand":"Ford","model":"Mustang","year":1694}
#vehiculos["color"]="red"#aunque no aparezca el valor "color" Python lo añade al diccionario
#print(vehiculos)

# ELIMINAR elementos del diccionario .POPITEM
#vehiculos={"brand":"Ford","model":"Mustang","year":1694}
#print(vehiculos)
#eliminado = vehiculos.popitem() #Elimina el ultimo item insertado y nos devuelve el valor eliminado
#print(vehiculos)
#print(eliminado) #nos lo devuelvo como formato de tupla
#print("Se ha eliminado la siguiente pareja de datos: ",eliminado)

# VACIAR el diccionario con el metodo "CLEAR"
#vehiculos={"brand":"Ford","model":"Mustang","year":1694}
#vehiculos.clear()
#print(vehiculos)

# COPIAR UN DICCIONARIO
# No puede copiar un diccionario simplemente escribiendo "dict2 = dict1", porque dict2 solo sera una referencia a dict1, y los cambios realizados en dict1 tambien se realizaran automaticamente en dict2
# Hay formas de hacer una copia, una es usar el metodo incorpordado copy()
#vehiculos={"brand":"Ford","model":"Mustang","year":1694}
#print(vehiculos)
#vehiculos_copia=vehiculos.copy()
#print(vehiculos_copia)

#vehiculos.pop("model") #elimina el elemento con el nombre de clave especificado
#print(vehiculos)
#print(vehiculos_copia) #comprobamos que la copia sigue intacta y no se ha modificado con el original

# SI puede haber diccionarios dentro de otros diccionarios (anidados)

#familia = {"hijo1": {"nombre":"Carlos","año": 1984},
          #"hijo2":{"nombre":"Ana","año":1989},
          #"hijo3":{"nombre":"Marcos","año":1994}}
#print(familia)
#print(familia["hijo1"])

# BONUS. Incluir listas en nuestros diccionarios

#diccionario = {"nombre":"Carlos",
              #"edad": 28,
              #"cursos":["Python","Django","Javascript"]}

#print("Diccionario completo: ")
#print(diccionario)

#print("\nElementos del diccionario")
#print(diccionario["nombre"]) #Carlos
#print(diccionario["edad"]) #28
#print(diccionario["cursos"]) #[Python,Django,Javascript]

#print("\nItems de la lista cursos: ")
#print(diccionario["cursos"][0])
#print(diccionario["cursos"][1])
#print(diccionario["cursos"][2])

#print("\nRecorriendo el diccionario con un bucle for: ")
#for key in diccionario:
  #print(key,":",diccionario[key])


## CONDICIONALES Y BUCLES
# Condicionales: IF-ELIF-ELSE
# Bucles FOR
# Bucles WHILE

# Sentencia IF (si)
# Permite dividir el flujo de un programa en diferentes caminos. El IF se ejecuta siempre que la expresion que comprueba devuelve True
#if True:
  #print("Se cumple la condicion")
  #print("Estamos dentro del bloque del if")

#if 7 == 7:
  #print("Se cumple la condicion porque 7 es igual a 7")
  #print("estamos dentro del bloque IF")
#print("Este print no perteneces al bloque del if")

#if 7 == 8:
  #print("Se cumple la condicion porque 7 es igual a 7")
  #print("estamos dentro del bloque IF")
#print("Este print no perteneces al bloque del if") # solo va a aparecer esta linea


#a=2
#if a == 2:
  #print("a vale 2")
#if a == 5:
  #print("a vale 5")

#a = 7 # primera linea comprueba
#b = 9 # segunda linea que comprueba
#if a == 7: # tercera linea que comprueba
  #print("a=",a)
  #b += 1
  #if b == 10:
    #print("b=",b)

# Como condicion podemos evaluar multiples expresiones, siempre que estas devuelvan True o False

#a=7
#b=10
#print(a==7 and b==10)
#print(a==7)
#print(b==10)
#if a == 7 and b ==10:
  #print("a = 5")
  #print("b = 10")

# Sentencia ELSE (Sino)
#n=7
#if 7 >=0:
  #print(n,"es un numero mayor o igual que 0") # como se cumple la condicion sale este print y no ejcuta el else, ya que el ELSE es la estructura CONTRARIA AL IF.
#else:
  #print(n,"es un numero menor que 0")

#n=8
#if n % 2 == 0:
  #print(n,"el numero es par")#nunca va poder ejecutarse un IF con un ELSE, solo se cumple una
#else:
  #print(n,"el numero es impar")

# SENTENCIA ELIF (Sino Si)
  # Se encadena a un if u otro elif para comprobar multiples ocndiciones, siempre que las anteriores no se ejecuten.
#nota = float(input("Introduce una nota: "))
#print("la nota",nota,"es del tipo",type(nota))

#if nota >=9:
    #print("Sobresaliente")
#elif nota >=7 and nota <9:
    #print("Notable")
#elif nota >=6:
    #print("Bien")
#elif nota >=5:
    #print("Suficiente")
#else:
    #print("Insuficiente")

## BUCLE WHILE (Mientras)
  # Se basa en repetir un bloque a partir de evaluar una condicion logica, siempre que esta sea TRUE
  # Queda en manos del programador decidir el momentoen que la condicion cambie a False para hacer que el bucel WHILE finalice

# ITERACIONES
  # Iterar significa realizar una accion varias veces. Cada vez que se repite se denomina iteracion.

#contador = 1
#while contador <= 5:
  #print(contador)
  #contador += 1 #contador = contador + 1
#print("continuamos con nuestro codigo")

# Sentencias ELSE en bucle while
# Se encadena al While para ejecutar un bloque de codigo una vez la condicion ya no devuelve True (normalmente al final)

#numero = 1
#while numero <= 5:
  #numero += 1
  #print("numero =",numero)
#else:
  #print("Fin del while -> numero =",numero)

## Instruccion BREAK
# Sirve para "romper" la ejecucion del WHILE en cualquier momento. No se ejecutara el ELSE, ya que este solo se llama al finalizar la operacion.
#numero = 0
#while numero <= 5:
 # numero += 1
  #if (numero ==3):
   # print("Rompemos el bucle cuando el numero es igual a",numero)
    #break
#  print("numero = ",numero)
#else:
#  print("Fin del while -> numero = ",numero)
#print("continuamos con el programa aqui")

## Instruccion CONTINUE
# Sirve para "saltarse" la iteracion actual sin romper el bucle

#numero = 0
#while numero <= 5:
  #numero += 1
 # if numero == 3 or numero == 4:
 #   print("Continuamos a la siguiente iteracion")
 #   continue
 # print("numero =",numero)
#else:
#  (print("Fin del while -> numero = ",numero))

## CREANDO UN MENU INTERACTIVO

#print("Bienvenido a la calculadora de Python")
#while (True): # asi hacemos que el bucel sea infinito##

#  print("""
#  1)Sumar dos numeros
#  2)Restar dos numeros
#  3)Salir""")
  
#  opcion = input("Introduzca una opcion: ")
#  if opcion == "1":
#    n1 = float(input("Introduce el primer numero: "))
#    n2 = float(input("Introduce el segundo numero: "))
#    print("El resultado de la suma es ",n1 + n2)

#  elif opcion == "2":
#    n1 = float(input("Introduce el primer numero: "))
#    n2 = float(input("Introduce el segundo numero: "))
#    print("El resultado de la resta es ",n1 - n2)

#  elif opcion == "3":
#    print("Saliendo del programa")
#    break

#  else:
#    print("opcion no valida")


## BUCLE FOR (para)
# El bucel FOR se utiliza para repetir una o mas instrucciones un determinado numero de veces. Lo utilizamos cuando queremos realizar una tarea pero sabemos exactamente el numero de veces que vamos a realizarla

#numeros=[1,2,3,4]
#for i in numeros:
 # numeros.append(6)
#  print(numeros)

#for x in range(10,20,2):
  #print(x)

#numeros=[1,2,3,4,5,6,7,8,9,10]
#for num in numeros:
#  print(num)

# Para asignar un nuevo valor a los elementos de una lista mientras la recorremos, podriamos intentar asignar un valor al numero el nuevo valor:

#print("Lista inicial: ")
#print(numeros)

#for num in numeros:
 # num *= 10 # num = num * 10
  #print(num, end=",")

#print("\nLista final") #con la "\n" imprimo todo en la misma linea
#print(numeros)

# La forma correcta de asignar un nuevo valor a los elementos de la lista mientras la recorresmos es haciendo referencia al indice de la lista en lugar de la variable:

#indice = 0
#numeros=[1,2,3,4,5,6,7,8,9,10]
#print("Lista incial : ",numeros)

#for numero in numeros:
#    numeros[indice] *=10
#    indice +=1
#print("\nLista final:",numeros)

# Podemos utilizar la funcion ENUMERATE() para conseguir el indice y el valor en cada iteracion facilmente:

# Utilizamos el enumerate cuando necesitamos las posiciones y los valores

#numeros = [10,20,30,40,50,60,70,80,90,100]
#for indice,num in enumerate (numeros):
#  print("indice",indice)
#  print("num: ",num)
#  numeros[indice] *= 10
#print(numeros)

#utilizamos "FOR" tambien en strings y podemos por ejemplo contar cuantas letras aparecen en una frase

#texto="Aprendiendo Python"

#contador=0
#for letra in texto:
#  if letra == "A" or letra == "a":
#    contador += 1
#    print(letra)
#print("El numero de A es: ",contador)

# y si ahora utilizamos el enumerate podemos conseguir encima que las posiciones queden a la vista

#texto="Aprendiendo a programar en Python"

#contador=0
#for indice,letra in enumerate(texto):
#  if letra == "A" or letra == "a":
#    contador += 1
#    print(letra,"en la posicion",indice)
#print("El numero de A es: ",contador)

# Hay 3 tipos de utilidades para el bucle FOR:
  # -> el bucle FOR normal, el simple, el que visualizamos y ya
  # -> el bucle FOR con ENUMERATE que nos sirve para acceder a la informacion y admeas poder ver la informacion de esa posicion
  # -> y el ultimo que es el bucle FOR combinado coon RANGE qu esirve para generar una lista de numeros que podemos recorrer facilmente, pero no ocupa memoria porque se interpreta sobre la marcha, sirve  para cuando por ejemplo queremos ejecutar un determinado codigo x veces

#for i in range(5):
#  print("Hola mundo")

#con RANGE podemos generar rangos especificos, podemos decir que queremos un rango que vaya de 5 a 10 por ejemplo y encima podemos especificar hasta un tercer valor
  
#for i in range (5,10):
#  print(i)
  
# range(fin)
# range(inicio,fin)
# range(inicio,fin,salto)

#for i in range(0,100,10):
#  print(i)

# aqui podemos ver como se hace para imprimr dos listas a la vez

#lista1=[1,2,3,4,5]
#lista2=[6,7,8,9,10]

#for i in range(len(lista1)):
 # print(lista1[i])
  #print(lista2[i])
  #print("------")

  

    
  
  
