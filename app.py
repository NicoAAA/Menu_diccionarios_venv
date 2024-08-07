'''
CENTRO DE BIOTECNOLOGIA AGROPECUARIO SENA

FICHA:    2877795
APRENDIZ: NICOLAS ANDRES ACOSTA HIGUERA
FECHA:    06 / 06 / 2024
PROHGRMA: MENÚ PRINCIPAL DICCIONARIO 
VERSION:  7.0
'''



# Importacion de módulos locales
from modulos.fnc import *

def main():
    """
    Función principal del programa. Muestra el título, el menú principal y ejecuta las acciones seleccionadas por el usuario.
    """
    titulo()
    datos = []
    
    while True:
        opciones_titulo()

        opciones = input('\n   Digite su opción: ').strip()
        print('-' * 55) 
        if opciones == '1':
            parametrizar(datos)
        elif opciones == '2':
            datos_aprendiz(datos)
        elif opciones == '3':
            ver_datos(datos)
        elif opciones == '4':
            buscar_por_ficha(datos)
        elif opciones == '5':
            mostrar_aprendices_por_ficha(datos)
        elif opciones == '6':
            eliminar_datos(datos)
        elif opciones == '7':
            editar_datos(datos)
        elif opciones == '0':
            print('\nGracias por usar el programa\n')
            print('-' * 55)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 0 al 7.")

# Ejecuta la funcion principal
if __name__ == '__main__':

    main()    


          


