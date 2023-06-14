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
padron = []
import csv
import os
import time
import colorama
from colorama import Fore, Back, Style
from colorama import init

archivo=""
nombre_archivo="padron"
init(autoreset=True)  # Inicializar colorama para que se reinicie automáticamente después de cada impresión

#(f"{VARIABLE:.2f}") => FORMATEA LA VARIABLE NUMÉRICA A DECIMAL DE DOS DIGITOS DECIMALES.
#FUNCION CARGA INICIAL DEL PADRON DE PERSONAS DESDE EL ARCHIVO padron.csv
def archivo_carga_inicial_personas(padron):
    global archivo
    archivo = "padron.csv"

    try:
        with open(archivo, 'r', encoding='utf-8', newline='') as csv_file:
            print("Cargando archivo: " + archivo)
            time.sleep(2)
            reader = csv.DictReader(csv_file, delimiter=';')

            for row in reader:
                # Crear un diccionario para cada persona y agregarlo al padrón
                persona = {
                    "apellido": row["apellido"],
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
                    "materia3": row["materia3"],
                    "materia3_nota1": (row["materia3_nota1"]),
                    "materia3_nota2": (row["materia3_nota2"]),
                    "materia3_promedio": (row["materia3_promedio"]),
                    "materia3_situacion": row["materia3_situacion"],
                    "materia4": row["materia4"],
                    "materia4_nota1": (row["materia4_nota1"]),
                    "materia4_nota2": (row["materia4_nota2"]),
                    "materia4_promedio": (row["materia4_promedio"]),
                    "materia4_situacion": row["materia4_situacion"]
                }

                padron.append(persona)

        print("Se ha cargado el archivo CSV en el sistema correctamente.")

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    except UnicodeDecodeError:
        print("Ocurrió un error al cargar las personas del archivo CSV: Error de decodificación de caracteres.")
    except Exception as e:
        print("Ocurrió un error al cargar las personas del archivo CSV:", str(e))


# Función para cargar una persona
def cargar_persona(padron):
    persona = {}
    os.system('cls' if os.name == 'nt' else 'clear')
    init()  # Inicializar colorama

    apellido = input(f"{Back.BLACK}{Fore.WHITE}Ingrese el apellido: ")
    persona["apellido"] = apellido.capitalize()

    nombres = input(f"{Back.BLACK}{Fore.WHITE}Ingrese los nombres: ")
    persona["nombres"] = nombres.capitalize()

    dni = int(input(f"{Back.BLACK}{Fore.WHITE}Ingrese el DNI: "))
    persona["dni"] = dni

    domicilio = input(f"{Back.BLACK}{Fore.WHITE}Ingrese el domicilio: ")
    persona["domicilio"] = domicilio.capitalize()

    campos = [
        ("materia1", "Ingrese el nombre de la materia 1"),
        ("materia2", "Ingrese el nombre de la materia 2"),
        ("materia3", "Ingrese el nombre de la materia 3"),
        ("materia4", "Ingrese el nombre de la materia 4"),
    ]

    for campo, mensaje in campos:
        valor = input(f"{Back.BLACK}{Fore.GREEN}{mensaje}: ")
        persona[campo] = valor.capitalize()


        # Solicitar notas y situación de la materia
        nota1_mensaje = f"Ingrese la primera nota de {valor.upper()}: "
        nota2_mensaje = f"Ingrese la segunda nota de {valor.upper()}: "
        situacion_mensaje = f"Ingrese la Situación de {valor}: "
        
        while True:
            try:
                nota1 = float(input(f"{Back.BLACK}{Fore.CYAN}{nota1_mensaje}: "))
                if nota1 < 0 or nota1 > 10:
                    raise ValueError("La nota debe estar entre 0 y 10")
                break
            except ValueError as e:
                print(f"{Fore.RED}Error: {str(e)}")

        while True:
            try:
                nota2 = float(input(f"{Back.BLACK}{Fore.BLUE}{nota2_mensaje}: "))
                if nota2 < 0 or nota2 > 10:
                    raise ValueError("La nota debe estar entre 0 y 10")
                break
            except ValueError as e:
                print(f"{Fore.RED}Error: {str(e)}")

        promedio = (nota1 + nota2) / 2
        situacion = "Aprobado" if promedio >= 6.00 else "Desaprobado"
        persona[f"{campo}_nota1"] = format(nota1, ".2f")
        persona[f"{campo}_nota2"] = format(nota2, ".2f")
        persona[f"{campo}_promedio"] = format(promedio, ".2f")
        persona[f"{campo}_situacion"] = situacion
    if not persona:
        print("No se ha ingresado ningún dato.")
        return None

    for i in range(1, 5):
        materia = persona.get(f"materia{i}", "")
        nota1 = float(persona.get(f"materia{i}_nota1", 0))
        nota2 = float(persona.get(f"materia{i}_nota2", 0))
        nota1 = format(nota1, ".2f")  # Formateo de nota1
        nota2 = format(nota2, ".2f")  # Formateo de nota2
        promedio = float(f"{((float(nota1) + float(nota2)) / 2):.2f}")
        situacion = "Aprobado" if promedio >= 6.00 else "Desaprobado"
        print(f"{Fore.GREEN}Materia {i}: {materia} Nota 1: {nota1} Nota 2: {nota2} Promedio: {format(promedio, '.2f')} Situación: {situacion}")

    return persona




