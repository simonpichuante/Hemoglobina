#def funcion_positivo()

nivel_hemoglobina = float(input('Ingrese nivel de hemoglobina: '))
#print('Nivel de hemoglobina en la sangre es de: ', nivel_hemoglobina)
edad = int(input('Ingrese edad: '))
escala_edad = str(input('Ingrese 0 si tiene meses ó 1 si tiene años de edad: '))
genero = str(input('Ingrese 0 si es Masculino ó 1 si es Femenino: '))


def determinar_anemia(nivel_hemoglobina, edad, escala_edad, genero):
    # Convertir la edad a años si está en meses
    if escala_edad == "0":
        edad /= 12
    
    # Determinar los rangos de hemoglobina según la edad y el género
    if edad <= 1/12:
        rango_min, rango_max = 13, 26
    elif edad <= 0.5:
        rango_min, rango_max = 10, 18
    elif edad <= 1:
        rango_min, rango_max = 11, 15
    elif edad <= 5:
        rango_min, rango_max = 11.5, 15
    elif edad <= 10:
        rango_min, rango_max = 12.6, 15.5
    elif edad <= 15:
        rango_min, rango_max = 13, 15.5
    elif genero == "1":  # Mujeres > 15 años
        rango_min, rango_max = 12, 16
    else:  # Hombres > 15 años
        rango_min, rango_max = 14, 18
    
    # Determinar el resultado
    if nivel_hemoglobina < rango_min:
        resultado = "negativo (bajo el rango)"
    elif nivel_hemoglobina > rango_max:
        resultado = "negativo (sobre el rango)"
    else:
        resultado = "positivo"
    
    return resultado

# Ejemplo de uso
#nivel_hemoglobina = 13.5
#edad = 25
#escala_edad = "1"
#genero = "0"
resultado = determinar_anemia(nivel_hemoglobina, edad, escala_edad, genero)
print(f"El resultado es: {resultado}")

