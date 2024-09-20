def mcd(a, b):

    while b != 0:
        a, b = b, a % b
    return a

def es_natural(numero):
    return numero.isdigit() and int(numero) > 0

def ingresar_numero(mensaje):
    while True:
        numero = input(mensaje)
        if es_natural(numero):
            return int(numero)
        else:
            print("Por favor ingrese un número natural válido.")

num1 = ingresar_numero("Ingrese el primer número natural: ")
num2 = ingresar_numero("Ingrese el segundo número natural: ")

resultado = mcd(num1, num2)
print(f"El máximo común divisor de {num1} y {num2} es: {resultado}")
