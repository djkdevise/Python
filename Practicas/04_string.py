# Uso del tipo de datos String

#Variables

name = 'Jamith'
last_name = 'Garcia'
age = 42
print(name)
print(last_name)
# Concatenar valores en python

full_name = name + " " + last_name

print(full_name)

# Formatos / format / f
# format
template = "Hola, mi nombre es {} y mi apellido es {}.".format(name, last_name)
print("Ver 1", template)
# f
template = f"Hola, mi nombre es {name}, mi apellido es {last_name} y mi edad es {age}."
print("Ver 2", template)
