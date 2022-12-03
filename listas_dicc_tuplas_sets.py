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