def guardar_padron_en_archivo(padron):
    global archivo
    os.system('cls' if os.name == 'nt' else 'clear')    
    while True:
        confirmacion = input("¿Desea guardar los cambios en el archivo " + archivo + "? (S/N): ")
        if confirmacion.lower() == "s":
            try:
                print("Archivo: "+ archivo)
                input()
                with open(archivo, "w", newline='') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=padron[0].keys(), delimiter=';')
                    writer.writeheader()
                    print(writer)
                    input()
                    for persona in padron:
                        print(persona)
                        #persona["materia1"] = persona["materia1"]
                        writer.writerow(persona)
            
                print("Se han guardado los cambios en el archivo CSV correctamente.")
                return
                #break  # Salir del bucle cuando se haya guardado correctamente
        
            except Exception as e:
                print("Ocurrió un error al guardar los cambios en el archivo CSV:", str(e))
                break  # Salir del bucle en caso de error

        elif confirmacion.lower() == "n":
            print("Los cambios no han sido guardados.")
            return
            #break  # Salir del bucle cuando no se deseen guardar los cambios
        
        else:
            print("Opción inválida. Por favor, seleccione 'S' o 'N'.")

    #FUNCION BLINKING PARA RESALTAR ADEVERTENCIAS
    def blink(text):
        return "\033[5m" + text + "\033[0m"

    titulo = blink("ATENCIÓN")

    while True:
        print(titulo)
        time.sleep(1)
        print("\033[0m")  # Restaurar el formato original después de imprimir el título
        time.sleep(1)
   




