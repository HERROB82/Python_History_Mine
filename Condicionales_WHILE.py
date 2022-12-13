## BUCLE WHILE (Mientras)
  # Se basa en repetir un bloque a partir de evaluar una condicion logica, siempre que esta sea TRUE
  # Queda en manos del programador decidir el momento que la condicion cambie a False para hacer que el bucle WHILE finalice

# ITERACIONES
  # Iterar significa realizar una accion varias veces. Cada vez que se repite se denomina iteracion.

'''contador = 1
while contador <= 5:
  print(contador)
  contador += 1 #contador = contador + 1
print("continuamos con nuestro codigo")'''

# Sentencias ELSE en bucle while
# Se encadena al While para ejecutar un bloque de codigo una vez la condicion ya no devuelve True (normalmente al final)
# EL BUCLE WHILE SE ESTARA REPITIENDO MIENTRAS UNA CONDICION SE CUMPLA, por lo que el bucle while dependera de esta condicion!!

'''numero = 0
while numero <= 5:
  numero += 1
  print("numero =",numero)
else:
  print("Fin del while -> numero =",numero)'''

  ## Instruccion BREAK
# Sirve para "romper" la ejecucion del WHILE en cualquier momento. No se ejecutara el ELSE, ya que este solo se llama al finalizar la operacion.
# El BREAK sale del bucle, lo rompe por completo, lo revienta!!

'''numero = 0
while numero <= 5:
  numero += 1
  if (numero ==3):
    print("Rompemos el bucle cuando el numero es igual a",numero)
    break
  print("numero = ",numero)
else:
  print("Fin del while -> numero = ",numero)
print("continuamos con el programa aqui")'''

## Instruccion CONTINUE
# Sirve para "saltarse" la iteracion actual sin romper el bucle
# El CONTINUE rompe solo una iteracion!

'''numero = 0
while numero <= 5:
  numero += 1
  if numero == 3 or numero == 4:
    print("Continuamos a la siguiente iteracion")
    continue
  print("numero =",numero)
else:
  (print("Fin del while -> numero = ",numero))'''

# Ejercicio de Calculadora

print("Bienvenidos a la calculadora de Python")
salir = False
while salir == False:
#while (True):
  print("""
  1)Sumar
  2)Restar
  3)Salir""")
  opcion=input("Introduzca una opcion: ")

  if opcion == "1":
    n1=int(input("Introduzca un numero: "))
    n2=int(input("Introduzca un numero: "))
    print("El resultado de la suma es: ",n1 + n2)

  elif opcion == "2":
    n1=int(input("Introduzca un numero: "))
    n2=int(input("Introduzca un numero: "))
    print("El resultado de la resta es: ",n1 - n2)  

  elif opcion == "3":
    print("saliendo del programa")
    #break
    salir = True # tambien podemos utilizar CONTINUE

  else:
    print("Opcion no valida")·no funciona


