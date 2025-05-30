# 🚀 Retos Semanales

Este repositorio contiene las soluciones a los retos semanales de programación. Cada solución está organizada por lenguaje o tecnología, y nombrada con el nombre del autor para fácil identificación.

## 📌 Buenas Prácticas

1. Nombra tu archivo con tu nombre o alias.
2. Guarda tu archivo en la carpeta correspondiente al lenguaje usado. Si no existe, créala.
3. Documenta tu código con comentarios útiles.
4. Mantén este `README.md` bien organizado si haces cambios.

## 🧠 Tecnologías Usadas

- Python 🐍
- JavaScript 💻
- C++ 🧠
- Java ☕
- HTML + CSS 🌐
- y la que tu quieras 

## 🙌 Contribuyentes

- Marco (autor principal)

---

# ejemplo de un codigo documentado

# Autor: Marco
# Lenguaje: Python
# Reto: Sumar dos números dados por el usuario

def sumar_numeros(a, b):
    """
    Función que suma dos números.
    :param a: primer número
    :param b: segundo número
    :return: suma de a y b
    """
    return a + b

# Solicita al usuario dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Imprime el resultado
print(f"La suma es: {sumar_numeros(num1, num2)}")
