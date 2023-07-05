from data_stark import *
import os

def extraer_iniciales(nombre_heroe:str)->str:
    """Se encarga de extraer las iniciales del nombre de un heroe, si contiene el articulo "the"
    se quitara, si contiene "-" se reemplazara por un espacio

    Args:
        nombre_heroe (str): El string con el nombre del heroe

    Returns:
        str: El nombre del heroe formateado con las iniciales, en caso de ser un string vacio devolvera "N/A"
    """
    if type(nombre_heroe) == str and len(nombre_heroe) > 0:
        
        partes_nombre = nombre_heroe.split()
        nombre_sin_articulo = ""
        iniciales = ""
        for palabra in partes_nombre:
            if palabra == "the" or palabra == "The":
                palabra = " "

            nombre_sin_articulo += palabra
        
        for letra in nombre_sin_articulo:
            if letra == "-":
                letra = " "

            if letra >= "A" and letra <= "Z":
                iniciales += letra + "."
        
        nombre_actualizado = iniciales.strip()
                
        return nombre_actualizado
    
    else:
        return "N/A"
    
def definir_iniciales_nombre(heroe:dict, clave_nueva:str)->bool:
    """Agrega una nueva clave al diccionario y su valor sera las iniciales del nombre correspondiente

    Args:
        heroe (dict): El diccionario del heroe\n
        clave_nueva (str): El string que se asignara como nombre de la clave

    Returns:
        bool: True en caso de salir todo bien, en caso contrario False
    """
    if type(heroe) == dict and "nombre" in heroe and type(clave_nueva) == str:
        heroe[clave_nueva.lower()] = extraer_iniciales(heroe["nombre"])
        flag_salio_bien = True
    else:
        flag_salio_bien = False
    
    return flag_salio_bien    

def agregar_iniciales_nombre(lista_heroes:list)-> bool:
    """Agregar las iniciales de todos los nombres de los heroes en una clave llamada "iniciales"

    Args:
        lista_heroes (list): La lista que contendra el diccionario de todos los heroes

    Returns:
        bool: True en caso agregar todas las iniciales con exito. En caso contrario un mensaje de error
    """
    if type(lista_heroes) == list and len(lista_heroes) >= 1:
        flag_salio_bien = True
        for heroe in lista_heroes:
            if not definir_iniciales_nombre(heroe,"iniciales"):
                flag_salio_bien = False
                break
        
        if not flag_salio_bien:
            print("El origen de datos no contiene el formato correcto")
        else:
            return flag_salio_bien

def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    """Agrega las iniciales de los nombres de los heroes y luego los muestra en pantalla 

    Args:
        lista_heroes (list): La lista de diccionario de los heroes
    """
    if type(lista_heroes) == list and len(lista_heroes) >= 1:
        agregar_iniciales_nombre(lista_heroes)
        for heroe in lista_heroes:
            print(f"* {heroe['nombre']} ({heroe['iniciales']})")
        
