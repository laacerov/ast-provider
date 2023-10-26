# -*- coding: utf-8 -*-

import csv
from datetime import datetime, timedelta

# Ruta al archivo CSV del mes actual
archivo_csv_mes_actual = '/var/log/asterisk/cdr-csv/Master-Mes-{}.csv'.format(datetime.now().strftime('%Y-%m'))

# Crear una cadena que contiene la fila de encabezado
encabezado = "accountcode;src;dst;dcontext;clid;channel;dstchannel;lastapp;lastdata;start;answer;end;duration;billsec;disposition;amaflags;Uniqueid\n"

# Diccionario para almacenar la duración por troncal
duraciones_por_troncal = {}

# Inicializar el total de consumo en segundos
consumo_total_mes = 0

# Abre el archivo CSV del mes actual en modo lectura
with open(archivo_csv_mes_actual, mode='r') as entrada:
    # Imprime un mensaje para verificar que se ha abierto el archivo
    print("Archivo abierto con éxito: {}".format(archivo_csv_mes_actual))

    # Crear un lector CSV para el archivo de entrada
    reader = csv.reader(entrada, delimiter=';', quotechar='"')

    # Imprime un mensaje para verificar que el lector CSV se ha creado
    print("Lector CSV creado")

    # Leer la fila de encabezado
    fila_encabezado = next(reader)
    print("Fila de encabezado: {}".format(fila_encabezado))

    # Procesar las filas
    for fila in reader:
        if len(fila) > 5:
            # Obtener el campo 'channel'
            channel = fila[5]

            # Extraer la troncal
            troncal = channel.split('/')[1].split('.')[0]

            # Sumar la duración al total de consumo del mes en segundos
            duracion = int(fila[12])
            consumo_total_mes += duracion

            # Actualizar el diccionario de duraciones por troncal
            if troncal in duraciones_por_troncal:
                duraciones_por_troncal[troncal] += duracion
            else:
                duraciones_por_troncal[troncal] = duracion

    # Calcular el consumo total del mes en minutos y segundos
    minutos, segundos = divmod(consumo_total_mes, 60)
    print("Consumo total del mes en curso: {} minutos y {} segundos".format(minutos, segundos))

    # Imprimir la duración por troncal
    for troncal, duracion in duraciones_por_troncal.items():
        troncal_minutos, troncal_segundos = divmod(duracion, 60)
        print("Duración por troncal {}: {} minutos y {} segundos".format(troncal, troncal_minutos, troncal_segundos))
