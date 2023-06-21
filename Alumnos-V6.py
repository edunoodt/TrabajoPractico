#######################################################################################
# TRABAJO PRÁCTICO DE TÉCNICAS DE PROGRAMACIÓN
# PROFESORA: Gloria Chocobar
#
# SISTEMA DE ALUMNOS-MateriaS
# INTEGRANTES DEL GRUPO VINTAGE:
# Juan Janczuk
# Eduardo Noodt
# Sergio Conte
# Juan Faucheux
#
#####################################################################################
import re  # para ejecutar expresiones regulares
import pprint  # permite formatear objetos para luego ser impresos
import textwrap  # permite formatear parrafos de texto
# Este módulo proporciona varias funciones relacionadas con el tiempo.
import time
import os  # Este módulo provee una manera versátil de usar funcionalidades dependientes del sistema operativo
import csv  # El módulo csv implementa clases para leer y escribir datos tabulares en formato TXT.
from cgi import print_form  # imprime en formato html form


# INICIO DE PROGRAMA
padron = []  # genera la lista que se utilizará durante todo el programa
archivo = ""
nombre_archivo = "padron"

# Función para subrayar textos

def subrayar(*textos):
    """
     Permite el subrayado de múltiples textos y retorna el texto subrayado como cadena.
    :return: Retorna una cadena que contiene el o los texto(s) de entrada con un formato de subrayado aplicado a ellos usando
    Códigos de escape ANSI.
    """
    return " ".join("\033[4m" + texto + "\033[0m" for texto in textos)

###########################################################################
# FUNCION CARGA INICIAL DEL PADRON DE PERSONAS DESDE EL ARCHIVO padron.txt
###########################################################################

def archivo_carga_inicial_personas(padron):
    """
    Esta función carga un archivo de texto que contiene información acerca de los alumnos en una lista de diccionarios.

    :param padron: Una lista que se poblara con diccionarios que representan a individuos en un registro. Cada diccionario
    contendrá información como el nombre, DNI, Domicilio y las dos Notas de cada uno de los dos cursos. Esta función lee un
    archivo de texto con esta información y completa la lista con los diccionarios correspondientes.
    """

    global archivo
    archivo = "Alumnos.txt"  # Cambio de extensión a .txt
    #
    #DNI
    #Nombre
    #Apellido
    #Domicilio
    #Materia1
    #Materia1 - Nota1
    #Materia1 - Nota2
    #Materia1 - Promedio
    #Materia1 - Situacion
    #Materia2
    #Materia2 - Nota1
    #Materia2 - Nota2
    #Materia2 - Promedio
    #Materia2 - Situacion
    #
    try:
        with open(archivo, 'r', encoding='latin-1') as txt_file:  # Apertura como archivo de texto
            print("Cargando archivo: " + archivo)
            print("Aguarde.....")
            time.sleep(2)
            # Utilizando DictReader con delimitador de tabulaciones
            reader = csv.DictReader(txt_file, delimiter='\t')

            for row in reader:
                persona = {
                    "DNI": int(row["DNI"]),
                    "Nombre": row["Nombre"],
                    "Apellido": row["Apellido"],
                    "Domicilio": row["Domicilio"],
                    "Materia1": row["Materia1"],
                    "Materia1-Nota1": row["Materia1-Nota1"],
                    "Materia1-Nota2": row["Materia1-Nota2"],
                    "Materia1-Promedio": row["Materia1-Promedio"],
                    "Materia1-Situacion": row["Materia1-Situacion"],
                    "Materia2": row["Materia2"],
                    "Materia2-Nota1": row["Materia2-Nota1"],
                    "Materia2-Nota2": row["Materia2-Nota2"],
                    "Materia2-Promedio": row["Materia2-Promedio"],
                    "Materia2-Situacion": row["Materia2-Situacion"],
                }

                padron.append(persona)

        print("Se ha cargado el archivo de texto en el sistema correctamente.")

    except FileNotFoundError:
        print("No se encontró el archivo de texto.")
    except UnicodeDecodeError:
        print("Ocurrió un error al cargar las personas del archivo de texto: Error de decodificación de caracteres.")
    except Exception as e:
       print("Ocurrió un error al cargar las personas del archivo de texto:", str(e))

#######################################
# OPCION 1: ALTAS DE ALUMNOS Y MateriaS
#######################################

