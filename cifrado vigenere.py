def vigenere():
    # alfabeto español (27 LETRAS y 10 numeros)
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    
    # bucle hacia el menú
    while True:
        # muestra las opciones a escoger del 1 al 3
        print("\n1. cifrar")
        print("2. descifrar")
        print("3. salir")
        opcion = input("Elige: ")
        
        # sale del programa y da por terminado la ejecución del codigo
        if opcion == "3":
            break
        
        # vaida la opcion correcta entre el 1 y 2
        if opcion not in ["1", "2"]:
            print("Opción inválida")
            continue
        
        # entrada de los datos 
        mensaje = input("Mensaje: ").upper().replace(" ", "")  # da la opcion de leer el mensaje con mayusculas o minusculas
        clave = input("Clave: ").upper()

        # valida los caracteres del mensaje
        valido = True
        for c in mensaje:  # revisa cada letra del abecedario
            if c not in alfabeto:
                print(f"'{c}' no está en el alfabeto")
                valido = False
                break
        
        # valida los caracteres de la clave
        for c in clave:  # revisa cada letra de la clave
            if c not in alfabeto:
                print(f"'{c}' no está en el alfabeto")
                valido = False
                break
        
        # ni identifica un caracter invalido, regresa al menu
        if not valido:
            continue

        # repite la clave hasta acompletar el mismo tamaño del mensaje
        clave_rep = ""
        for i in range(len(mensaje)):
            clave_rep += clave[i % len(clave)]  # toma la letra en manera de ciclo
        
        # cifrado/descifrado
        resultado = ""
        for i in range(len(mensaje)):
            # convierte letras a numeros
            m = alfabeto.index(mensaje[i])  # valor numerico de la letra mensaje
            k = alfabeto.index(clave_rep[i])  # valor numerico de la letra de clave
            
            # aplica la formula segun la opcion a escoger
            if opcion == "1":
                valor = (m + k) % len(alfabeto)  # cifra: (M + K) mod 37
            else:
                valor = (m - k) % len(alfabeto)  # descifra: (M - K) mod 37
            
            # convierte numero a letra y agrega el resultado para mandar a imprimir
            resultado += alfabeto[valor]
        
        # muestra el resultado final
        print(f"resultado: {resultado}")

# ejecuta el nombre del programa marcado desde un inicio
vigenere()