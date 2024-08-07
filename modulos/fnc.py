"""
CENTRO DE BIOTECNOLOGIA AGROPECUARIO SENA

FICHA:    2877795
APRENDIZ: NICOLAS ANDRES ACOSTA HIGUERA
FECHA:    06 / 06 / 2024
PROHGRMA: MENÚ PRINCIPAL DICCIONARIO(FUNCIONES)
VERSION:  7.0

"""

# Importacion de librerias de terceros
from tabulate import tabulate

def titulo():
    """
    Imprime el título del programa.
    """
    print('╔═════════════════════════════════════════════════════╗')
    print('║                                                     ║')
    print('║        CENTRO DE BIOTECNOLOGIA  AGROPECUARIO        ║')
    print('║                                                     ║')
    print('║                Mosquera - CBA - SENA                ║')
    print('║                                                     ║')
    print('╚═════════════════════════════════════════════════════╝\n')
    print(input('   Presiona enter para continuar . . . '))

def opciones_titulo():
    """
    Imprime el menú principal del programa.
    """
    print('')
    print('╔═════════════════════════════════════════════════════╗')
    print('║                   MENÚ  PRINCIPAL                   ║')
    print('╚═════════════════════════════════════════════════════╝')
    print('╔═════════════════════════════════════════════════════╗')
    print('║                                                     ║')
    print('║                                                     ║')
    print('║  ° Elige una opcion para continuar (solo números).  ║')
    print('║                                                     ║')
    print('║                                                     ║')
    print('║                                                     ║')
    print('║   ( 1 ) PARAMETRIZAR                                ║')
    print('║                                                     ║')
    print('║   ( 2 ) INGRESO APRENDIZ                            ║')
    print('║                                                     ║')
    print('║   ( 3 ) LISTA APRENDICES                            ║')
    print('║                                                     ║')
    print('║   ( 4 ) LISTA POR FICHAS                            ║')
    print('║                                                     ║')
    print('║   ( 5 ) RESULTADO APRENDICES POR FICHA              ║')
    print('║                                                     ║')
    print('║   ( 6 ) BORRAR APRENDIZ                             ║')
    print('║                                                     ║')
    print('║   ( 7 ) ACTUALIZAR INFORMACION                      ║')
    print('║                                                     ║')
    print('║   ( 0 ) SALIR                                       ║')
    print('║                                                     ║')
    print('║                                                     ║')
    print('╚═════════════════════════════════════════════════════╝')

def validar_cedula():
    """
    Valida que la cédula ingresada sea un número de 6 a 10 dígitos.
    Devuelve la cédula si es válida.
    """
    while True:
        cedula = input('DOCUMENTO: ')
        if cedula.isdigit() and 6 <= len(cedula) <= 10:
            return cedula
        else:
            if not cedula.isdigit():
                print("La cédula debe contener solo números.")
            else:
                print("La cédula debe tener entre 6 y 10 dígitos.")

def validar_ficha():
    """
    Valida que la ficha ingresada sea un número de 7 dígitos.
    Devuelve la ficha si es válida.
    """
    while True:
        ficha = input('FICHA: ')
        if ficha.isdigit() and  len(ficha) == 7:
            return ficha
        else:
            if not ficha.isdigit():
                print("Error: La ficha debe contener solo números.")
            else:
                print("Error: La ficha debe tener 7 digitos")

def validar_nombre():
    """
    Valida que el nombre ingresado solo contenga letras y espacios.
    Devuelve el nombre si es válido.
    """
    while True:
        nombre = input("NOMBRE: ").strip()
        if all(x.isalpha() or x.isspace() for x in nombre):
            return nombre.title()
        else:
            print("El NOMBRE solo debe contener letras y espacios.")

def validar_calificacion():
    """
    Valida que la calificación ingresada sea 'A' o 'D'.
    Devuelve la calificación si es válida.
    """
    while True:
        calificacion = input("CALIFICACION (A/D): ").strip().upper()
        if calificacion in ('A', 'D'):
            return calificacion
        else:
            print("\nCalificación no válida. Por favor, ingrese 'A' para aprobado o 'D' para desaprobado.\n")

def parametrizar(datos):
    """
    Esta función borra todos los datos guardados si el usuario confirma la acción.
    """
    while True:
        guardar_mas = input('Esta opcion borra todos los dotos guardados\n¿Seguro que quiere eliminar todo? (s/n): \n').strip().lower()
        if guardar_mas == 's':
            datos.clear()
            print('\nDatos borrados satisfactoriamente.\n')
            input('\nPresiona enter para volver al menú principal. . .\n')
            break 
        elif guardar_mas == 'n':
            input('\nPresiona enter para volver al menú principal. . .\n')
            break
        else:
            print("\nOpción no válida. Por favor, ingrese 's' para sí o 'n' para no.\n")
                