def cargar_persona(padron):
    """
    Esta función permite al usuario ingresar información sobre una persona, incluyendo su nombre, dirección
    y Notas de dos asignaturas, y agrega esta información a una lista.

    :param padron: `padron` es una lista que contiene a todas las personas que han sido registradas en el
    sistema. Cada persona está representada por un diccionario con su información personal y registros académicos.
    Esta función agrega una nueva persona a la lista `padron`.
    :return: La función no devuelve explícitamente nada, pero agrega un diccionario que representa a una persona
    a una lista llamada "padron".
    """
    persona = {}
    os.system('cls' if os.name == 'nt' else 'clear')
    global DNI
    titulo = subrayar(f"Ingrese Datos del Nuevo Alumno y sus Materias:")    
    print(titulo)
    print("")
    Apellido = input(f"Ingrese el Apellido: ")
    persona["Apellido"] = Apellido.capitalize()

    Nombre = input(f"Ingrese los Nombre: ")
    persona["Nombre"] = Nombre.capitalize()

    DNI = int(input(f"Ingrese el DNI: "))
    # Chequear si el DNI ya existe en la lista
    persona_encontrada = mostrar_persona_a_modificar(padron, DNI)
    if persona_encontrada is not None:
        print("ERROR: El DNI ya existe en la base. Por favor, reintente.")
        mostrar_persona(padron, DNI)
        time.sleep(5)
        cargar_persona(padron)
        return

    persona["DNI"] = DNI


    Domicilio = input(f"Ingrese el Domicilio: ")
    persona["Domicilio"] = Domicilio.capitalize()

    campos = [
        ("Materia1", "Ingrese el nombre de la Materia 1"),
        ("Materia2", "Ingrese el nombre de la Materia 2"),
        ]

    for campo, mensaje in campos:
        valor = input(f"{mensaje}: ")
        persona[campo] = valor.capitalize()
        # Verificar si el nombre de la Materia es nulo y asignar valores de 0 a las Notas
        if valor == "":
            persona[f"{campo}-Nota1"] = "0.00"
            persona[f"{campo}-Nota2"] = "0.00"
            persona[f"{campo}-Promedio"] = "0.00"
            persona[f"{campo}-Situacion"] = "No Regularizada"
            continue

        # Solicitar Notas y situación de la Materia
        Nota1_mensaje = f"Ingrese la primera Nota de {valor.upper()} "
        Nota2_mensaje = f"Ingrese la segunda Nota de {valor.upper()} "
        Situacion_mensaje = f"Ingrese la Situación de {valor} "

        while True:
            try:
                Nota1 = float(input(f"{Nota1_mensaje}: "))
                if Nota1 < 0 or Nota1 > 10:
                    raise ValueError("La Nota debe estar entre 0 y 10")
                break
            except ValueError as e:
                print(f"Error: {str(e)}")

        while True:
            try:
                Nota2 = float(input(f"{Nota2_mensaje}: "))
                if Nota2 < 0 or Nota2 > 10:
                    raise ValueError("La Nota debe estar entre 0 y 10")
                break
            except ValueError as e:
                print(f"Error: {str(e)}")

        Promedio = (Nota1 + Nota2) / 2
        Situacion = "Regularizada" if Promedio >= 6.00 else "No Regularizada"
        persona[f"{campo}-Nota1"] = format(Nota1, ".2f")
        persona[f"{campo}-Nota2"] = format(Nota2, ".2f")
        persona[f"{campo}-Promedio"] = format(Promedio, ".2f")
        persona[f"{campo}-Situacion"] = Situacion
    if not persona:
        print("No se ha ingresado ningún dato.")
        return None

    for i in range(1, 3):
        Materia = persona.get(f"Materia{i}", "")
        Nota1 = float(persona.get(f"Materia{i}-Nota1", 0))
        Nota2 = float(persona.get(f"Materia{i}-Nota2", 0))
        Nota1 = format(Nota1, ".2f")  # Formateo de Nota1
        Nota2 = format(Nota2, ".2f")  # Formateo de Nota2
        Promedio = float(f"{((float(Nota1) + float(Nota2)) / 2):.2f}")
        Situacion = "Regularizada" if Promedio >= 6.00 else "No Regularizada"
        print(f"Materia {i}: {Materia} Nota 1: {Nota1} Nota 2: {Nota2} Promedio: {format(Promedio, '.2f')} Situación: {Situacion}")

    padron.append(persona)


# FIN OPCION 1: ALTAS DE PERSONAS Y MateriaS
##
####################################
# OPCION 2: BAJAS
####################################
#