def generar_codigo_heroe(id_heroe:int, genero_heroe:str) -> str:
    """Genera un codigo de 10 digitos del heroe

    Args:
        id_heroe (int): El entero que representara el codigo del heroe
        genero_heroe (str): El genero del heroe (M - F - NB)

    Returns:
        str: El codigo del heroe en caso finalizar correctamente. En caso contrario "N/A"
    """
    
    if type(id_heroe) == int and (genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB") and len(genero_heroe.strip()) > 0:
        codigo_heroe = f"{genero_heroe}-{id_heroe}"
        ceros = ""
        
        while len(codigo_heroe) < 10:
            ceros += "0"
            codigo_heroe = f"{genero_heroe}-{ceros}{id_heroe}"
            if len(codigo_heroe) == 10:
                break
            
        return codigo_heroe
    else:
        return "N/A"
                  
def agregar_codigo_heroe(un_heroe:dict, id_heroe:int) -> bool:
    """Agregar al diccionario de cada heroe la clave "codigo_heroe" con su respectivo codigo

    Args:
        un_heroe (dict): El diccionario del heroe\n
        id_heroe (int): Un entero que representara la id

    Returns:
        bool: True en caso de salir todo bien, False en caso contrario
    """
    if len(un_heroe) > 0:
        codigo = generar_codigo_heroe(id_heroe,un_heroe["genero"])
        if len(codigo) == 10:
            un_heroe["codigo_heroe"] = codigo
            flag_salio_bien = True
    else:
        flag_salio_bien = False
    
    return flag_salio_bien 

def stark_generar_codigos_heroes(lista_heroes:list):
    """
    Itera la lista de heroes y le agrega un codigo a cada uno

    Args:
        un_heroe (dict): La lista con los diccionarios de los personajes
    """
    flag_todo_ok = False
    contador_codigos = 0
    
    if len(lista_heroes) >= 1:
        for heroe in range(len(lista_heroes)):
            if type(lista_heroes[heroe]) == dict and "genero" in lista_heroes[heroe]:
                if agregar_codigo_heroe(lista_heroes[heroe],heroe+1):
                    flag_todo_ok = True
                    contador_codigos += 1
        
    if not flag_todo_ok:
        print("El origen de datos no contiene el formato correcto")
    else:
        print(f"Se asignaron {contador_codigos} codigos\nEl codigo del primer heroe es {lista_heroes[0]['codigo_heroe']}\nEl codigo del ultimo heroe es {lista_heroes[-1]['codigo_heroe']}")
        
def sanitizar_entero(numero_str:str)->int:
    """
    Analiza el string recibido y determinar si es un número entero positivo. Quita los espacios de atras y adelante del string

    Args:
        numero_str (str): El string a analizar\n

    Returns:
        bool: Devuelve distintos valores según el problema encontrado. 
        Si contiene carácteres no numéricos retorna -1.
        Si el número es negativo se deberá retorna un -2.
        Si ocurren otros errores que no permiten convertirlo a entero entonces retornara -3.
    """
    numero_str = numero_str.strip()
    if not numero_str.isdigit() and numero_str[0] != "-":
        return -1
    else:
        try:
            numero = int(numero_str)
            if numero < 0:
                return -2
            else:
                return numero
        except:
            return -3

def sanitizar_flotante(numero_str:str)-> int:
    """Analiza el string recibido y determina si es un número flotante positivo. Quita los espacios de adelante y atras de la cadena

    Args:
        numero_str (str): El string a analizar

    Returns:
        int: Si contiene carácteres no numéricos retorna -1, si el número es negativo retorna -2, 
        si ocurren otros errores que no permiten convertirlo a entero entonces retorna -3
    """    
    numero_str = numero_str.strip()
    
    tiene_punto = False
    
    for caracter in numero_str:
        if caracter == ".":
            tiene_punto = True
            break
    
    if not numero_str.isdigit() and not tiene_punto:
        return -1
    else:   
        try:
            flotante = float(numero_str)
            if flotante < 0:
                return -2
            else:
                return flotante
        except:
            return -3
    
def sanitizar_string(valor_str:str, valor_por_defecto:str = "-") -> str:
    """Analiza un string y determina si es una cadena alfabetica. Cambia las "/" por espacios. Quita los espacios de adelante y atras del string

    Args:
        valor_str (str): String a validar\n
        valor_por_defecto (str, opcional): String. Por defecto en "-".

    Returns:
        str: En caso de que la cadena contenga numeros retornara "N/A", en caso de ser una cadena alfabetica la retornara en minusculas. En caso de no pasarle un string, retornara el valor por defecto en minusculas.
    """    
    if len(valor_str) > 0:
        valor_str = valor_str.strip()
        sin_barra = ""
        str_final = ""
        for caracter in valor_str:
            if caracter.isdigit():
                return "N/A"
             
            if caracter == "/":
                caracter = " "
                sin_barra += caracter
            else:
                sin_barra += caracter
                
        for caracter in sin_barra:
            if (caracter >= "A" and caracter <= "Z") or (caracter >= "a" and caracter <= "z") or (caracter == " "):
                str_final += caracter.lower()
        
        return str_final
    else:
        return valor_por_defecto.lower()

def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str)->bool:
    """Realiza una validacion y casteo del valor del diccionario correspondiente a la clave y al tipo de dato recibido. Valida que exista esa clave dentro del diccionario. 

    Args:
        heroe (dict): un diccionario con los datos del personaje\n
        clave (str): un string que representa el dato a validar\n
        tipo_dato (str): un string que representa el tipo de dato que quiero validar

    Returns:
        bool: Retorna True en caso de que el dato coincida con el tipo de dato. En caso contrario False
    """    
    tipo_dato = tipo_dato.lower()
    salio_bien = False
    if tipo_dato == "string" or tipo_dato == "entero" or tipo_dato == "flotante":
        if clave.lower() in heroe:
            match tipo_dato:
                case "entero":
                    if sanitizar_entero(heroe[clave]) != -1 and sanitizar_entero(heroe[clave]) != -2 and sanitizar_entero(heroe[clave]) != -3:
                        heroe[clave] = sanitizar_entero(heroe[clave])
                        salio_bien = True 
                case "string":
                    if sanitizar_string(heroe[clave]) != "N/A" and sanitizar_string(heroe[clave]) != "-":
                        heroe[clave] = sanitizar_string(heroe[clave])
                        salio_bien = True 
        
                case "flotante":
                    if sanitizar_flotante(heroe[clave]) != -1 and sanitizar_flotante(heroe[clave]) != -2 and sanitizar_flotante(heroe[clave]) != -3:
                        heroe[clave] = sanitizar_flotante(heroe[clave])
                        salio_bien = True 
        else:
            print("La clave especificada no existe en el héroe")
    else:
        print("Tipo de dato no reconocido")
    
    return salio_bien
        
