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
from cgi import print_form
import csv
import os
import time
import colorama
from colorama import Fore, Back, Style
from colorama import init
from sty import fg, bg, ef, rs
import textwrap
import pprint
import re
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
        situacion = "Regularizada" if promedio >= 6.00 else "No Regularizada"
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
        situacion = "Regularizada" if promedio >= 6.00 else "No Regularizada"
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
    #print("Función modificar_persona()")
    #os.system('cls' if os.name == 'nt' else 'clear')
    global encontrado
    encontrado = False
    dni = int(input("Ingrese el DNI de la persona cuyos datos desea modificar: "))
    global persona
    persona = mostrar_persona_a_modificar(padron, dni)

    if persona is not None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print(f"Va a modificar los datos de " + persona["apellido"] + ", " + persona["nombres"])
        mostrar_persona_a_modificar(padron, dni)
        time.sleep(4)

    else:
        print("No se encontró una persona con ese DNI.")
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        return


    # Definir las opciones del menú con diferentes estilos


#    opcion1 = f"{fg.da_blue}[APE]. " + f"{fg.li_blue}{ef.italic}Modificar Apellido"
#    opcion2 = f"{fg.da_blue}[NOM]. " + f"{fg.li_blue}{ef.italic}Modificar Nombre"
#    opcion3 = f"{fg.da_blue}[DOM]. " + f"{fg.li_blue}{ef.italic}Modificar Domicilio"
#    opcion4 = f"{fg.da_blue}[DNI]. " + f"{fg.li_blue}{ef.italic}Modificar DNI"

