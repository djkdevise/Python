#Delcarcion de variables
name = "Jamith"

#Validamos el tipo de dato de la variable name
print(type(name)) #deberia ser string

#Convertimos el tipo de dato de la variable a name de string a int
name = 12

#Validamos el tipo de dato de la variable name
print(type(name)) #deberia ser int

#convertimos el tipo de dato de la variable name de int a boolean
name = True

#Validamos el tipo de dato de la variable name
print(type(name)) #deberia ser boolean

print("Nicolas" + " " + "Jamith") #concatenacion de strings

print(10 +20) #suma de numeros

print("Nicolas " + "10") #Error de tipos de datos "TypeError: can only concatenate str (not "int") to str"

#Ejemplo de conversion de tipos de datos
#Declaramos la variable age
age = 12

#Usamos la varible age como parte de una cadena usando print
print("Mi edad es " + str(age)) #es una concatenacion de un string con un int

print(f"Mi edad es {age}") #Se usa 'f' para indicar que es una cadena de texto y se usa {} para indicar que es una variable

#Solictamos al usuario que ingrese su edad
age = input('Ingresa tu edad: ') #Capturamos la edad del usuario desde el teclado
print(type(age)) #Validamos el tipo de dato de la variable age
age = int(age) #Convertimos el tipo de dato de la variable age de string a int
age = age + 10 #sumamos 10 a la variable age
print(f"Tu edad dentro de 10 años sera {age}")

#Si el usuario en lugar de ingresar un numero ingresa un texto, se genera un error de tipo de dato
#ValueError: invalid literal for int() with base 10: 'treinta'






