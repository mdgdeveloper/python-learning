# Ejercicio #1: Formateador aritmético 

Este es uno de los ejercicios que forman parte del catálogo básico de ejercicios de Python accesible a través del siguiente repositorio: [https://github.com/mdgdeveloper/python-learning](https://github.com/mdgdeveloper/python-learning)

El primero de los ejercicios con Python ha sido el de crear un formateador aritmético.

La entrada del problema es un array de cadenas de texto de la forma:
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

De tal forma que el resultado final sea: 

```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474

```

El programa debe ser capaz de lanzar errores en los siguientes supuestos:
1. Cuando se le pasen más de 5 operaciones
2. Cuando las operaciones estén mal formateadas: numero operando numero 
3. Cuando los operandos tengan mas de 4 cifras 
4. Cuando los operadores no sean o suma o resta.

Mi primera solución, seguramente infinitamente mejorable, es la siguiente:

En la primera fase del programa inicializamos el resultado, siendo cada elemento del array un string en el que se almacenará temporalmente cada línea de la respuesta: (operandos 1, operandos 2 junto con el operador, linea de separación y el resultado).
```python
def arithmetic_arranger(operations):
    result = ["", "", "", ""]

    # Primera comprobacion: Maximo 5 operaciones
    if len(operations) > 5:
        return ('Error: too many problems')
    else:
      # Iteramos el array para ir construyendonos la aritmetica:
      for oper in operations:
          aux = oper.split()
          if (len(aux) < 3):
            # Segunda comprobacion: tenemos que introducir tres elementos: 2 operandos y 1 operador
              return ("Error: too few arguments")

          # Almacenamos los operandos (convirtiendolos a enteros) y el operador.
          operand1 = int(aux[0])
          operator = aux[1]
          operand2 = int(aux[2])
          # Llamamos a la funcion max_len que nos proporcionara la longitud maxima de los dos operandos
          maxLen = max_len(aux[0], aux[2])      
```

En este punto hago una llamada a una de las funciones auxiliares que me he creado para el programa. Creo que, siempre que se pueda, modularizar el comportamiento de una función conlleva muchas ventajas y es recomendable.

```python
def max_len(operand1, operand2):
    len1 = len(operand1)
    len2 = len(operand2)

    return (np.fmax(len1, len2))
```

Siguiendo con el programa principal, ya disponemos de todos los elementos que nos van a permitir analizar los posibles errores restantes, asi que lo agrupamos en esta parte del código:
```python
# Error control
  if (np.isnan(operand1) or np.isnan(operand2)):
      return ("Error: operands MUST be numbers")
  if (operator != "+" and operator != "-"):
      return ("Error: Operation MUST be + or -")
  if (len(aux[0]) > 4 or len(aux[2]) > 4):
      return ("Error: Numbers cannot be more than four digits")
```

A continuación vamos a calcular el resultado y, en función del mismo, definiremos una variable auxiliar que nos va a añadir un número de espacios variables para la línea de resultado dependiendo de si el resultado es negativo, positivo o supera los 4 digitos:

```python
operationResult = calculate(operand1, operand2, operator)
if (operationResult < 0):
    addSpaces = " "
else:
    addSpaces = "  "
if (len(str(operationResult)) > 4 and operationResult > 0):
    addSpaces = " "
```

```python
def calculate(operator1, operator2, operand):
    if (operand == "+"):
        return operator1 + operator2
    else:
        return operator1 - operator2
```

Al tener controlado el numero máximo de digitos de los operandos, podemos fijar algunos de los cálculos a ese valor. De lo contrario, necesitaríamos usar el valor maxLen para realizar las comprobaciones. 

Procedo después a crear los elementos visuales restantes: el separador entre operaciones (4 espacios en blanco) y la línea de la operación, que vendrá definida por el operando con longitud máxima:

```python
separator = 4*" "
line = (maxLen+2)*"-"
```

Quedaba pendiente justificar los operandos, puesto que el ejercicio exige que aparezcan justificados a la derecha. Para ello, de nuevo, vamos a hacer uso de una función auxiliar que me va a devolver un String con el número de espacios que debo insertar para justificar los números:

```python
esp0 = esp(aux[0], maxLen)
esp1 = esp(aux[2], maxLen)
esp3 = esp(str(operationResult), maxLen)
```

```python
def esp(operand, maxLen):
    if (len(operand) < maxLen):
        return (maxLen-len(operand))*" "
    else:
        return ""
```

Una vez obtenidos todos estos valores, ya solo nos queda generar cada una de las lineas que conforman la operacion. Al tratarse de un proceso iterativo, iremos añadiendo estos valores conforme vayamos trabajando con cada una de las operaciones:

```python
result[0] = result[0] + "  " + esp0 + f"{operand1}{separator}"
result[1] = result[1] + f"{operator} {esp1}{operand2}{separator}"
result[2] = result[2] + line + separator
result[3] = result[3] + addSpaces + esp3 + str(operationResult) + separator
```

Por último, dado que el ejercicio nos pide que demos un resultado único, convertiremos nuestro Array auxiliar en un string con saltos de línea:

```python
resultStr = ""
for line in result:
  resultStr = resultStr + line + "\n"
```

Con esto concluiríamos con el ejercicio que nos solicitan, habiendo contemplado todos los casos posibles. Mi intención en un futuro es volver a repetir el proceso, pero esta aplicando metodologías de desarrollo más avanzadas e incluyendo testing. 