def borrar_persona(padron):
    """
    Esta función elimina los datos de una persona de una lista de registros basándose en su número de identificación
    después de confirmar con el usuario.

    :param padron: Es la lista de diccionarios que representan un registro de estudiantes, donde cada diccionario
    contiene información sobre un estudiante, como su nombre, edad y DNI (número de identificación nacional)
    :return: None.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    #print("Función borrar_persona()")
    DNI = int(input("Ingrese el DNI del Alumno: "))
    mostrar_persona(padron, DNI)
    
    # Agregar confirmación de borrado
    confirmacion = input("¿Confirma que desea eliminar los datos de este Alumno? (S/N): ")

    if confirmacion.lower() == "s":
        for persona in padron:
            if persona["DNI"] == DNI:
                padron.remove(persona)
                print("Datos eliminados correctamente.")
                print("Registro borrado:", persona)
                return

        print("No se encontró un Alumno con ese DNI.")
    else:
        print("El borrado de los datos del Alumno ha sido cancelado.")
    print("Aguarde....")
    time.sleep(2)
# FIN OPCION 2: BAJAS
#
######################################################
# OPCION 3: MODIFICACION DE PERSONAS Y SUS MateriaS
######################################################


def mostrar_persona_a_modificar(padron, DNI):
    """
    La función busca a una persona en una lista por su número de identificación y devuelve su información.

    :param padron: una lista de diccionarios que representa un registro o lista de votantes
    :param DNI: El parámetro DNI es una cadena que representa el número de identificación nacional de una
    persona. Se utiliza para buscar a una persona específica en una lista de diccionarios (padron) que contiene
    información sobre varias personas, incluido su DNI
    :return: la persona encontrada en la lista "padron" con el "DNI" (número de identificación) dado. Si no se
    encuentra ninguna persona con ese "DNI", la función devuelve None.
    """
    # Buscar la persona en el padrón
    global encontrado
    global persona
    global persona_encontrada

    persona_encontrada = None

    # Buscar la persona en el padrón
    encontrado = False
    for persona in padron:
        if persona["DNI"] == DNI:
            encontrado = True
            persona_encontrada = persona
            break

    return persona_encontrada


# -----FUNCION ESPECIFICA PARA MODIFICAR DATOS
def modificar_persona(padron):
    """
    Esta función permite al usuario modificar los datos de una persona en una base de datos, incluyendo su
    nombre, dirección y calificaciones en dos Materias diferentes.

    :param padron: Es una lista de diccionarios que contiene información sobre estudiantes, como nombre,
    dirección y calificaciones.
    :return: La función no tiene una declaración de retorno, por lo que devuelve None de forma predeterminada.
    """
    global encontrado
    encontrado = False
    DNI = int(input("Ingrese el DNI del Alumno cuyos datos desea modificar: "))
    global persona
    persona = mostrar_persona_a_modificar(padron, DNI)

    if persona is not None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print(f"Va a modificar los datos de " +
              persona["Apellido"] + ", " + persona["Nombre"])
        print("Aguarde....")
        time.sleep(2)
    else:
        print("No se encontró un Alumno con ese DNI.")
        print("Aguarde....")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return

# Opciones del menú
    Materia1 = persona['Materia1']
    Materia2 = persona['Materia2']
    opciones_modif = [
        f"[APE]. " +
        f"Modificar Apellido de {persona['Apellido']}, {persona['Nombre']}",
        f"[NOM]. " +
        f"Modificar Nombre {persona['Apellido']}, {persona['Nombre']}",
        f"[DOM]. " +
        f"Modificar Domicilio de {persona['Apellido']}, {persona['Nombre']}",
        f"[MA1]. " + f"Modificar el Nombre de la Materia 1: {Materia1}",
        f"[N11]. " + f"Modificar la Primera Nota de {Materia1}",
        f"[N21]. " + f"Modificar la Segunda Nota de {Materia1}",
        f"[MA2]. " + f"Modificar el Nombre de la Materia 2: {Materia2}",
        f"[N12]. " + f"Modificar la Primera Nota de {Materia2}",
        f"[N22]. " + f"Modificar la Segunda Nota de {Materia2}",
        f"[ V ]. " + f"Volver al Menú Principal ",
        f" "
    ]

    # Calcular la longitud máxima de las opciones en cada columna
    max_length = max(len(option) for option in opciones_modif)
    half_length = max_length // 2  # Longitud deseada para cada columna

    # Dividir las opciones en dos columnas
    columnas = list(zip(opciones_modif[:len(
        opciones_modif)//2], opciones_modif[len(opciones_modif)//2:]))

    # Imprimir las opciones en dos columnas
    titulo = subrayar(f"Ingrese la operación que desea realizar:")
    print(titulo)

    for column in columnas:
        for option in column:
            print(option.ljust(max_length), end='   ')
        print()

    texto_estilizado = opciones_modif

    while True:
        try:
            # Solicitar la opción al usuario
            #opcion_str = input(texto_estilizado).upper()
            opcion_str = str(input("¿Su opción? ")).upper()
            # Eliminar caracteres de formato ANSI
            opcion_str = re.sub(r"\x1b\[\d+(?:;\d+)*m", "", opcion_str)
            if opcion_str == "":
                opcion_str = -1
            else:
                opcion = (opcion_str)

# MODIFICACIONES DATOS ALUMNOS
            if opcion_str == 'APE':
                persona["Apellido"] = input(
                    "Ingrese el nuevo Apellido: ").upper()

            elif opcion_str == 'NOM':
                persona["Nombre"] = input("Ingrese Nombre: ").upper()

            elif opcion_str == 'DOM':
                persona["Domicilio"] = str(
                    input("Ingrese el nuevo Domicilio: "))

            elif opcion_str == 'DNI':

                if persona_encontrada is not None:
                    nuevo_DNI = input("Ingrese el nuevo DNI: ")
                    persona_encontrada["DNI"] = int(nuevo_DNI)
                    print("DNI modificado correctamente.")
                    print("Aguarde....")
                    time.sleep(4)
                else:
                    print("No se encontró un Alumno con ese DNI.")
                    print("Aguarde....")
                    time.sleep(4)

# MODIFICACIONES Materia 1
            elif opcion_str == 'MA1':
                #print(f"Nombre actual de la Materia :   {str(persona['Materia1']).upper()}".ljust(10))
                persona["Materia1"] = input(
                    f"Cambiar nombre de la Materia {persona['Materia1'].upper()}:   ".ljust(10)).capitalize()

            elif opcion_str == 'N11':
                Nota = float(input(
                    f"Cambiar la primera Nota de la Materia {persona['Materia1']}:   ".ljust(10)))
                persona["Materia1-Nota1"] = format(Nota, ".2f")

            elif opcion_str == 'N21':
                Nota = float(input(
                    f"Cambiar la segunda Nota de la Materia {persona['Materia1']}:   ".ljust(10)))
                persona["Materia1-Nota2"] = format(Nota, ".2f")

# MODIFICACIONES Materia 2
            elif opcion_str == 'MA2':
                persona["Materia2"] = input(
                    "Ingrese el nombre de la Materia 2: ").upper()

            elif opcion_str == 'N12':
                Nota = float(input(
                    f"Cambiar la primera Nota de la Materia {persona['Materia2']}:   ".ljust(10)))
                persona["Materia2-Nota1"] = format(Nota, ".2f")

            elif opcion_str == 'N22':
                Nota = float(input(
                    f"Cambiar la segunda Nota de la Materia {persona['Materia2']}:   ".ljust(10)))
                persona["Materia2-Nota2"] = format(Nota, ".2f")

            elif opcion_str == 'V':
                print("Saliendo del Menú...")
                mostrar_persona(padron, DNI)
                return
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
                print("Aguarde....")
                time.sleep(2)

        except ValueError:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# FIN OPCION 3: MODIFICACION
#
#################################################
# OPCION 4: MOSTRAR DATOS DE UNA PERSONA (OK)
#################################################


def mostrar_persona(padron, DNI):
    """
    La función "mostrar_persona" busca a una persona en una lista de diccionarios y muestra su información,
    incluyendo las Notas y estado de dos Materias.

    :param padron: una lista de diccionarios que representa una lista de estudiantes, donde cada diccionario
    contiene información sobre un estudiante, como su nombre, número de identificación, dirección y Notas en
    diferentes Materias.
    :param DNI: el parámetro "DNI" representa el "Documento Nacional de Identidad". Este código se utiliza
    como clave para buscar a una persona en una lista de registros (padron).
    :return: no retorna nada si la persona no se encuentra en la lista "padron", y devuelve los detalles de la
    persona y sus Notas si se encuentra.
    """
    # Buscar la persona en el padrón
    global encontrado
    for persona in padron:
        if persona["DNI"] == DNI:
            print(f"Datos del Alumno:")
            print("")
            # DATOS DEL ALUMNO
            print(f"Apellido: {persona['Apellido']}".ljust(39),
                  f"Nombre: {persona['Nombre']}".ljust(35),
                  f"D.N.I.: {persona['DNI']}".ljust(40),
                  f"Domicilio: {persona['Domicilio']}".ljust(30)
                  )
            print("")
            # TITULOS SUBRAYADOS
            print(subrayar(
                f"Materia".ljust(38),
                f"".ljust(0),
                f"PRIMERA Nota".ljust(12),
                f"".ljust(0),
                f"SEGUNDA Nota".ljust(12),
                f"".ljust(0),
                f"Promedio".ljust(20),
                f"Situacion".ljust(10)
                ))

            #INICIO LISTADO DE MateriaS/NotaS/Promedio/Situacion. Materia 1 (OK)
            persona['Materia1-Promedio'] = f"{((float(persona['Materia1-Nota1']) + float(persona['Materia1-Nota2'])) / 2):.2f}"
            persona['Materia1-Situacion'] = "Regularizada" if float(persona['Materia1-Promedio']) >= 6.00 else "No Regularizada"
            print(f"{persona['Materia1']}".ljust(39),
                  f"{persona['Materia1-Nota1']}".ljust(12),
                  f"".ljust(0),
                  f"{persona['Materia1-Nota2']}".ljust(12),
                  f"".ljust(0),
                  f"{persona['Materia1-Promedio']}".ljust(20),
                  f"{persona['Materia1-Situacion']}".ljust(12)
                  )

            #INICIO LISTADO DE MateriaS/NotaS/Promedio/Situacion. Materia 2 (OK)
            persona['Materia2-Promedio'] = f"{((float(persona['Materia2-Nota1']) + float(persona['Materia2-Nota2'])) / 2):.2f}"
            persona['Materia2-Situacion'] = "Regularizada" if float(persona['Materia2-Promedio']) >= 6.00 else "No Regularizada"
            print(f"{persona['Materia2']}".ljust(39),
                  f"{persona['Materia2-Nota1']}".ljust(12),
                  f"".ljust(0),
                  f"{persona['Materia2-Nota2']}".ljust(12),
                  f"".ljust(0),
                  f"{persona['Materia2-Promedio']}".ljust(20),
                  f"{persona['Materia2-Situacion']}".ljust(12)
                  )
            print("Operacion a Confirmar en el paso que sigue, dos segundos por favor....")
            print("Aguarde....")
            time.sleep(2)
            encontrado=True
            return

    # Si no se encuentra la persona
    print(f"No se encontró un Alumno con ese DNI.")
    encontrado = False
# FIN OPCION 4
#

#
##########################################################
# OPCION 5: MUESTRA EL CONTENIDO COMPLETO DEL PADRON
##########################################################


def mostrar_padron(padron):
    """
    La función "mostrar_padron" muestra una lista de alumnos con su información, permitiendo al usuario 
    ver la lista en segmentos y confirmar si desea seguir viendo.

    :param padron: Lista de diccionarios que contiene información sobre los estudiantes, como su nombre,
    número de identificación y calificaciones.
    """
    # print("\033[5m")  # Código para fuente de tamaño menor
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Lista completa de Alumnos:")
    conteo = 0
    for i, persona in enumerate(padron, start=1):
        print(f"Registro {i}: ", end="")
        for campo, valor in persona.items():
            #valor = "M" if campo == "Materia1" and valor else valor
            print(f"{campo.upper()}: {valor} | ", end="")
        print("\n------------------------------")
        conteo = conteo+1
        if conteo == 10:
            conteo = 0
            confirmacion = input("¿Continua visualizando? (S/N): ")
            if confirmacion.lower() == "n":
                break
    print("\033[0m")  # Código para restaurar el tamaño de fuente
# FIN OPCION 6
#
#########################################################################
# GUARDA EL RESULTADO DE LA OPERACION RECIENTE (ALTA, BAJA, MODIFICACION)
# EN EL ARCHIVO GENERAL
#########################################################################


def guardar_padron_en_archivo(padron):
    """

    La función "guardar_padron_en_archivo" guarda un diccionario de datos en un archivo de texto utilizando
    el módulo txt y solicita al usuario una confirmación antes de hacerlo.

    :param padron: Es una lista de diccionarios que representa un padrón de votantes. Cada diccionario
    contiene información sobre un votante, como su nombre, número de identificación y preferencia de voto.
    :return: nada (es decir, None). Utiliza la declaración "return" solo para salir de la función después
    de que los cambios se hayan guardado o el usuario haya decidido no guardarlos.
    """
    global archivo
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        confirmacion = input(
            "¿Desea guardar los cambios en el archivo " + archivo + "? (S/N): ")
        if confirmacion.lower() == "s":
            try:
                print("Archivo: " + archivo)
                with open(archivo, "w") as txt_file:
                    fieldnames = padron[0].keys()
                    writer = csv.DictWriter(
                        txt_file, fieldnames=fieldnames, delimiter='\t')
                    writer.writeheader()
                    for persona in padron:
                        # Convertir los valores a str
                        persona_str = {k: str(v) for k, v in persona.items()}
                        writer.writerow(persona_str)

                print(
                    "Se han guardado los cambios en el archivo de texto correctamente.")
                return

            except Exception as e:
                print(
                    "Ocurrió un error al guardar los cambios en el archivo de texto:", str(e))
                break  # Salir del bucle en caso de error

        elif confirmacion.lower() == "n":
            print("Los cambios no han sido guardados.")
            return

        else:
            print("Opción inválida. Por favor, seleccione 'S' o 'N'.")

##############################################################################


##############################################
# CUERPO PRINCIPAL DEL PROGRAMA
##############################################

# INVOCA A LA FUNCION DE CARGA INICIAL QUE SE ENCUENTRA DEFINIDA AL PRINCIPIO DE ESTE PROGRAMA.
# le pasa como parametro la lista padron vacia
archivo_carga_inicial_personas(padron)

##############################
# Menú de opciones
##############################
"""
Este código implementa un programa basado en menús para gestionar una lista de personas.
Proporciona opciones para agregar, modificar, eliminar y mostrar personas de la lista. 
También permite importar una lista de personas desde un archivo TXT. 
El programa utiliza funciones para realizar estas operaciones y guarda los cambios en un archivo después
de cada operación. También incluye manejo de errores para gestionar entradas inválidas del usuario.
"""

# ------------------Definir las opciones del menú con diferentes estilos
titulo = subrayar(f"Ingrese la operación que desea realizar:")

opcion1 = f"1. " + f"Dar de Alta a una Alumno"
opcion2 = f"2. " + f"Modificar datos de un Alumno"
opcion3 = f"3. " + f"Eliminar datos de un Alumno"
opcion4 = f"4. " + f"Mostrar datos de un Alumno"
opcion5 = f"5. " + f"Visualizar listado completo de Alumnos"
opcion7 = f"0. " + f"Salir del Menú "
opcion8 = f"¿Su opción? " + f"-->>> "

# -------------------Concatenar las líneas del menú
texto_estilizado_0 = f"{titulo}\n{opcion1}\n{opcion2}\n{opcion3}\n{opcion4}\n{opcion5}\n{opcion7}\n{opcion8}"

# -------------------- Solicitar la opción al usuario
while True:
    try:

        # Para limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        opcion = input(texto_estilizado_0)
        #
        # ALTAS
        if opcion == "1":
            cargar_persona(padron)
            mostrar_persona(padron,DNI)
            input("Presione ENTER para proseguir")
            # Guardar los cambios al agregar una persona
            guardar_padron_en_archivo(padron)
            input("Presione ENTER para volver al Menú...")
        # ---------
        #
        # MODIFICACION
        #
        elif opcion == "2":
            modificar_persona(padron)
            if encontrado:
                # Guardar los cambios al modificar una persona
                guardar_padron_en_archivo(padron)
            input("Presione ENTER para volver al Menú...")
        # -----------------
        # BAJA
        #
        elif opcion == "3":
            borrar_persona(padron)
            if encontrado:
                # Guardar los cambios al eliminar los datos de una persona
                guardar_padron_en_archivo(padron)
            input("Presione ENTER para volver al Menú...")
        # ------------------

        elif opcion == "4":
            DNI= int(input("Ingrese el DNI de la persona a mostrar: "))
            mostrar_persona(padron, DNI)
            input("Presione ENTER para volver al Menú...")
        elif opcion == "5":
            mostrar_padron(padron)
            input("Presione ENTER para volver al Menú...")
        elif opcion == "0":
            print("Saliendo del Menú...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    except ValueError:
        print("Opción inválida. Por favor, seleccione una opción válida.")


input("Presione ENTER para continuar...")
print()  # Salto de línea para separar el menú de la próxima operación
print("Fin del programa")

# Para limpiar la pantalla
os.system('cls' if os.name == 'nt' else 'clear')

# FIN DE PROGRAMA
