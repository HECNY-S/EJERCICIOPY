'''objetivo: desarrollar un programa en python que solicite al usuario su nombre, edad y numero, 
luego realice operaciones basicas con los datos proporcionados'''

nombre = input("Por favor, Ingrese su nombre: ")
edad = input("Por favor, Ingrese su edad: ")
print(f"¡BIENVENIDA! {nombre}, Tienes {edad} años")
numero_ingresar = input("Por favor, Ingrese un numero: ")
numero_entero = int(numero_ingresar)
print(type(numero_entero))
doble = numero_entero * 2
print(f"el doble del numero ingresado es {doble}. ")