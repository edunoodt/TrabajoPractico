#TRABAJO PRÁCTICO DE TÉCNICAS DE PROGRAMACIÓN
#PROFESORA: Gloria Chocobar
#
#SISTEMA DE ALUMNOS-MATERIAS
#INTEGRANTES DEL GRUPO VINTAGE:
    #Juan Janczuk
    #Eduardo Noodt
    #Sergio Conte
    #Juan Faucheux
#
#
#INICIO DE PROGRAMA
padron = [] #genera la lista que se utilizará durante todo el programa
from cgi import print_form #imprime en formato html form
import csv #El módulo csv implementa clases para leer y escribir datos tabulares en formato CSV.
import os #Este módulo provee una manera versátil de usar funcionalidades dependientes del sistema operativo
import time #Este módulo proporciona varias funciones relacionadas con el tiempo.
import textwrap #permite formatear parrafos de texto
import pprint #permite formatear objetos para luego ser impresos
import re #para ejecutar expresiones regulares
archivo=""
nombre_archivo="padron"

# Función para subrayar el texto
def subrayar(*textos):
    return " ".join("\033[4m" + texto + "\033[0m" for texto in textos)

###########################################################################
#FUNCION CARGA INICIAL DEL PADRON DE PERSONAS DESDE EL ARCHIVO padron.csv
###########################################################################
def archivo_carga_inicial_personas(padron):
    #declara la variable archivo como global para que este disponible fuera del scope de la funcion
    #archivo contiene el nombre del archivo externo donde se alojan los datos
    #en este caso considera que es un archivo con separador ;
    global archivo
    archivo = "padron.csv"

    try:
        with open(archivo, 'r', encoding='utf-8', newline='') as csv_file:
            print("Cargando archivo: " + archivo)
            print("Aguarde.....")
            time.sleep(2)
            reader = csv.DictReader(csv_file, delimiter=';')

            for row in reader:
                # Crear un diccionario para cada persona y agregarlo al padrón
                persona = {
                    "apellido": row["apellido"], #toma el valor de la columna con row[<nombre columna>]
                    "nombres": row["nombres"],
                    "dni": int(row["dni"]),
                    "domicilio": row["domicilio"],
                    "materia1": row["materia1"],
                    "materia1_nota1": (row["materia1_nota1"]),
                    "materia1_nota2": (row["materia1_nota2"]),
                    "materia1_promedio": (row["materia1_promedio"]),
                    "materia1_situacion": (row["materia1_situacion"]),
                    "materia2": (row["materia2"]),
                    "materia2_nota1": (row["materia2_nota1"]),
                    "materia2_nota2": (row["materia2_nota2"]),
                    "materia2_promedio": (row["materia2_promedio"]),
                    "materia2_situacion": row["materia2_situacion"],
                }

                padron.append(persona)

        print("Se ha cargado el archivo CSV en el sistema correctamente.")

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    except UnicodeDecodeError:
        print("Ocurrió un error al cargar las personas del archivo CSV: Error de decodificación de caracteres.")
    except Exception as e:
        print("Ocurrió un error al cargar las personas del archivo CSV:", str(e))


