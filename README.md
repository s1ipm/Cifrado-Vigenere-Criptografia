# Cifrado-Vigenere-Criptografia

El código implementa un cifrado de sustitución polialfabética. A diferencia de los métodos de sustitución simple, este algoritmo utiliza una palabra clave para variar el desplazamiento de cada letra del mensaje, lo que dificulta significativamente el análisis de frecuencias convencional.

**El sistema utiliza un alfabeto de 37 caracteres:**
_ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789_

### Fundamentos

El funcionamiento del programa se basa en la aritmética modular. Primero, se asigna un valor numérico a cada carácter del alfabeto;

*CIFRADO* para obtener el mensaje cifrado, se suma el valor de la letra del mensaje con el valor de la letra correspondiente de la clave:

$$C_i = (M_i + K_i) \pmod{37}$$

*DESCIFRADO* Para recuperar el mensaje original, se resta el valor de la clave al valor del carácter cifrado:
(el **mod** permite que el resultado siempre permanezca dentro de los límites del alfabeto definido, creando un ciclo continuo de caracteres.)

$$M_i = (C_i - K_i) \pmod{37}$$

### Implementación

1. **Normalización:** El programa transforma todas las entradas a mayúsculas y elimina los espacios en blanco del mensaje para asegurar la consistencia en el procesamiento.

2. **Repetición de Clave:** Si la clave es más corta que el mensaje, el script utiliza el operador de residuo para repetir la clave cíclicamente hasta cubrir la longitud total del texto.

3. **Validación:** Se incluye un control de errores que verifica que cada carácter ingresado por el usuario exista dentro del alfabeto de 37 caracteres antes de proceder con el cálculo.

### Uso

1. Ejecutar el archivo: python vigenere.py
2. Seleccionar la operación (1 para cifrar, 2 para descifrar y 3 para salir del programa).
3. Ingresar el texto y la clave de seguridad cuando el sistema lo solicite.
4. El resultado se mostrará inmediatamente en la consola.
