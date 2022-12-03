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