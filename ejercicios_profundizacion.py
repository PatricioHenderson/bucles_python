#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Patricio Henderson"
__email__ = "patricio.henderson.v@gmail.com"
__version__ = "1.2"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''
    
    inicio = int(input("Introducir primer numero: "))
    fin = int(input("Introducir segundo numero: "))

    sumatoria = 0
    contador = 0
    for i in range(inicio,fin + 1):
        contador += 1
        sumatoria += i

    promedio = sumatoria / contador
    print ("Cantidad numeros : " , contador , "Sumatoria : ", sumatoria, 
            "Promedio : ", promedio)
    # cantidad_numeros ....
    # sumatoria ....

    # bucle.....

    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros

    # Imprimir resultado en pantalla


def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
    
    numero_1 = float(input("Introducir primer numero: "))
    
    numero_2 = float(input("Introducir segundo numero: "))
    
    funcion = str(input("Introducir simbolo operación a realizar "))
    
    while funcion != "FIN":

        if funcion == "+" :

            print ("el resultado es : " , numero_1 + numero_2)
            
            numero_1 = float(input("Introducir primer numero: "))
    
            numero_2 = float(input("Introducir segundo numero: "))
    
            funcion = str(input("Introducir simbolo operación a realizar "))

        elif funcion == "-" :

            print ("el resultado es : ", numero_1 - numero_2)

            numero_1 = float(input("Introducir primer numero: "))
    
            numero_2 = float(input("Introducir segundo numero: "))
    
            funcion = str(input("Introducir simbolo operación a realizar "))

        elif funcion == "*" :

            print ("el resultado es : ", numero_1 * numero_2)

            numero_1 = float(input("Introducir primer numero: "))
    
            numero_2 = float(input("Introducir segundo numero: "))
    
            funcion = str(input("Introducir simbolo operación a realizar "))

        elif funcion == "/" :

            print ("el resultado es : ", numero_1 / numero_2)

            numero_1 = float(input("Introducir primer numero: "))
    
            numero_2 = float(input("Introducir segundo numero: "))
    
            funcion = str(input("Introducir simbolo operación a realizar "))
    
        elif funcion == "**" :

            print ("el resultado es : ", numero_1 ** numero_2)

            numero_1 = float(input("Introducir primer numero: "))
    
            numero_2 = float(input("Introducir segundo numero: "))
    
            funcion = str(input("Introducir simbolo operación a realizar "))
         
        else :

            print ("Indrodujo una transacción no soportada")
            break


    if funcion == "FIN":
        print("Programa terminado.\n")
        
        
   


def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudiante se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''

    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0           # Ya le hemos inicializado en 0

    cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria
    for i in notas:

        if i < 0 :
            cantidad_ausentes += 1 
            

        if i > 0 :
            sumatoria += i
            cantidad_notas +=1
            
    

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas
    promedio = sumatoria / cantidad_notas
    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado
    puntaje = promedio

    if 100 < puntaje >= 90:
        
        print ("A")

    elif  90 > puntaje >= 80 :

        print("B")

    elif  80 > puntaje >= 70 :
        
        print ("C")
    
    elif 70 > puntaje >= 60 :

        print ("D")
    
    elif 60 > puntaje >=0  :
        
        print ("F")

    else:

        print ("Dato incorrecto")
    # Imprima en pantalla al cantidad de ausentes
    print(sumatoria, cantidad_notas, cantidad_ausentes)

def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temporada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.
    
    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''

    temperatura_max = 0     # Aquí debe ir almacenando la temp máxima
    temperatura_min = 0      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

    # Colocar el bucle aqui......
    temperatura_min = 100
    for i in temp_dataloger:
        

        if i > temperatura_max:
            temperatura_max = i
        
        if i  < temperatura_min :
            temperatura_min = i

        temperatura_sumatoria += i
        temperatura_len += 1

    temperatura_promedio = temperatura_sumatoria / temperatura_len

    print (temperatura_max, temperatura_min, temperatura_sumatoria, temperatura_promedio, temperatura_len)       

    from statistics import mean
    
    maxima = max(temp_dataloger) 
    
    minima = min(temp_dataloger)
    
    sumatoria = sum(temp_dataloger)
    
    promedio = mean(temp_dataloger)
    
    largo = len(temp_dataloger)
    
    print(maxima, minima, sumatoria, promedio , largo)
    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''
    if temperatura_max <= 18 and temperatura_min >= 19:
        print("Verano")

    if temperatura_max <= 24 and temperatura_min >= 11:
        print ("Otoño")
    
    if temperatura_max <= 14 and temperatura_min >= 8:
        print("Invierno")
    
    if temperatura_max <= 24 and 11 > temperatura_min >= 10 :
        print("Primavera")


    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Obtener la palabra más grande por orden alfabético (usando el operador ">")
    2 - Obtener la palabra más grande por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    
    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

  '''

    
    
    palabra_1= str(input("Introducir primer palabra: "))
    palabra_2= str(input("Introducir segunda palabra: "))
    palabra_3= str(input("Introducir tercer palabra: "))
    #Creamos la lista
    lista =  palabra_1.lower() , palabra_2.lower() , palabra_3.lower()
    #Ponemos todo en minusculas para que luego queden bien ordenadas
    

    orden = int(input("Elegir 1 para orden alfabético o 2 para ordenar por cantidad  de letras"
            "o 3 para salir: "))

    #Dejamos selección de opcion por teclado
    # Si elije 1 o 2 luego de ordenar esas palabras iniciales, entra en un bucle   
    while True:
        # Si pongo este IF abajo de todo, no me lo tomaba al selecionar la opción 3
        if orden == 3:
            break
        # Continiamos al proximo paso
        else:
            print("Selección incorrecta.")
            continue

        if orden == 1 :

            lista_orden = sorted(lista)
            print (lista_orden)
                
    
        elif orden == 2 :

            lista_orden = sorted(lista, key=len , reverse=True)

            print (lista_orden)

        # Solicitamos ingrese por teclado cuantas palabras va a querer ingresar:   
        cantidad_palabras = 0        
        cantidad_palabras = int(input("ingrese cantidad de palabras deseadas :"))

        palabras_deseadas = 0
        lista_palabras = []

        while palabras_deseadas < cantidad_palabras :
            palabras_deseadas += 1
            nueva_palabra = str(input("Ingrese nueva palabra: \n"))
            nueva_palabra_minusc = nueva_palabra.lower()
            lista_palabras.append(nueva_palabra_minusc)
        # Una vez ingresadas todas las palabras, solicitamos indique como quiere el orden    

        orden_2 = int(input("1 Para más grande o 2 con mayor cantidad de letras: "))
                
        if orden_2 == 1 :
            print (max(lista_palabras))
        #2 distintas formas de hacerlo para ver si el resultado es el mismo
        
        if orden_2 == 1:
            mayor_palabra = lista_palabras[0]
            for i in lista_palabras :
                if i > mayor_palabra :
                    mayor_palabra = i
            print(mayor_palabra)
            break

        

        if orden_2 == 2 :
            largo_palabra = lista_palabras[0]   

            for i in lista_palabras :
                if len(i) > len(largo_palabra):
                    largo_palabra = i
            print(largo_palabra)
            break
        # Si se elecciona 3 volvemos al inicio
    

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
