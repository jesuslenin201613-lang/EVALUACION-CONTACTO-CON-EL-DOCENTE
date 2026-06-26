
import random  # Importa la librería random para generar valores aleatorios

# Función para generar la contraseña
def generar_contraseña(longitud):  # Define una función que recibe la longitud de la contraseña
    caracteres = "abcdefghijklmnñopqrstvwxyzABCDEFGHIJKLMNÑOPQRSTVWXYZ0123456789#$&*!"  # Lista de caracteres posibles
    contraseña = ""  # Variable vacía donde se construirá la contraseña

    for i in range(longitud):  # Repite el ciclo tantas veces como la longitud indicada
        contraseña += random.choice(caracteres)  # Agrega un carácter aleatorio a la contraseña

    return contraseña  # Devuelve la contraseña generada

# Función para verificar si la contraseña es segura
def es_segura(contraseña):  # Define función que evalúa la seguridad de la contraseña

    mayuscula = False  # verificar mayúsculas
    minuscula = False  # verificar minúsculas
    numero = False  # verificar números
    simbolo = False  # B verificar símbolos

    for caracter in contraseña:  # Recorre cada carácter de la contraseña

        if caracter.isupper():  # Si el carácter es mayúscula
            mayuscula = True  # Marca que hay una mayúscula

        elif caracter.islower():  # Si el carácter es minúscula
            minuscula = True  # Marca que hay una minúscula

        elif caracter.isdigit():  # Si el carácter es un número
            numero = True  # Marca que hay un número

        else:  # Si no es letra ni número, es símbolo
            simbolo = True  # Marca que hay un símbolo

    if len(contraseña) >= 2 and mayuscula and minuscula and numero and simbolo:  # Evalúa seguridad completa con la funcion LEN midiendo la longitud
        return True  # La contraseña es segura
    else:
        return False  # La contraseña no es segura


# Programa principal

longitud = int(input("¿Cuál es la longitud de la contraseña deseada?: "))  # Pide la longitud al usuario

while True:  # Bucle infinito hasta que el usuario decida salir

    nueva_contraseña = generar_contraseña(longitud)  # Genera una nueva contraseña
    print("\nLa nueva contraseña es:", nueva_contraseña)  # Muestra la contraseña generada

    if es_segura(nueva_contraseña):  # Verifica si la contraseña es segura
        print("La contraseña es SEGURA.")  # Mensaje si es segura
    else:
        print("La contraseña NO es SEGURA.")  # Mensaje si no es segura

    opcion = input("¿Deseas mantener su contraseña? (si/no): ").strip().lower()  # Pregunta al usuario y normaliza texto

    if opcion == "si":  # Si el usuario acepta la contraseña
        print("Tu contraseña será:", nueva_contraseña)  # Muestra la contraseña final
        exit()  # Termina completamente el programa

    elif opcion == "no":  # Si el usuario no la acepta
        longitud = int(input("\nIngrese una nueva longitud para la contraseña: "))  # Pide nueva longitud

    else:  # Si escribe algo incorrecto
        print("Opción no válida. Escriba solo 'si' o 'no'.")  # Mensaje de error