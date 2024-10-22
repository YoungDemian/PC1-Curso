def convertir_hora(hora_str):
    try:
        horas, minutos = map(int, hora_str.split(":"))
        if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
            return None
        return horas + minutos / 60
    except ValueError:
        return None
hora_ingresada = input("Por favor, introduce la hora en formato 24 horas (##:##): ")
hora_decimal = convertir_hora(hora_ingresada)
if hora_decimal is not None:
    if 7 <= hora_decimal <= 8:
        print("Es hora del desayuno.")
    elif 12 <= hora_decimal <= 13:
        print("Es hora del almuerzo.")
    elif 18 <= hora_decimal <= 19:
        print("Es hora de la cena.")
    else:
        print("No es hora de comer.")
else:
    print("Formato de hora no válido. Intente de nuevo con el formato ##:##.")