# Función para modificar una persona
def modificar_persona(padron):
    print("Función modificar_persona()")
    dni = int(input("Ingrese el DNI de la persona a modificar: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    encontrado = False
    #materia1_nota1 = None
    #materia1_nota2 = None


    for persona in padron:
        if persona["dni"] == dni:
            # Modificar los datos de la persona
            opciones = """Ingrese la opción del dato que desea modificar:
            A. Apellido
            N. Nombres
            M1. materia_1
            N11. Primera Nota de la materia 1
            N12. Segunda Nota de la materia 1
#Promedio
            S1. Indique Situación Materia 1
            D. Domicilio, Número, Piso, Departamento, materia2_promedio, Provincia, Código Postal o Año de ingreso
            M. materia3
            V. Volver al menú
            """
            opcion = input(opciones).upper()

            if opcion == 'A':
                persona["apellido"] = input("Ingrese el nuevo apellido: ").upper()

            elif opcion == 'N':
                persona["nombres"] = input("Ingrese los nuevos nombres: ").upper()

            elif opcion == 'M1':
                persona["materia1"] = input("Ingrese el nombre de la materia 1: ").upper()
            
            elif opcion == 'N11':
                persona["materia1_nota1"] = float(input("Ingrese la primera nota de la materia 1: "))
             
            elif opcion == 'N12':
                persona["materia1_nota2"] = float(input("Ingrese la segunda nota de la materia 1: "))
            
            elif opcion == 'S1':
                persona["materia1_situacion"] = str(input("Ingrese Situación materia 1: "))

            elif opcion == 'D':
                persona["domicilio"] = str(input("Ingrese la nueva domicilio: "))
                
                #USAR ESTAS INSTRUCCIONES PARA CARGAR EL RESTO DE LAS MATERIAS####
                
                #persona["materia1_situacion"] = str(input("Ingrese el nuevo número: "))
                #persona["materia2"] = int(input("Ingrese el nuevo materia2: "))
                #persona["materia2_nota1"] = input("Ingrese el nuevo departamento: ")
                #persona["materia2_nota2"] = input("Ingrese Provincia: ")
                #persona["materia2_promedio"] = input("Ingrese la materia2_promedio: ")
                #persona["materia2_situacion"] = input("Ingrese el código postal: ")
                #persona["materia3_nota1"] = int(input("Ingrese el año de ingreso: "))
                

            elif opcion == 'M':
                persona["materia3"] = input("Ingrese la materia 3: ")

            elif opcion == 'V':
                print("Saliendo del Menú...")
                break

            print("Datos modificados correctamente.")

            print("Datos de la persona:")
            print("Apellido:", persona["apellido"])
            print("Nombres:", persona["nombres"])
            print("DNI:", persona["dni"])
            print("Domicilio:", persona["domicilio"])
            print("Materia 1:", persona["materia1"])
            print("Materia 1_Nota 1:", persona["materia1_nota1"])
            print("Materia 1_Nota 2:", persona["materia1_nota2"])
            print("Materia 1_Promedio:", persona["materia1_promedio"])
            print("Materia 1_Situacion:", persona["materia1_situacion"])
            print("Materia 2:", persona["materia2"])
            print("Materia 2_Nota 1:", persona["materia2_nota1"])
            print("Materia 2_Nota 2:", persona["materia2_nota2"])
            print("Materia 2_Promedio:", persona["materia2_promedio"])
            print("Materia 2_Situacion:", persona["materia2_situacion"])
            print("Materia 3:", persona["materia3"])
            print("Materia 3_nota 1:", persona["materia3_nota1"])
            print("Materia 3_Nota 2:", persona["materia3_nota2"])
            print("Materia 3_Promedio:", persona["materia3_promedio"])
            print("Materia 3_Situacion:", persona["materia3_situacion"])
            print("Materia 4:", persona["materia4"])
            print("Materia 4_nota 1:", persona["materia4_nota1"])
            print("Materia 4_Nota 2:", persona["materia4_nota2"])
            print("Materia 4_Promedio:", persona["materia4_promedio"])
            print("Materia 4_Situacion:", persona["materia4_situacion"])


            encontrado = True
            break
    
    if encontrado==True:
        guardar_padron_en_archivo(padron)
       
    else:
        print("No se encontró una persona con ese DNI.")


#FUNCION PARA BORRAR UNA PERSONA (OK)
import os

def borrar_persona(padron):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Función borrar_persona()")
    dni = int(input("Ingrese el DNI de la persona a borrar: "))
    mostrar_persona(padron, dni)

    # Agregar confirmación de borrado
    confirmacion = input("¿Confirma que desea borrar a esta persona? (S/N): ")

    if confirmacion.lower() == "s":
        for persona in padron:
            if persona["dni"] == dni:
                padron.remove(persona)
                print("Persona eliminada correctamente.")
                print("Registro borrado:", persona)
                return

        print("No se encontró una persona con ese DNI.")
    else:
        print("El borrado de la persona ha sido cancelado.")

    input()



#FUNCION MOSTRAR DATOS DE UNA PERSONA (OK)
def mostrar_persona(padron, dni):
    # Buscar la persona en el padrón
    colorama.init(autoreset=True)    
    for persona in padron:
        if persona["dni"] == dni:
            print(f"{Fore.LIGHTGREEN_EX}Datos del Alumno:")
            print("")
            #DATOS DEL ALUMNO
            print(f"{Back.BLACK}{Fore.WHITE}Apellido: {persona['apellido']}".ljust(39),
                f"{Back.BLACK}{Fore.WHITE}Nombres: {persona['nombres']}".ljust(35),
                f"{Back.BLACK}{Fore.WHITE}D.N.I.: {persona['dni']}".ljust(40)
                )
            print("")
            #TITULOS SUBRAYADOS
            print(subrayar(
                f"{Back.BLACK}{Fore.BLUE}MATERIA".ljust(39),
                f"{Back.BLACK}{Fore.LIGHTBLUE_EX}PRIMERA NOTA".ljust(20),
                f"{Back.BLACK}{Fore.LIGHTBLUE_EX}SEGUNDA NOTA".ljust(20),
                f"{Back.BLACK}{Fore.LIGHTBLUE_EX}PROMEDIO".ljust(10),
                f"{Back.BLACK}{Fore.LIGHTBLUE_EX}SITUACION".ljust(10)
                ))
            

            #INICIO LISTADO DE MATERIAS/NOTAS/PROMEDIO/SITUACION. MATERIA 1 (OK)
            persona['materia1_promedio'] = f"{((float(persona['materia1_nota1']) + float(persona['materia1_nota2'])) / 2):.2f}"
            print(f"{Back.BLACK}{Fore.GREEN}{persona['materia1']}".ljust(39), f"{Back.BLACK}{Fore.GREEN}{persona['materia1_nota1']}".ljust(22),
                  f"{Back.BLACK}{Fore.GREEN}{persona['materia1_nota2']}".ljust(22), 
                  f"{Back.BLACK}{Fore.GREEN}{persona['materia1_promedio']}".ljust(18),
                  f"{Back.BLACK}{Fore.GREEN}{persona['materia1_situacion']}".ljust(12)
                  )
            # Materia 1: Guardar el promedio en el archivo padron.csv
            with open('padron.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=padron[0].keys(), delimiter=';')
                writer.writeheader()
                writer.writerows(padron)
            csvfile.close()  # Cerrar el archivo

            #INICIO LISTADO DE MATERIAS/NOTAS/PROMEDIO/SITUACION. MATERIA 2 (OK)
            persona['materia2_promedio'] = f"{((float(persona['materia2_nota1']) + float(persona['materia2_nota2'])) / 2):.2f}"
            print(f"{Back.BLACK}{Fore.YELLOW}{persona['materia2']}".ljust(39),
                  f"{Back.BLACK}{Fore.YELLOW}{persona['materia2_nota1']}".ljust(22),
                  f"{Back.BLACK}{Fore.YELLOW}{persona['materia2_nota2']}".ljust(22),
                  f"{Back.BLACK}{Fore.YELLOW}{persona['materia2_promedio']}".ljust(18),
                  f"{Back.BLACK}{Fore.YELLOW}{persona['materia2_situacion']}".ljust(12)
                  )
            # Materia 2: Guardar el promedio en el archivo padron.csv
            with open('padron.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=padron[0].keys(), delimiter=';')
                writer.writeheader()
                writer.writerows(padron)
            csvfile.close()  # Cerrar el archivo

            #INICIO LISTADO DE MATERIAS/NOTAS/PROMEDIO/SITUACION. MATERIA 3 (OK)
            persona['materia3_promedio'] = f"{((float(persona['materia3_nota1']) + float(persona['materia3_nota2'])) / 2):.2f}"
            print(f"{Back.BLACK}{Fore.CYAN}{persona['materia3']}".ljust(39),
                  f"{Back.BLACK}{Fore.CYAN}{persona['materia3_nota1']}".ljust(22),
                  f"{Back.BLACK}{Fore.CYAN}{persona['materia3_nota2']}".ljust(22),
                  f"{Back.BLACK}{Fore.CYAN}{persona['materia3_promedio']}".ljust(18),
                  f"{Back.BLACK}{Fore.CYAN}{persona['materia3_situacion']}".ljust(12)
                  )
            # Materia 3: Guardar el promedio en el archivo padron.csv
            with open('padron.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=padron[0].keys(), delimiter=';')
                writer.writeheader()
                writer.writerows(padron)
            csvfile.close()  # Cerrar el archivo

            #INICIO LISTADO DE MATERIAS/NOTAS/PROMEDIO/SITUACION. MATERIA 4 (OK)
            persona['materia4_promedio'] = f"{((float(persona['materia4_nota1']) + float(persona['materia4_nota2'])) / 2):.2f}"
            print(f"{Back.BLACK}{Fore.MAGENTA}{persona['materia4']}".ljust(39),
                  f"{Back.BLACK}{Fore.MAGENTA}{persona['materia4_nota1']}".ljust(22),
                  f"{Back.BLACK}{Fore.MAGENTA}{persona['materia4_nota2']}".ljust(22),
                  f"{Back.BLACK}{Fore.MAGENTA}{persona['materia4_promedio']}".ljust(18),
                  f"{Back.BLACK}{Fore.MAGENTA}{persona['materia4_situacion']}".ljust(12)
                  )
            # Materia 4: Guardar el promedio en el archivo padron.csv
            with open('padron.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=padron[0].keys(), delimiter=';')
                writer.writeheader()
                writer.writerows(padron)
            csvfile.close()  # Cerrar el archivo
            print("TODO OK EN ESTA OPCION")
            time.sleep(2)
            return
    ###OK###
    #hasta aqui todo ok
    # Si no se encuentra la persona
    print(f"{Back.WHITE}{Fore.RED}No se encontró una persona con ese DNI.")
    print(Style.RESET_ALL)  # Resetear los estilos después de imprimir


# CARGAR AL PADRON DESDE UN ARCHIVO (padron.csv)
def archivo_carga_personas(padron, nombre_archivo):
    global archivo
    archivo=None
    os.system('cls' if os.name == 'nt' else 'clear')
    archivo = input("Ingrese SOLO EL NOMBRE del archivo CSV: " + ".csv" + " (solo 'ENTER' carga el archivo 'padron'). ")
    
    try:
        if archivo == "":
            archivo = nombre_archivo + ".csv"
            print("ingresa y carga el nombre completo" + archivo)
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
                    "materia3": str(row["materia3"]),
                    "materia3_nota1": (row["materia3_nota1"]),
                    "materia3_nota2": (row["materia3_nota2"]),
                    "materia3_promedio": (row["materia3_promedio"]),
                    "materia3_situacion": str(row["materia3_situacion"]),
                    "materia4": str(row["materia4"]),
                    "materia4_nota1": (row["materia4_nota1"]),
                    "materia4_nota2": (row["materia4_nota2"]),
                    "materia4_promedio": (row["materia4_promedio"]),
                    "materia4_situacion": str(row["materia4_situacion"])

                }

                padron.append(persona)

        if agregar_al_padron:
            print("Se han agregado las personas del archivo CSV en el sistema correctamente.")
            archivo="padron.csv"
            time.sleep(2)
            guardar_padron_en_archivo(padron)
        else:
            print("Se han cargado las personas del archivo CSV correctamente.")
            time.sleep(2)
            #guardar_padron_en_archivo(padron)

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    except Exception as e:
        print("Ocurrió un error al cargar las personas del archivo CSV:", str(e))



#MUESTRA EL CONTENIDO COMPLETO DEL PADRON

def mostrar_padron(padron):
    #print("\033[5m")  # Código para fuente de tamaño menor
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Lista completa de personas:")
    for i, persona in enumerate(padron, start=1):
        print(f"Registro {i}: ", end="")
        for campo, valor in persona.items():
            #valor = "M" if campo == "materia1" and valor else valor
            print(f"{campo.upper()}: {valor} | ", end="")
        print("\n------------------------------")

    print("\033[0m")  # Código para restaurar el tamaño de fuente

# mostrar_padron(padron, int(dni))
import csv



#INVOCA A LA FUNCION DE CARGA INICIAL QUE SE ENCUENTRA DEFINIDA AL PRINCIPIO DE ESTE PROGRAMA.
archivo_carga_inicial_personas(padron)

# Menú de opciones

import os
os.system('cls' if os.name == 'nt' else 'clear') #Para limpiar la pantalla
      
   
    # Función para subrayar el texto
#def subrayar(texto):
#    return "\033[4m" + texto + "\033[0m"

def subrayar(*textos):
    return " ".join("\033[4m" + texto + "\033[0m" for texto in textos)



# Definir las opciones del menú con diferentes estilos
titulo = subrayar(f"{Fore.GREEN}{Style.BRIGHT}Ingrese la operación que desea realizar:")

opcion1 = "1. " + f"{Fore.WHITE}{Style.BRIGHT}Dar de Alta a una persona"
opcion2 = f"{Fore.RESET}{Style.RESET_ALL}2. " + f"{Fore.WHITE}{Style.BRIGHT}Modificar datos de la persona"
opcion3 = f"{Fore.RESET}{Style.RESET_ALL}3. " + f"{Fore.WHITE}{Style.BRIGHT}Eliminar a una persona"
opcion4 = f"{Fore.RESET}{Style.RESET_ALL}4. " + f"{Fore.WHITE}{Style.BRIGHT}Mostrar datos de una persona"
opcion5 = f"{Fore.RESET}{Style.RESET_ALL}5. " + f"{Fore.CYAN}Recargar/Importar listado de personas desde un archivo CSV"
opcion6 = f"{Fore.RESET}{Style.RESET_ALL}6. " + f"{Fore.WHITE}{Style.BRIGHT}Visualizar listado completo"
opcion7 = f"{Fore.RED}{Style.BRIGHT}0. " + f"{Fore.WHITE}{Style.BRIGHT}Salir del Menú "
opcion8 = f"¿Su opción? " + f"{Fore.RESET}{Style.RESET_ALL}-->>> "

# Concatenar las líneas del menú
texto_estilizado = f"{titulo}\n\n{opcion1}\n{opcion2}\n{opcion3}\n{opcion4}\n{opcion5}\n{opcion6}\n{opcion7}\n{opcion8}"

# Solicitar la opción al usuario
opcion_str = input(texto_estilizado)

while True:
    try:
            # Solicitar la opción al usuario
            opcion_str = input(texto_estilizado)
        
            if opcion_str == "":
                opcion = -1
            else:
                opcion = int(opcion_str)
        
            if opcion == 1:
                persona = cargar_persona(padron)
                padron.append(persona)
                
                guardar_padron_en_archivo(padron)  # Guardar los cambios al agregar una persona
                input("Presione ENTER para volver al Menú...")
            elif opcion == 2:
                modificar_persona(padron)
                input("Presione ENTER para volver al Menú...") # guardar_padron_en_archivo(padron)  # Guardar los cambios al modificar los datos de una persona
            elif opcion == 3:
                borrar_persona(padron)
                guardar_padron_en_archivo(padron)  # Guardar los cambios al eliminar los datos de una persona
                input("Presione ENTER para volver al Menú...")
            elif opcion == 4:
                dni = int(input("Ingrese el DNI de la persona a mostrar: "))
                mostrar_persona(padron, dni)
                input("Presione ENTER para volver al Menú...")
            elif opcion == 5:
######OK
                archivo_carga_personas(padron, nombre_archivo)
                input("Presione ENTER para volver al Menú...")
            elif opcion == 6:
                mostrar_padron(padron)
                input("Presione ENTER para volver al Menú...")
            elif opcion == 0:
                print("Saliendo del Menú...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    except ValueError:
        print("Opción inválida. Por favor, seleccione una opción válida.")
  

input("Presione ENTER para continuar...")
print()  # Salto de línea para separar el menú de la próxima operación
print("Fin del programa")
archivo="padron.csv"
guardar_padron_en_archivo(padron)
#break

    #Para limpiar la pantalla
import os
os.system('cls' if os.name == 'nt' else 'clear')

#FIN DE PROGRAMA