#######################################
# OPCION 1: ALTAS DE ALUMNOS Y MATERIAS
#######################################
def cargar_persona(padron):
    persona = {}
    os.system('cls' if os.name == 'nt' else 'clear')

    apellido = input(f"Ingrese el apellido: ")
    persona["apellido"] = apellido.capitalize()

    nombres = input(f"Ingrese los nombres: ")
    persona["nombres"] = nombres.capitalize()

    dni = int(input(f"Ingrese el DNI: "))
    persona["dni"] = dni

    domicilio = input(f"Ingrese el domicilio: ")
    persona["domicilio"] = domicilio.capitalize()

    campos = [
        ("materia1", "Ingrese el nombre de la materia 1"),
        ("materia2", "Ingrese el nombre de la materia 2"),
    ]

    for campo, mensaje in campos:
        valor = input(f"{mensaje}: ")
        persona[campo] = valor.capitalize()


        # Solicitar notas y situación de la materia
        nota1_mensaje = f"Ingrese la primera nota de {valor.upper()} "
        nota2_mensaje = f"Ingrese la segunda nota de {valor.upper()} "
        situacion_mensaje = f"Ingrese la Situación de {valor} "
        
        while True:
            try:
                nota1 = float(input(f"{nota1_mensaje}: "))
                if nota1 < 0 or nota1 > 10:
                    raise ValueError("La nota debe estar entre 0 y 10")
                break
            except ValueError as e:
                print(f"Error: {str(e)}")

        while True:
            try:
                nota2 = float(input(f"{nota2_mensaje}: "))
                if nota2 < 0 or nota2 > 10:
                    raise ValueError("La nota debe estar entre 0 y 10")
                break
            except ValueError as e:
                print(f"Error: {str(e)}")

        promedio = (nota1 + nota2) / 2
        situacion = "Regularizada" if promedio >= 6.00 else "No Regularizada"
        persona[f"{campo}_nota1"] = format(nota1, ".2f")
        persona[f"{campo}_nota2"] = format(nota2, ".2f")
        persona[f"{campo}_promedio"] = format(promedio, ".2f")
        persona[f"{campo}_situacion"] = situacion
    if not persona:
        print("No se ha ingresado ningún dato.")
        return None

    for i in range(1, 3):
        materia = persona.get(f"materia{i}", "")
        nota1 = float(persona.get(f"materia{i}_nota1", 0))
        nota2 = float(persona.get(f"materia{i}_nota2", 0))
        nota1 = format(nota1, ".2f")  # Formateo de nota1
        nota2 = format(nota2, ".2f")  # Formateo de nota2
        promedio = float(f"{((float(nota1) + float(nota2)) / 2):.2f}")
        situacion = "Regularizada" if promedio >= 6.00 else "No Regularizada"
        print(f"Materia {i}: {materia} Nota 1: {nota1} Nota 2: {nota2} Promedio: {format(promedio, '.2f')} Situación: {situacion}")

    padron.append(persona)

#####FIN OPCION 1: ALTAS DE PERSONAS Y MATERIAS
##
####################################
# OPCION 2: BAJAS
####################################
#
def borrar_persona(padron):
    os.system('cls' if os.name == 'nt' else 'clear')
    #print("Función borrar_persona()")
    dni = int(input("Ingrese el DNI del Alumno: "))
    mostrar_persona(padron, dni)

    # Agregar confirmación de borrado
    confirmacion = input("¿Confirma que desea eliminar los datos de este Alumno? (S/N): ")

    if confirmacion.lower() == "s":
        for persona in padron:
            if persona["dni"] == dni:
                padron.remove(persona)
                print("Datos eliminados correctamente.")
                print("Registro borrado:", persona)
                return

        print("No se encontró un Alumno con ese DNI.")
    else:
        print("El borrado de los datos del Alumno ha sido cancelado.")
    print("Aguarde....")
    time.sleep(2)
###########################FIN OPCION 2: BAJAS
#
######################################################
# OPCION 3: MODIFICACION DE PERSONAS Y SUS MATERIAS
######################################################
def mostrar_persona_a_modificar(padron, dni):
    # Buscar la persona en el padrón
    global encontrado
    global persona
    global persona_encontrada
    
    persona_encontrada = None

    # Buscar la persona en el padrón
    encontrado = False
    for persona in padron:
        if persona["dni"] == dni:
            encontrado = True
            persona_encontrada = persona
            break

    return persona_encontrada

 
#-----FUNCION ESPECIFICA PARA MODIFICAR DATOS
def modificar_persona(padron):
    global encontrado
    encontrado = False
    dni = int(input("Ingrese el DNI del Alumno cuyos datos desea modificar: "))
    global persona
    persona = mostrar_persona_a_modificar(padron, dni)

    if persona is not None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print(f"Va a modificar los datos de " + persona["apellido"] + ", " + persona["nombres"])
        print("Aguarde....")
        time.sleep(2)
    else:
        print("No se encontró un Alumno con ese DNI.")
        print("Aguarde....")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return