def datos_aprendiz(datos):
    """
    Esta función permite ingresar los datos de un aprendiz.
    """
    print('Ingreso aprendiz.\n')
    while True:
        documento= validar_cedula()
        nombre= validar_nombre()
        ficha= validar_ficha()
        calificacion= validar_calificacion()
        datos.append({'NOMBRE': nombre,'DOCUMENTO':documento,'FICHA':ficha,'CALIFICACION':calificacion})
        print('\nDatos añadidos correctamente.\n')

        while True:
            guardar_mas = input('¿Quiere guardar más datos? (s/n): \n').strip().lower()
            if guardar_mas in ('s', 'n'):
                break
            else:
                print("\nError: opción no válida. Por favor, ingrese 's' para sí o 'n' para no.\n")
        if guardar_mas == 'n':
            break

def ver_datos(data):
    """
    Esta función muestra los datos guardados en una tabla.
    """
    if data:
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
        input("\nPresiona enter para volver al menú principal. . .\n")
    else:
        print("No hay datos para mostrar.\n")
        input("Presiona enter para volver al menú principal. . .\n")

def eliminar_datos(data):
    """
    Esta función permite eliminar los datos de un aprendiz.
    """
    if data:
        print('\nEliminar datos de Aprendiz\n')
        while True:
            cedula = validar_cedula()
            indices = [i for i, registro in enumerate(data) if registro['DOCUMENTO'] == cedula]
            
            if indices:
                for index in sorted(indices, reverse=True):
                    del data[index]
                print("Datos eliminados correctamente.\n")
                input("Presione enter para volver al menú principal. . .")
                break
            else:
                print("Número de documento no encontrado. Por favor, intente de nuevo.")
    else:
        print("No hay datos para eliminar.\n")
        input('Presione enter para volver al menú principal. . . ')


def buscar_por_ficha(data):
    """
    Esta función permite buscar aprendices por ficha.
    """
    print('\nLista de aprendices por ficha.\n')
    if data:
        ficha = validar_ficha()
        resultados = [registro for registro in data if registro.get('FICHA') == ficha]
        
        if resultados:
            print(tabulate(resultados, headers="keys", tablefmt="fancy_grid"))
            input('Presione enter para volver al menú principal. . . ')
        else:
            print("\nNúmero de ficha no encontrado.\n")
            
    else:
        print("No hay datos para buscar.")
        input('Presione enter para volver al menú principal. . . ')


def editar_datos(data):
    """
    Permite editar los datos de un aprendiz.
    
    Si hay datos disponibles, se solicita la cédula del aprendiz cuyos datos se desean editar.
    Se puede actualizar el nombre, documento, ficha y calificación del aprendiz.
    """
    
    if data:
        print('Actualizar datos\n')
        print('Digite el número de cedula de la persona que quiere editar\nlos datos. Presione enter sobre la opcion si no quiere editar \nesa parte.Digite el posible cambio de informacion y dele a \nenter, despues digite la nueva informacion y dele a enter.\n\n')

        while True:
            cedula = validar_cedula()
            indices = [i for i, registro in enumerate(data) if registro.get('DOCUMENTO') == cedula]
            
            if indices:
                index = indices[0]  
                print(f"\nEditando datos de la persona con cédula: {cedula}")
                nombre = input(f"Nombre [{data[index]['NOMBRE']}]: ").strip()
                if nombre:
                    nombre = validar_nombre()
                else:
                    nombre = data[index]['NOMBRE']
                
                nueva_cedula = input(f"Documento [{data[index]['DOCUMENTO']}]: ").strip()
                if nueva_cedula:
                    nueva_cedula = validar_cedula()
                else:
                    nueva_cedula = data[index]['DOCUMENTO']
                


                ficha = input(f"Ficha [{data[index]['FICHA']}]: ").strip()
                if ficha:
                    ficha = validar_ficha()
                else:
                    ficha = data[index]['FICHA']


                calificacion = input(f"Calificación [{data[index]['CALIFICACION']}]: ").strip().lower()
                if calificacion:
                    calificacion = validar_calificacion()
                else:
                    calificacion = data[index]['CALIFICACION']
                
                data[index] = {"NOMBRE": nombre, "DOCUMENTO": nueva_cedula, "FICHA": ficha, "CALIFICACION":calificacion}
                print("\nDatos actualizados correctamente.\n")
                input('Presione enter para volver al menú principal. . . ')


                break
            else:
                print("\nNúmero de cédula no encontrado. Por favor, intente de nuevo.\n")
    else:
        print("\nNo hay datos para editar.\n")
        input('Presione enter para volver al menú principal. . . ')

def mostrar_aprendices_por_ficha(data):
    """
    Esta función muestra los aprendices por ficha.
    """
    if data:
        fichas = {}
        for registro in data:
            ficha = registro.get('FICHA')
            if ficha not in fichas:
                fichas[ficha] = []
            fichas[ficha].append({"NOMBRE": registro.get('NOMBRE'), "CALIFICACION": registro.get('CALIFICACION')})

        for ficha, aprendices in fichas.items():
            print(f"\nFICHA {ficha}")
            print(tabulate(aprendices, headers="keys", tablefmt="fancy_grid"))
            input('Presione enter para continuar. . . ')
    else:
        print("No hay datos para mostrar.")