# """
# 3.5. Crear la función 'stark_normalizar_datos’ la cual recibirá como parámetros:
# ● lista_heroes: la listas personajes
# La función deberá recorrer la lista de héroes y sanitizar los valores solo de las
# siguientes claves: ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e
# ‘inteligencia’
# ● Un vez finalizado el proceso mostrar el mensaje ‘Datos normalizados’,
# ● Validar que la lista de héroes no esté vacía para realizar sus acciones,
# caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
# ● La función no retorna nada
# ● Reutilizar la función sanitizar_dato
# """

def stark_normalizar_datos(lista_heroes:list):
    if len(lista_heroes) > 0:
        altura_normalizada = False
        peso_normalizado = False
        color_ojos_normalizado = False
        color_pelo_normalizado = False
        inteligencia_normalizado = False
        fuerza_normalizado = False
        
        for heroe in lista_heroes:
            if sanitizar_dato(heroe,"altura","flotante"):
                altura_normalizada = True
                
            if sanitizar_dato(heroe,"peso","flotante"):
                peso_normalizado = True
                
            if sanitizar_dato(heroe,"color_ojos","string"):
                color_ojos_normalizado = True
                
            if sanitizar_dato(heroe,"color_pelo","string"):
                color_pelo_normalizado = True
                
            if sanitizar_dato(heroe,"inteligencia","string"):
                inteligencia_normalizado = True

            if sanitizar_dato(heroe,"fuerza","entero"):
                fuerza_normalizado = True
        
        if altura_normalizada and peso_normalizado and color_ojos_normalizado and color_pelo_normalizado and inteligencia_normalizado and fuerza_normalizado:
            print("Datos normalizados")
    else:
        print("Error: Lista de héroes vacía")

# """ 
# 4.1. Crear la función ‘generar_indice_nombres’ la cual recibirá como parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá iterar la lista de personajes y generar una lista donde cada
# elemento es cada palabra que componen el nombre de los personajes.
# Por ejemplo la lista que se deberá retornar tiene la siguiente forma:
# [‘Howard’, ‘the’, ‘Duck’, ‘Rocket’, ‘Raccoon’, ‘Wolverine’, … ]
# La función deberá validar que:
# ● La lista contenga al menos un elemento
# ● Todos los elementos de lista_heroes sean del tipo diccionario
# ● Todos los elementos contengan la clave ‘nombre’
# En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no
# contiene el formato correcto’
# """
def generar_indice_nombres(lista_heroes:list)->list:
    
    salio_bien = False
    
    if len(lista_heroes) > 0:
        sublista = []
        nombre_personajes_partes = []

        for heroe in lista_heroes:
            if type(heroe) == dict and "nombre" in heroe:
                salio_bien = True
                
        if salio_bien:
            for heroe in lista_heroes:
                heroe["nombre"] = heroe["nombre"].replace("-", " ")
                dividir_nombre = heroe["nombre"].split(" ")
                sublista.append(dividir_nombre)
            
            for nombre in sublista:
                nombre_personajes_partes.extend(nombre)
                
            return nombre_personajes_partes
        else:
            print("El origen de datos no contiene el formato correcto") 
    else:
        print("El origen de datos no contiene el formato correcto")     

# """ 
# 4.2. Crear la función ‘stark_imprimir_indice_nombre’ la cual recibirá como
# parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá mostrar por pantalla el índice generado por la función
# generar_indice_nombres con todos los nombres separados con un guión.
# Por ejemplo:
# Howard-the-duck-Rocket-Raccoon-Wolverine…
# """

def stark_imprimir_indice_nombre(lista_heroes:list):
    lista_nombres = generar_indice_nombres(lista_heroes)
    separador = "-"
    nombres_con_separador = separador.join(lista_nombres)
    print(nombres_con_separador)
        

