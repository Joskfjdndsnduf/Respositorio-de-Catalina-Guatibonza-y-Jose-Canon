import asistencia_congreso as asis

def ejecutar_cargar_datos() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de asistencia de los congresistas
        Retorno: list
            La lista de asistencia por parte de congresistas de la camara de representantes
            a sesiones en el congreso.
    """
    asistencia = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con la asistencia: ")
    asistencia = asis.cargar_datos(archivo)
    if len(asistencia)==0:
        print("El archivo seleccionado no es válido. No se pudo cargar la información de la asistencia.")
    else:
        print("Se cargaron las asistencias de los siguientes congresistas a partir del archivo.")
        
    return asistencia

def ejecutar_mas_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar el congresista con mayor número de inasistencias injustificadas.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        El congresista (nombre_congresista) faltó (inasistencias) veces a sesiones de forma injustificada"
    """
    n=asis.inasistencias(asistencias)
    return print(n)
    #TODO: Completar la función

def ejecutar_mas_asistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar el congresista con mayor número de asistencias al congreso.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        El congresista (nombre_congresista) asistió (asistencias) veces a sesiones del congreso"
    """
    n=asis.asistencias(asistencias)
    return print(n)
    #TODO: Completar la función

def ejecutar_porcentaje_asistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar el porcentaje de asistencias por cada congresista.
        Se debe mostrar al usuario el nombre de cada congresista con su respectivo porcentaje de asistencia.
        A continuación se muestra un ejemplo de la salida esperada:
        (Nombre congresista 1) : (Porcentaje congresista 1)
        (Nombre congresista 2) : (Porcentaje congresista 2)
    """
    n=asis.promedio_congreso(asistencias)
    return print(n)
    #TODO: Completar la función

def ejecutar_circunscripcion_mas_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar la circunscripcion con mayor número de inaasistencias al congreso.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        La circunscripción (nombre circunscripcion) acumuló (número de fallas) fallas
    """
    n=asis.inasistenciasC(asistencias)
    return print(n)
    #TODO: Completar la función

def ejecutar_mas_inasistencias_excusa(asistencias:list)->None:
    """Ejecuta la opción de consultar el congresista con mayor número de inasistencias al congreso con excusa médica.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        El congresista (nombre congresista) falló (numero de inasistencias) veces con excusa médica
    """
    n=asis.inasistenciasEM(asistencias)
    return print(n)
    #TODO: Completar la función

def ejecutar_mas_X_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar los congresistas que fallan mas de un numero determinado de veces
        Se debe mostrar al usuario el nombre de cada congresista con su respectivo número de inasistencias.
        A continuación se muestra un ejemplo de la salida esperada:
        (Nombre congresista 1) : (inasistencias congresista 1)
        (Nombre congresista 2) : (inasistencias congresista 2)
        Si el diccionario está vacío debe retornar el siguiente mensaje:
        Ningún congresista supera el limite establecido
    """
    y=int(input("Introduzca el número a hallar congresistas con más fallas del número puesto:"))
    n=asis.numer_d_veces(asistencias,y)
    return print(n)
    #TODO: Completar la función

def ejecutar_asistencias_partido(asistencias:list)->None:
    """Ejecuta la opción de consultar los porcentajes de asistencias de los partidos politicos
        Se debe mostrar al usuario el nombre de cada partido con su respectivo porcentaje de inasistencias.
        A continuación se muestra un ejemplo de la salida esperada:
        (Nombre partido 1) : (porcentaje partido 1)
        (Nombre partido 2) : (porcentaje partido 2)
    """
    n=asis.promedio_partidos(asistencias)
    return print(n)
    #TODO: Completar la función