# Opciones del menú
    materia1=persona['materia1']
    materia2=persona['materia2']
    opciones_modif = [
        f"[APE]. " + f"Modificar Apellido de {persona['apellido']}, {persona['nombres']}",
        f"[NOM]. " + f"Modificar Nombre {persona['apellido']}, {persona['nombres']}",
        f"[DOM]. " + f"Modificar Domicilio {persona['apellido']}, {persona['nombres']}",
        f"[MA1]. " + f"Modificar el Nombre de la Materia 1: {materia1}",
        f"[N11]. " + f"Modificar la Primera Nota de {materia1}",
        f"[N21]. " + f"Modificar la Segunda Nota de {materia1}",
        f"[MA2]. " + f"Modificar el Nombre de la Materia 2: {materia2}",
        f"[N12]. " + f"Modificar la Primera Nota de {materia2}",
        f"[N22]. " + f"Modificar la Segunda Nota de {materia2}",
        f"[ V ]. " + f"Volver al Menú Principal ",
        f" " 
    ]

    # Calcular la longitud máxima de las opciones en cada columna
    max_length = max(len(option) for option in opciones_modif)
    half_length = max_length // 2  # Longitud deseada para cada columna

    # Dividir las opciones en dos columnas
    columnas = list(zip(opciones_modif[:len(opciones_modif)//2], opciones_modif[len(opciones_modif)//2:]))

    # Imprimir las opciones en dos columnas
    titulo = subrayar(f"Ingrese la operación que desea realizar:")
    print(titulo)

    for column in columnas:
        for option in column:
            print(option.ljust(max_length), end='   ')
        print()

    texto_estilizado=opciones_modif

    while True:
        try:
                # Solicitar la opción al usuario
                #opcion_str = input(texto_estilizado).upper()
                opcion_str = str(input("¿Su opción? ")).upper()
                opcion_str = re.sub(r"\x1b\[\d+(?:;\d+)*m", "", opcion_str)  # Eliminar caracteres de formato ANSI        
                if opcion_str == "":
                    opcion_str = -1
                else:
                    opcion = (opcion_str)
        
################ MODIFICACIONES DATOS ALUMNOS
                if opcion_str == 'APE':
                    persona["apellido"] = input("Ingrese el nuevo apellido: ").upper()

                elif opcion_str == 'NOM':
                    persona["nombres"] = input("Ingrese nombres: ").upper()

                elif opcion_str == 'DOM':
                    persona["domicilio"] = str(input("Ingrese el nuevo domicilio: "))

                
                elif opcion_str == 'DNI':
                    
                        if persona_encontrada is not None:
                            nuevo_dni = input("Ingrese el nuevo DNI: ")
                            persona_encontrada["dni"] = int(nuevo_dni)
                            print("DNI modificado correctamente.")
                            print("Aguarde....")
                            time.sleep(4)
                        else:
                            print("No se encontró un Alumno con ese DNI.")
                            print("Aguarde....")
                            time.sleep(4)
                
################ MODIFICACIONES MATERIA 1
                elif opcion_str == 'MA1':
                    #print(f"Nombre actual de la materia :   {str(persona['materia1']).upper()}".ljust(10))
                    persona["materia1"] = input(f"Cambiar nombre de la materia {persona['materia1'].upper()}:   ".ljust(10)).capitalize()
        
                elif opcion_str == 'N11':
                    nota = float(input(f"Cambiar la primera nota de la materia {persona['materia1']}:   ".ljust(10)))
                    persona["materia1_nota1"] = format(nota,".2f")
                
                elif opcion_str == 'N21':
                    nota = float(input(f"Cambiar la segunda nota de la materia {persona['materia1']}:   ".ljust(10)))
                    persona["materia1_nota2"] = format(nota,".2f")
            
################ MODIFICACIONES MATERIA 2
                elif opcion_str == 'MA2':
                    persona["materia2"] = input("Ingrese el nombre de la materia 2: ").upper()
            
                elif opcion_str == 'N12':
                    nota = float(input(f"Cambiar la primera nota de la materia {persona['materia2']}:   ".ljust(10)))
                    persona["materia2_nota1"] = format(nota,".2f")
             
                elif opcion_str == 'N22':
                    nota = float(input(f"Cambiar la segunda nota de la materia {persona['materia2']}:   ".ljust(10)))
                    persona["materia2_nota2"] = format(nota,".2f")

                elif opcion_str == 'V':
                    print("Saliendo del Menú...")
                    mostrar_persona(padron, dni)
                    return
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
                    print("Aguarde....")
                    time.sleep(2)

        except ValueError:
            print("Opción inválida. Por favor, seleccione una opción válida.")

#################### FIN OPCION 3: MODIFICACION 
#
#################################################
#### OPCION 4: MOSTRAR DATOS DE UNA PERSONA (OK)
#################################################
def mostrar_persona(padron, dni):
    # Buscar la persona en el padrón

    for persona in padron:
        if persona["dni"] == dni:
            print(f"Datos del Alumno:")
            print("")
            #DATOS DEL ALUMNO
            print(f"Apellido: {persona['apellido']}".ljust(39),
                f"Nombres: {persona['nombres']}".ljust(35),
                f"D.N.I.: {persona['dni']}".ljust(40),
                f"Domicilio: {persona['domicilio']}".ljust(30)
                )
            print("")
            #TITULOS SUBRAYADOS
            print(subrayar(
                f"MATERIA".ljust(39),
                f"PRIMERA NOTA".ljust(20),
                f"SEGUNDA NOTA".ljust(20),
                f"PROMEDIO".ljust(10),
                f"SITUACION".ljust(10)
                ))
            

            #INICIO LISTADO DE MATERIAS/NOTAS/PROMEDIO/SITUACION. MATERIA 1 (OK)
            persona['materia1_promedio'] = f"{((float(persona['materia1_nota1']) + float(persona['materia1_nota2'])) / 2):.2f}"
            persona['materia1_situacion'] = "Regularizada" if float(persona['materia1_promedio']) >= 6.00 else "No Regularizada"
            print(f"{persona['materia1']}".ljust(39), f"{persona['materia1_nota1']}".ljust(22),
                  f"{persona['materia1_nota2']}".ljust(22), 
                  f"{persona['materia1_promedio']}".ljust(6),
                  f"{persona['materia1_situacion']}".ljust(12)
                  )

            #INICIO LISTADO DE MATERIAS/NOTAS/PROMEDIO/SITUACION. MATERIA 2 (OK)
            persona['materia2_promedio'] = f"{((float(persona['materia2_nota1']) + float(persona['materia2_nota2'])) / 2):.2f}"
            persona['materia2_situacion'] = "Regularizada" if float(persona['materia2_promedio']) >= 6.00 else "No Regularizada"
            print(f"{persona['materia2']}".ljust(39),
                  f"{persona['materia2_nota1']}".ljust(22),
                  f"{persona['materia2_nota2']}".ljust(22),
                  f"{persona['materia2_promedio']}".ljust(6),
                  f"{persona['materia2_situacion']}".ljust(12)
                  )
            print("Operacion a Confirmar en el paso que sigue, dos segundos por favor....")
            print("Aguarde....")
            time.sleep(2)
            return
    ###OK###
    #hasta aqui todo ok
    # Si no se encuentra la persona
    print(f"No se encontró un Alumno con ese DNI.")
######### FIN OPCION 4
#
############################################################
# OPCION 5: CARGAR AL PADRON DESDE UN ARCHIVO (padron.csv)
############################################################
def archivo_carga_personas(padron, nombre_archivo):
    global archivo
    archivo=None
    os.system('cls' if os.name == 'nt' else 'clear')
    archivo = input("Ingrese SOLO EL NOMBRE del archivo CSV: " + ".csv" + " (solo 'ENTER' carga el archivo 'padron'). ")
    
    try:
        if archivo == "":
            archivo = nombre_archivo + ".csv"
            print("ingresa y carga el nombre completo" + archivo)
            print("Aguarde....")
            time.sleep(2)
            agregar_al_padron = False
        else:
            archivo = archivo + ".csv"
            agregar_al_padron = True
 

        with open(archivo, newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')

            if not agregar_al_padron:
                # Si no se desea agregar al padrón existente, se limpia el padrón
                padron.clear()

            for row in reader:
                # Crear un diccionario para cada persona y agregarlo al padrón
                persona = {
                    "apellido": row["apellido"],
                    "nombres": row["nombres"],
                    "dni": int(row["dni"]),
                    "domicilio": str(row["domicilio"]),
                    "materia1": str(row["materia1"]),
                    "materia1_nota1": (row["materia1_nota1"]),
                    "materia1_nota2": (row["materia1_nota2"]),
                    "materia1_promedio": (row["materia1_promedio"]),
                    "materia1_situacion": str(row["materia1_situacion"]),
                    "materia2": str(row["materia2"]),
                    "materia2_nota1": (row["materia2_nota1"]),
                    "materia2_nota2": (row["materia2_nota2"]),
                    "materia2_promedio": (row["materia2_promedio"]),
                    "materia2_situacion": str(row["materia2_situacion"]),

                }

                padron.append(persona)

        if agregar_al_padron:
            print("Se han agregado los Alumnos del archivo CSV en el sistema correctamente.")
            archivo="padron.csv"
            print("Aguarde....")
            time.sleep(2)
            guardar_padron_en_archivo(padron)
        else:
            print("Se han cargado los Alumnos del archivo CSV correctamente.")
            print("Aguarde....")
            time.sleep(2)
            #guardar_padron_en_archivo(padron)

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    except Exception as e:
        print("Ocurrió un error al cargar los Alumnos del archivo CSV:", str(e))
################# FIN OPCION 5
#
##########################################################
### OPCION 6: MUESTRA EL CONTENIDO COMPLETO DEL PADRON
##########################################################
def mostrar_padron(padron):
    #print("\033[5m")  # Código para fuente de tamaño menor
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Lista completa de Alumnos:")
    for i, persona in enumerate(padron, start=1):
        print(f"Registro {i}: ", end="")
        for campo, valor in persona.items():
            #valor = "M" if campo == "materia1" and valor else valor
            print(f"{campo.upper()}: {valor} | ", end="")
        print("\n------------------------------")

    print("\033[0m")  # Código para restaurar el tamaño de fuente
######## FIN OPCION 6
#
#########################################################################
# GUARDA EL RESULTADO DE LA OPERACION RECIENTE (ALTA, BAJA, MODIFICACION)
# EN EL ARCHIVO GENERAL
#########################################################################
def guardar_padron_en_archivo(padron):
    global archivo
    os.system('cls' if os.name == 'nt' else 'clear')    
    while True:
        confirmacion = input("¿Desea guardar los cambios en el archivo " + archivo + "? (S/N): ")
        if confirmacion.lower() == "s":
            try:
                print("Archivo: "+ archivo)
                #input()
                with open(archivo, "w", newline='') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=padron[0].keys(), delimiter=';')
                    writer.writeheader()
                    #print(writer)
                    #input()
                    for persona in padron:
                        #print(persona)
                        #persona["materia1"] = persona["materia1"]
                        writer.writerow(persona)
            
                print("Se han guardado los cambios en el archivo CSV correctamente.")
                return
                        
            except Exception as e:
                print("Ocurrió un error al guardar los cambios en el archivo CSV:", str(e))
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

#INVOCA A LA FUNCION DE CARGA INICIAL QUE SE ENCUENTRA DEFINIDA AL PRINCIPIO DE ESTE PROGRAMA.
#le pasa como parametro la lista padron vacia
#
archivo_carga_inicial_personas(padron)

##############################
############ Menú de opciones
##############################

# ------------------Definir las opciones del menú con diferentes estilos
titulo = subrayar(f"Ingrese la operación que desea realizar:")

opcion1 = f"1. " + f"Dar de Alta a una Alumno"
opcion2 = f"2. " + f"Modificar datos de un Alumno"
opcion3 = f"3. " + f"Eliminar datos de un Alumno"
opcion4 = f"4. " + f"Mostrar datos de un Alumno"
opcion5 = f"5. " + f"Recargar/Importar listado de Alumnos desde un archivo CSV"
opcion6 = f"6. " + f"Visualizar listado completo de Alumnos"
opcion7 = f"0. " + f"Salir del Menú "
opcion8 = f"¿Su opción? " + f"-->>> "

# -------------------Concatenar las líneas del menú
texto_estilizado_0 = f"{titulo}\n{opcion1}\n{opcion2}\n{opcion3}\n{opcion4}\n{opcion5}\n{opcion6}\n{opcion7}\n{opcion8}"

#-------------------- Solicitar la opción al usuario
while True:
    try:

            os.system('cls' if os.name == 'nt' else 'clear') #Para limpiar la pantalla
            opcion = input(texto_estilizado_0)
            #
            #### ALTAS
            #
            if opcion == "1": 
                cargar_persona(padron)
                guardar_padron_en_archivo(padron)  # Guardar los cambios al agregar una persona
                input("Presione ENTER para volver al Menú...")
            #---------
            #
            #### MODIFICACION
            #
            elif opcion == "2":
                modificar_persona(padron)
                guardar_padron_en_archivo(padron)  # Guardar los cambios al modificar una persona
                input("Presione ENTER para volver al Menú...") 
            #-----------------
            ##### BAJA
            #
            elif opcion == "3":
                borrar_persona(padron)
                guardar_padron_en_archivo(padron)  # Guardar los cambios al eliminar los datos de una persona
                input("Presione ENTER para volver al Menú...")
            #------------------

            elif opcion == "4":
                dni = int(input("Ingrese el DNI de la persona a mostrar: "))
                mostrar_persona(padron, dni)
                input("Presione ENTER para volver al Menú...")
            elif opcion == "5":
                archivo_carga_personas(padron, nombre_archivo)
                input("Presione ENTER para volver al Menú...")
            elif opcion == "6":
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

    #Para limpiar la pantalla
os.system('cls' if os.name == 'nt' else 'clear')

#FIN DE PROGRAMA