# """ 
# 5.1. Crear la función ‘convertir_cm_a_mtrs’ la cual recibirá como parámetro:
# ● valor_cm: Un número que representa una medida en centímetros
# La función deberá retornar el número recibido, pero convertido a la unidad
# metros. La función deberá validar que el número recibido sea un número
# flotante positivo, en caso de no serlo retornar -1
# """

def convertir_cm_a_mtrs(valor_cm:str):
    try:
        valor_cm = float(valor_cm)
        if valor_cm < 0:
            return -1
        else:
            valor_m = valor_cm / 100
            return valor_m
    except:
        return -1

# """ 
# 5.2. Crear la función ‘generar_separador’ la cual recibirá como parámetro
# ● patron: un carácter que se utilizará como patrón para generar el
# separador
# ● largo: un número que representa la cantidad de caracteres que va
# ocupar el separador.
# ● imprimir: un parámetro opcional del tipo booleano (por default definir
# en True)
# La función deberá generar un string que contenga el patrón especificado
# repitiendo tantas veces como la cantidad recibida como parámetro (uno junto
# al otro, sin salto de línea)
# Si el parámetro booleano recibido se encuentra en False se deberá solo
# retornar el separador generado. Si se encuentra en True antes de retornarlo,
# imprimirlo por pantalla
# La función deberá validar:
# ● Que el parámetro patrón tenga al menos un carácter y como máximo
# dos
# ● Que el parámetro largo sea un entero entre 1 y 235 inclusive
# En caso de no verificarse las validaciones devolver ‘N/A’
# Ejemplo de llamada:
# generar_separador(‘*’, 10)
# Ejemplo de salida:
# **********
# """

def generar_separador(patron:str, largo:int, imprimir:bool = True)->str:
    if (len(patron) >= 1 and len(patron) <= 2) and (largo >= 1 and largo <= 235):
        contador = 0
        separador = ""
        while contador < largo:
            separador += patron
            contador += 1
        if imprimir:
            print(separador)
        
        return separador
    else:
        return "N/A"

# """ 
# 5.3. Crear la función ‘generar_encabezado’ la cual recibirá como parámetro
# ● titulo: un string que representa el título de una sección de la ficha
# La función deberá devolver un string que contenga el título envuelto entre dos
# separadores (estimar el largo requerido para tu pantalla).
# Ejemplo de salida:
# ********************************************************************************
# PRINCIPAL
# ********************************************************************************
# La función deberá convertir el titulo recibido en todas letras mayúsculas
# """

def generar_encabezado(titulo:str):
    generar_separador("*",160,imprimir=True)
    print(titulo.upper())
    generar_separador("*",160,imprimir=True)
    

# """
# 5.4. Crear la función ‘imprimir_ficha_heroe’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del héroe
# La función deberá a partir los datos del héroe generar un string con el
# siguiente formato e imprimirlo por pantalla::
# ***************************************************************************************
# PRINCIPAL
# ***************************************************************************************
# NOMBRE DEL HÉROE: Spider-Man (S.M.)
# IDENTIDAD SECRETA: Peter Parker
# CONSULTORA: Marvel Comics
# CÓDIGO DE HÉROE : M-00000001
# ***************************************************************************************
# FISICO
# ***************************************************************************************
# ALTURA: 1,78 Mtrs.
# PESO: 74,25 Kg.
# FUERZA: 55 N
# ***************************************************************************************
# SEÑAS PARTICULARES
# ***************************************************************************************
# COLOR DE OJOS: Hazel
# COLOR DE PELO: Brown
# """
def imprimir_ficha_heroe(heroe:dict)->None:
    generar_encabezado("Principal")
    print(f"NOMBRE DEL HÉROE: {heroe['nombre']} ({heroe['iniciales']})\nIDENTIDAD SECRETA: {heroe['identidad']}\nCONSULTORA: {heroe['empresa']}\nCÓDIGO DE HÉROE: {heroe['codigo_heroe']}")
    generar_encabezado("Fisico")
    print(f"ALTURA: {heroe['altura']}\nPESO: {heroe['peso']}\nFUERZA: {heroe['fuerza']}")
    generar_encabezado("Señas particulares")
    print(f"COLOR DE OJOS: {heroe['color_ojos']}\nCOLOR DE PELO: {heroe['color_pelo']}")
    