def ejecutar_fecha_mas_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar la fecha con mayor número de inasistencias
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        En la fecha (fecha) hubo (número de inasistencias) fallas
    """
    n=asis.funcion_9(asistencias)
    return print(n)
    #TODO: Completar la función

def ejecutar_mes_mayor_sesiones(asistencias:list)->None:
    """Ejecuta la opción de consultar el mes y año con mayor numero de sesiones
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        En el mes (mes/año) hubo (número de sesiones) sesiones
    """
    n=asis.funcion_10(asistencias)
    return print(n)
    #TODO: Completar la función

def ejecutar_asistio_fecha(asistencias:list):
    """Ejecuta la opción de consultar la asistencia de un congresista en una fecha determinada
        Si el congresista asistió a la sesion de la fecha, se debe mostrar el siguiente mensaje:
            El congresista (nombre congresista) asistió a la sesión de la fecha (dia)/(mes)/(anio)
        Si el congresista no asistio o no habia sesion ese dia, se muestra el siguiente mensaje:
            El congresista no asistio a la sesion o no hubo sesion ese dia
    """
    o=""
    d=input("Introduzca el día a consultar, si es un número menor a 0 ponga un 0 antes del número como por ejemplo 09: ")
    m=input("Introduzca el mes a consultar, si es un número menor a 0 ponga un 0 antes del número como por ejemplo 09 :")
    a=input("Introduzca el año a consultar: ")
    no=input("Introduzca el nombre a buscar: ")
    n=asis.funcion_11(asistencias,d,m,a,no)
    if n==True:
        o="El/La congresista asistió en la fecha situada."
    else:
        o="El/La conngresista no asistió en la fecha situada,"
    return print(o)
    #TODO: Completar la función

def ejecutar_asistencia_circunscripcion_fecha(asistencia:list)->None:
    """Ejecuta la opción de consultar la asistencia por circunscripcion en un mes y año determinado
        Se debe mostrar al usuario cada circunscripcion y su respectiva asistencia como se muestra a continuación:
        "(nombre circunscripcion) : (asistencia)"
    """
    
    m=input("Introduzca el mes a consultar, si es un número menor a 0 ponga un 0 antes del número como por ejemplo 09 :")
    a=input("Introduzca el año a consultar: ")
    n=asis.funcion_12(asistencia,m,a)
    return print(n)
    #TODO: Completar la función


def mostrar_menu():
    print("\nOpciones")
    print("1. Cargar el archivo con la asistencia al congreso")
    print("2. Consultar congresista con más inasistencias injustificadas")
    print("3. Consultar congresista con más asistencias")
    print("4. Calcular porcentaje de asistencia de los congresistas")
    print("5. Consultar la circunscripcion con mas inasistencias")
    print("6. Consultar el congresista con más inasistencias con excusa médica")
    print("7. Consultar congresistas que fallan más de un número determinado de veces")
    print("8. Consultar porcentaje de asistencias por partido político")
    print("9. Consultar fecha con más fallas")
    print("10. Consutlar mes y año con mayor número de sesiones realizadas")
    print("11. Consultar asistencias de congresista por fecha")
    print("12. Consultar asistencia por circunscripcion por mes y año")
    print("13. Salir de la aplicacion")

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar  = True
    asistencia = None
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            asistencia = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 3:
            ejecutar_mas_asistencias(asistencia)
        elif opcion_seleccionada == 4:
            ejecutar_porcentaje_asistencias(asistencia)
        elif opcion_seleccionada == 5:
            ejecutar_circunscripcion_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 6:
            ejecutar_mas_inasistencias_excusa(asistencia)
        elif opcion_seleccionada == 7:
            ejecutar_mas_X_inasistencias(asistencia)
        elif opcion_seleccionada == 8:
            ejecutar_asistencias_partido(asistencia)
        elif opcion_seleccionada == 9:
            ejecutar_fecha_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 10:
            ejecutar_mes_mayor_sesiones(asistencia)
        elif opcion_seleccionada == 11:
            ejecutar_asistio_fecha(asistencia)
        elif opcion_seleccionada == 12:
            ejecutar_asistencia_circunscripcion_fecha(asistencia)
        elif opcion_seleccionada == 13:
            continuar = False
        else:
            print("Por favor ingrese una opcion válida")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()