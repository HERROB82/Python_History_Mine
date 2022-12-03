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

  

    
  
  