# """ 
# 5.5. Crear la función 'stark_navegar_fichas’ la cual recibirá como parámetros:
# ● lista_heroes: la listas personajes
# La función deberá comenzar imprimiendo la ficha del primer personaje de la
# lista y luego solicitar al usuario que ingrese alguna de las siguientes opciones:
# [ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir
# ● Si el usuario ingresa ‘1’: se debe mostrar el héroe que se encuentra en
# la posición anterior en la lista (en caso de estar en el primero, ir al
# último)
# ● Si el usuario ingresa ‘2’: se debe mostrar el héroe que se encuentra en
# la posición siguiente en la lista (en caso de estar en el último, ir al
# primero)
# ● Si ingresa ‘S’: volver al menú principal
# ● Si ingresa cualquier otro valor, volver a mostrar las opciones hasta que
# ingrese un valor válido
# """

def stark_navegar_fichas(lista_heroes:list, ):

    indice = 0
    imprimir_ficha_heroe(lista_heroes[0])
    while True:
        
        while True:
            opcion = input("\n[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir\n").upper()
            if opcion == "1" or opcion == "2" or opcion == "S":
                break
            else:
                imprimir_ficha_heroe(lista_heroes[indice])
        match opcion:
            case "1":
                    indice -= 1
                    if indice < 0:
                        indice = len(lista_heroes) - 1
                    imprimir_ficha_heroe(lista_heroes[indice])
            case "2":
                indice += 1
                if indice >= len(lista_heroes):
                    indice = 0
                imprimir_ficha_heroe(lista_heroes[indice])
            case "S":
                print("Volviendo al menu principal...")
                break
    
def imprimir_menu():
    print("\n------------------->    STARK MARVEL APP 3   <-------------------\n")
    print(" 1 -> Imprimir la lista de nombres junto con sus iniciales\n 2 -> Generar códigos de héroes\n 3 -> Normalizar Datos\n 4 -> Imprimir indices de nombres\n 5 -> Navegar fichas\n 6 -> Salir")


# """ 
# 6.2. Crear la función ‘stark_menu_principal'. No recibe parámetros.
# La función deberá imprimir el menú de opciones y le pedirá al usuario que
# ingrese una.
# La función deberá retornar la respuesta del usuario
# """
def stark_menu_principal():
    
    imprimir_menu()
    opcion = input("\nIngrese una opcion\n")
    return opcion


# """ 
# 6.3. Crear la función ‘stark_marvel_app_3’ la cual recibirá como parámetro:
# ● lista_heroes: la lista de personajes
# La función se encargará de la ejecución principal de nuestro programa.
# Utilizar if/elif o match según prefiera (match solo para los que cuentan con
# python 3.10+).
# Debe informar por consola en caso de seleccionar una opción incorrecta y
# volver a pedir el dato al usuario.
# Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.
# """

def stark_marvel_app_3(lista_heroes:list):
    
    if len(lista_heroes) > 0:
        flag_datos = False
        flag_codigos = False
        flag_iniciales = False
        while True:
            os.system("cls")
            while True:
                try:
                    opcion = int(stark_menu_principal())
                    if opcion >= 1 and opcion <= 6:
                        break
                    else:
                        print("Opcion incorrecta")
                except ValueError:
                    print("ERROR! No se puede convertir a entero")
            match opcion:
                case 1:
                    if flag_datos:
                        stark_imprimir_nombres_con_iniciales(lista_heroes)
                        flag_iniciales = True
                    else:
                        print("Primero se debe normalizar los datos")
                case 2:
                    if flag_datos:
                        stark_generar_codigos_heroes(lista_heroes)
                        flag_codigos = True
                    else:
                        print("Primero se debe normalizar los datos")
                case 3:
                    if not flag_datos:
                        stark_normalizar_datos(lista_heroes)
                        flag_datos = True
                    else:
                        print("Ya se normalizaron los datos")
                case 4:
                    if flag_datos:
                        stark_imprimir_indice_nombre(lista_heroes)
                    else:
                        print("Primero se debe normalizar los datos")
                case 5:
                    if flag_datos:
                        if flag_iniciales:
                            if flag_codigos:
                                stark_navegar_fichas(lista_heroes)
                            else:
                                print("Primero debe inicializar la clave codigo")
                        else:
                            print("Primero debe inicializar las iniciales")
                    else:
                        print("Primero se debe normalizar los datos")
                case 6:
                    while True:
                        confirmacion = input("¿Seguro desea salir? s/n\n").lower()
                        if confirmacion == "s" or confirmacion == "n": 
                            break
                    if confirmacion == "s":
                        break
            os.system("pause")
    else:
        print("Error! Lista vacia")