#    opcion5 = f"{fg.da_green}[MA1]. " + f"{fg.li_green}{ef.italic}Modificar Nombre Materia 1"
#    opcion6 = f"{fg.da_green}[N11]. " + f"{fg.li_green}{ef.italic}Modificar Primera Nota Materia 1"
#    opcion7 = f"{fg.da_green}[N21]. " + f"{fg.li_green}{ef.italic}Modificar Segunda Materia 2"
#
#    opcion8 = f"{fg.da_yellow}[MA2]. " + f"{fg.li_yellow}{ef.italic}Modificar Nombre Materia 2"
#    opcion9 = f"{fg.da_yellow}[N12]. " + f"{fg.li_yellow}{ef.italic}Modificar Primera Nota Materia 2"
#    opcion10 = f"{fg.da_yellow}[N22]. " + f"{fg.li_yellow}{ef.italic}Modificar Segunda Materia 2"
#
#    opcion11 = f"{fg.da_cyan}[MA3]. " + f"{fg.li_cyan}{ef.italic}Modificar Nombre Materia 3"
#    opcion12 = f"{fg.da_cyan}[N13]. " + f"{fg.li_cyan}{ef.italic}Modificar Primera Nota Materia 3"
#    opcion13 = f"{fg.da_cyan}[N23]. " + f"{fg.li_cyan}{ef.italic}Modificar Segunda Materia 3"
#
#    opcion14 = f"{fg.da_magenta}[MA4]. " + f"{fg.li_magenta}{ef.italic}Modificar Nombre Materia 4"
#    opcion15 = f"{fg.da_magenta}[N14]. " + f"{fg.li_magenta}{ef.italic}Modificar Primera Nota Materia 4"
#    opcion16 = f"{fg.da_magenta}[N24]. " + f"{fg.li_magenta}{ef.italic}Modificar Segunda Materia 4"
# Opciones del menú 
# Opciones del menú
    materia1=persona['materia1']
    materia2=persona['materia2']
    materia3=persona['materia3']
    materia4=persona['materia4']
    opciones_modif = [
        f"{fg.da_blue}[APE]. " + f"{fg.li_blue}{ef.italic}Modificar Apellido de {persona['apellido']}, {persona['nombres']}",
        f"{fg.da_blue}[NOM]. " + f"{fg.li_blue}{ef.italic}Modificar Nombre {persona['apellido']}, {persona['nombres']}",
        f"{fg.da_green}[MA1]. " + f"{fg.li_green}{ef.italic}Modificar el Nombre de la Materia 1: {materia1}",
        f"{fg.da_green}[N11]. " + f"{fg.li_green}{ef.italic}Modificar la Primera Nota de {materia1}",
        f"{fg.da_green}[N21]. " + f"{fg.li_green}{ef.italic}Modificar la Segunda Nota de {materia1}",
        f"{fg.da_yellow}[MA2]. " + f"{fg.li_yellow}{ef.italic}Modificar el Nombre de la Materia 2: {materia2}",
        f"{fg.da_yellow}[N12]. " + f"{fg.li_yellow}{ef.italic}Modificar la Primera Nota de {materia2}",
        f"{fg.da_yellow}[N22]. " + f"{fg.li_yellow}{ef.italic}Modificar la Segunda Nota de {materia2}",
        f"{fg.li_red}[ V ]  . " + f"{bg.da_black}{fg.da_red}Volver al Menú Principal ",
        f"{fg.da_blue}[DOM]. " + f"{fg.li_blue}{ef.italic}Modificar Domicilio de {persona['apellido']}, {persona['nombres']}",
        f"{fg.da_blue}[DNI]. " + f"{fg.li_blue}{ef.italic}Modificar DNI de {persona['apellido']}, {persona['nombres']}",
        f"{fg.da_cyan}[MA3]. " + f"{fg.li_cyan}{ef.italic}Modificar el Nombre de la Materia 3:  {materia3}",
        f"{fg.da_cyan}[N13]. " + f"{fg.li_cyan}{ef.italic}Modificar la Primera Nota de {materia3}",
        f"{fg.da_cyan}[N23]. " + f"{fg.li_cyan}{ef.italic}Modificar la Segunda Nota de {materia3}",
        f"{fg.da_magenta}[MA4]. " + f"{fg.li_magenta}{ef.italic}Modificar el Nombre de la Materia 4: {materia4}",
        f"{fg.da_magenta}[N14]. " + f"{fg.li_magenta}{ef.italic}Modificar la Primera Nota de {materia4}",
        f"{fg.da_magenta}[N24]. " + f"{fg.li_magenta}{ef.italic}Modificar la Segunda Nota de {materia4}",
        f" " + f"{Fore.RESET}{Style.RESET_ALL}"
    ]

    # Calcular la longitud máxima de las opciones en cada columna
    max_length = max(len(option) for option in opciones_modif)
    half_length = max_length // 2  # Longitud deseada para cada columna

    # Dividir las opciones en dos columnas
    columnas = list(zip(opciones_modif[:len(opciones_modif)//2], opciones_modif[len(opciones_modif)//2:]))

    # Imprimir las opciones en dos columnas
        # Función para subrayar el texto
    def subrayar(*textos):
        return " ".join("\033[4m" + texto + "\033[0m" for texto in textos)
    
    titulo = subrayar(f"{Fore.GREEN}{Style.BRIGHT}Ingrese la operación que desea realizar:")
    print(titulo)
    print()

    for column in columnas:
        for option in column:
            print(option.ljust(max_length), end='   ')
        print()

    #texto_estilizado = opciones
    #print(texto_estilizado)


        #opcion17 = f"{fg.li_red}[V]  . " + f"{bg.da_black}{fg.da_red}Volver al Menú Principal "
        #opcion18 = f"¿Su opción? " + f"{Fore.RESET}{Style.RESET_ALL}-->>> "
    texto_estilizado=opciones_modif
# Concatenar las líneas del menú
    #texto_estilizado = f"{titulo}\n\n{opcion1}\n{opcion2}\n{opcion3}\n{opcion4}\n{opcion5}\n{opcion6}\n{opcion7}\n{opcion8}\n{opcion9}\n{opcion10}\n{opcion11}\n{opcion12}\n{opcion13}\n{opcion14}\n{opcion15}\n{opcion16}\n{opcion17}\n{opcion18}"
    #print(str(persona["materia1"]))

#    print(f"{Back.BLACK}{Fore.GREEN}Promedio de {persona['materia1']}: {float(persona['materia1_nota1']):.2f}".ljust(10))
#    print(f"{Back.BLACK}{Fore.GREEN}Promedio de {persona['materia1']}: {float(persona['materia1_nota2']):.2f}".ljust(10))
#    
#    print(f"{Back.BLACK}{Fore.YELLOW}Cambiar nombre de la materia {persona['materia2']}: {str(persona['materia2'])}".ljust(10))
#    print(f"{Back.BLACK}{Fore.YELLOW}Promedio de {persona['materia2']}: {float(persona['materia2_nota1']):.2f}".ljust(10))
#    print(f"{Back.BLACK}{Fore.YELLOW}Promedio de {persona['materia2']}: {float(persona['materia2_nota2']):.2f}".ljust(10))
#    
#    print(f"{Back.BLACK}{Fore.CYAN}Cambiar nombre de la materia {persona['materia3']}: {str(persona['materia3'])}".ljust(10))
#    print(f"{Back.BLACK}{Fore.CYAN}Promedio de {persona['materia3']}: {float(persona['materia3_nota1']):.2f}".ljust(10))
#    print(f"{Back.BLACK}{Fore.CYAN}Promedio de {persona['materia3']}: {float(persona['materia3_nota2']):.2f}".ljust(10))
#
#    print(f"{Back.BLACK}{Fore.MAGENTA}Cambiar nombre de la materia {persona['materia4']}: {str(persona['materia4'])}".ljust(10))
#    print(f"{Back.BLACK}{Fore.MAGENTA}Promedio de {persona['materia4']}: {float(persona['materia4_nota1']):.2f}".ljust(10))
#    print(f"{Back.BLACK}{Fore.MAGENTA}Promedio de {persona['materia4']}: {float(persona['materia4_nota2']):.2f}".ljust(10))    

#    print(texto_estilizado)


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
                            time.sleep(4)
                        else:
                            print("No se encontró una persona con ese DNI.")
                            time.sleep(4)
    
 ################ FIN DATOS ALUMNOS

################ MODIFICACIONES MATERIA 1
                elif opcion_str == 'MA1':
                    #print(f"{Back.BLACK}{Fore.GREEN}Nombre actual de la materia :   {str(persona['materia1']).upper()}".ljust(10))
                    persona["materia1"] = input(f"{Back.BLACK}{Fore.GREEN}Cambiar nombre de la materia {Back.BLACK}{Fore.GREEN}{persona['materia1'].upper()}:   ".ljust(10)).capitalize()
        
                elif opcion_str == 'N11':
                    nota = float(input(f"{Back.BLACK}{Fore.GREEN}Cambiar la primera nota de la materia {Back.BLACK}{Fore.GREEN}{persona['materia1']}:   ".ljust(10)))
                    persona["materia1_nota1"] = format(nota,".2f")
                
                elif opcion_str == 'N21':
                    nota = float(input(f"{Back.BLACK}{Fore.GREEN}Cambiar la segunda nota de la materia {Back.BLACK}{Fore.GREEN}{persona['materia1']}:   ".ljust(10)))
                    persona["materia1_nota2"] = format(nota,".2f")
            
################ MODIFICACIONES MATERIA 2
                elif opcion_str == 'MA2':
                    persona["materia2"] = input("Ingrese el nombre de la materia 2: ").upper()
            
                elif opcion_str == 'N12':
                    nota = float(input(f"{Back.BLACK}{Fore.GREEN}Cambiar la primera nota de la materia {Back.BLACK}{Fore.GREEN}{persona['materia2']}:   ".ljust(10)))
                    persona["materia2_nota1"] = format(nota,".2f")
             
                elif opcion_str == 'N22':
                    nota = float(input(f"{Back.BLACK}{Fore.GREEN}Cambiar la segunda nota de la materia {Back.BLACK}{Fore.GREEN}{persona['materia2']}:   ".ljust(10)))
                    persona["materia2_nota2"] = format(nota,".2f")

################ MODIFICACIONES MATERIA 3
                elif opcion_str == 'MA3':
                    persona["materia3"] = input("Ingrese el nombre de la materia 3: ").upper()
            
                elif opcion_str == 'N13':
                    nota = float(input(f"{Back.BLACK}{Fore.GREEN}Cambiar la primera nota de la materia {Back.BLACK}{Fore.GREEN}{persona['materia3']}:   ".ljust(10)))
                    persona["materia3_nota1"] = format(nota,".2f")
             
                elif opcion_str == 'N23':
                    nota = float(input(f"{Back.BLACK}{Fore.GREEN}Cambiar la primera nota de la materia {Back.BLACK}{Fore.GREEN}{persona['materia3']}:   ".ljust(10)))
                    persona["materia3_nota2"] = format(nota,".2f")

################ MODIFICACIONES MATERIA 4
                elif opcion_str == 'MA4':
                    persona["materia4"] = input("Ingrese el nombre de la materia 4: ").upper()
            
                elif opcion_str == 'N14':
                    nota = float(input(f"{Back.BLACK}{Fore.GREEN}Cambiar la primera nota de la materia {Back.BLACK}{Fore.GREEN}{persona['materia4']}:   ".ljust(10)))
                    persona["materia4_nota1"] = format(nota,".2f")

                elif opcion_str == 'N24':
                    nota = float(input(f"{Back.BLACK}{Fore.GREEN}Cambiar la primera nota de la materia {Back.BLACK}{Fore.GREEN}{persona['materia4']}:   ".ljust(10)))
                    persona["materia4_nota2"] = format(nota,".2f")

                elif opcion_str == 'V':
                    print("Saliendo del Menú...")
                    mostrar_persona(padron, dni)
                    return
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
                    time.sleep(3)

        except ValueError:
            print("Opción inválida. Por favor, seleccione una opción válida.")

        if encontrado==True:
#       guardar_padron_en_archivo(padron)
            mostrar_persona_a_modificar(padron, dni)
            input()
    
        else:
            print("No se encontró una persona con ese DNI.")

        


#################### FIN MODIFICACION DE DATOS DE ALUMNO


#FUNCION PARA BORRAR UNA PERSONA (OK)
#import os

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
    time.sleep(3)



#FUNCION MOSTRAR DATOS DE PERSONA PARA MODIFICAR SUS DATOS (OK)
def mostrar_persona_a_modificar_XXXXX(padron, dni):
    # Buscar la persona en el padrón
    colorama.init(autoreset=True)    
    
    
    for persona in padron:
        if persona["dni"] == dni:
            print(f"{Fore.LIGHTGREEN_EX}Datos a modificar del Alumno:")
            print("")
            
            #DATOS DEL ALUMNO
            print(f"{Back.BLACK}{Fore.WHITE}Apellido: {persona['apellido']}".ljust(39),
                f"{Back.BLACK}{Fore.WHITE}Nombres: {persona['nombres']}".ljust(45),
                f"{Back.BLACK}{Fore.WHITE}D.N.I.: {persona['dni']}".ljust(30),
                f"{Back.BLACK}{Fore.WHITE}Domicilio: {persona['domicilio']}".ljust(30)
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
            return
    ###OK###
    #hasta aqui todo ok
    # Si no se encuentra la persona
            print(f"{Back.WHITE}{Fore.RED}No se encontró una persona con ese DNI.")
            print(Style.RESET_ALL)  # Resetear los estilos después de imprimir

def mostrar_persona_a_modificar(padron, dni):
    # Buscar la persona en el padrón
    colorama.init(autoreset=True)
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


    if persona_encontrada is not None:
        print(f"{Fore.LIGHTGREEN_EX}Datos a modificar del Alumno:")
        print("")

        # DATOS DEL ALUMNO
        print(f"{Back.BLACK}{Fore.WHITE}Apellido: {persona_encontrada['apellido']}".ljust(39),
              f"{Back.BLACK}{Fore.WHITE}Nombres: {persona_encontrada['nombres']}".ljust(45),
              f"{Back.BLACK}{Fore.WHITE}D.N.I.: {persona_encontrada['dni']}".ljust(30),
              f"{Back.BLACK}{Fore.WHITE}Domicilio: {persona_encontrada['domicilio']}".ljust(30)
              )

        print("")
        # TITULOS SUBRAYADOS
        print(subrayar(
            f"{Back.BLACK}{Fore.BLUE}MATERIA".ljust(39),
            f"{Back.BLACK}{Fore.LIGHTBLUE_EX}PRIMERA NOTA".ljust(20),
            f"{Back.BLACK}{Fore.LIGHTBLUE_EX}SEGUNDA NOTA".ljust(20),
            f"{Back.BLACK}{Fore.LIGHTBLUE_EX}PROMEDIO".ljust(10),
            f"{Back.BLACK}{Fore.LIGHTBLUE_EX}SITUACION".ljust(10)
        ))

        # Cálculo de promedios
        materia1_promedio = ((float(persona_encontrada['materia1_nota1']) + float(persona_encontrada['materia1_nota2'])) / 2)
        materia2_promedio = ((float(persona_encontrada['materia2_nota1']) + float(persona_encontrada['materia2_nota2'])) / 2)
        materia3_promedio = ((float(persona_encontrada['materia3_nota1']) + float(persona_encontrada['materia3_nota2'])) / 2)
        materia4_promedio = ((float(persona_encontrada['materia4_nota1']) + float(persona_encontrada['materia4_nota2'])) / 2)

        # Imprimir datos de las materias
        print(f"{Back.BLACK}{Fore.GREEN}{persona_encontrada['materia1']}".ljust(39),
              f"{Back.BLACK}{Fore.GREEN}{persona_encontrada['materia1_nota1']}".ljust(22),
              f"{Back.BLACK}{Fore.GREEN}{persona_encontrada['materia1_nota2']}".ljust(22),
              f"{Back.BLACK}{Fore.GREEN}{materia1_promedio:.2f}".ljust(18),
              f"{Back.BLACK}{Fore.GREEN}{persona_encontrada['materia1_situacion']}".ljust(12)
              )

        print(f"{Back.BLACK}{Fore.YELLOW}{persona_encontrada['materia2']}".ljust(39),
              f"{Back.BLACK}{Fore.YELLOW}{persona_encontrada['materia2_nota1']}".ljust(22),
              f"{Back.BLACK}{Fore.YELLOW}{persona_encontrada['materia2_nota2']}".ljust(22),
              f"{Back.BLACK}{Fore.YELLOW}{materia2_promedio:.2f}".ljust(18),
              f"{Back.BLACK}{Fore.YELLOW}{persona_encontrada['materia2_situacion']}".ljust(12)
              )

        print(f"{Back.BLACK}{Fore.CYAN}{persona_encontrada['materia3']}".ljust(39),
              f"{Back.BLACK}{Fore.CYAN}{persona_encontrada['materia3_nota1']}".ljust(22),
              f"{Back.BLACK}{Fore.CYAN}{persona_encontrada['materia3_nota2']}".ljust(22),
              f"{Back.BLACK}{Fore.CYAN}{materia3_promedio:.2f}".ljust(18),
              f"{Back.BLACK}{Fore.CYAN}{persona_encontrada['materia3_situacion']}".ljust(12)
              )

        print(f"{Back.BLACK}{Fore.MAGENTA}{persona_encontrada['materia4']}".ljust(39),
              f"{Back.BLACK}{Fore.MAGENTA}{persona_encontrada['materia4_nota1']}".ljust(22),
              f"{Back.BLACK}{Fore.MAGENTA}{persona_encontrada['materia4_nota2']}".ljust(22),
              f"{Back.BLACK}{Fore.MAGENTA}{materia4_promedio:.2f}".ljust(18),
              f"{Back.BLACK}{Fore.MAGENTA}{persona_encontrada['materia4_situacion']}".ljust(12)
              )

        # Actualizar el promedio en la persona encontrada
        persona_encontrada['materia1_promedio'] = f"{materia1_promedio:.2f}"
        persona_encontrada['materia2_promedio'] = f"{materia2_promedio:.2f}"
        persona_encontrada['materia3_promedio'] = f"{materia3_promedio:.2f}"
        persona_encontrada['materia4_promedio'] = f"{materia4_promedio:.2f}"

        # Guardar los cambios en el archivo padron.csv
        with open('padron.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=padron[0].keys(), delimiter=';')
            writer.writeheader()
            writer.writerows(padron)

        print("Datos actualizados correctamente.")
    else:
        print("No se encontró una persona con ese DNI.")



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
                f"{Back.BLACK}{Fore.WHITE}D.N.I.: {persona['dni']}".ljust(40),
                f"{Back.BLACK}{Fore.WHITE}Domicilio: {persona['domicilio']}".ljust(30)
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
            persona['materia1_situacion'] = "Regularizada" if float(persona['materia1_promedio']) >= 6.00 else "No Regularizada"
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
            persona['materia2_situacion'] = "Regularizada" if float(persona['materia2_promedio']) >= 6.00 else "No Regularizada"
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
            persona['materia3_situacion'] = "Regularizada" if float(persona['materia3_promedio']) >= 6.00 else "No Regularizada"
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
            persona['materia4_situacion'] = "Regularizada" if float(persona['materia4_promedio']) >= 6.00 else "No Regularizada"
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



############ Menú de opciones

import os
os.system('cls' if os.name == 'nt' else 'clear') #Para limpiar la pantalla
      
# Función para subrayar el texto
def subrayar(*textos):
    return " ".join("\033[4m" + texto + "\033[0m" for texto in textos)

# Definir las opciones del menú con diferentes estilos
titulo = subrayar(f"{Fore.GREEN}{Style.BRIGHT}Ingrese la operación que desea realizar:")

opcion1 = f"{Fore.RESET}{Style.RESET_ALL}1. " + f"{Fore.WHITE}{Style.BRIGHT}Dar de Alta a una persona"
opcion2 = f"{Fore.RESET}{Style.RESET_ALL}2. " + f"{Fore.WHITE}{Style.BRIGHT}Modificar datos de la persona"
opcion3 = f"{Fore.RESET}{Style.RESET_ALL}3. " + f"{Fore.WHITE}{Style.BRIGHT}Eliminar a una persona"
opcion4 = f"{Fore.RESET}{Style.RESET_ALL}4. " + f"{Fore.WHITE}{Style.BRIGHT}Mostrar datos de una persona"
opcion5 = f"{Fore.RESET}{Style.RESET_ALL}5. " + f"{Fore.CYAN}Recargar/Importar listado de personas desde un archivo CSV"
opcion6 = f"{Fore.RESET}{Style.RESET_ALL}6. " + f"{Fore.WHITE}{Style.BRIGHT}Visualizar listado completo"
opcion7 = f"{Fore.RED}{Style.BRIGHT}0. " + f"{Fore.WHITE}{Style.BRIGHT}Salir del Menú "
opcion8 = f"¿Su opción? " + f"{Fore.RESET}{Style.RESET_ALL}-->>> "

# Concatenar las líneas del menú
texto_estilizado_0 = f"{titulo}\n\n{opcion1}\n{opcion2}\n{opcion3}\n{opcion4}\n{opcion5}\n{opcion6}\n{opcion7}\n{opcion8}"

# Solicitar la opción al usuario
#opcion_str = input(texto_estilizado_0)

while True:
    try:
            # Solicitar la opción al usuario
            opcion_str = input(texto_estilizado_0)
        
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

