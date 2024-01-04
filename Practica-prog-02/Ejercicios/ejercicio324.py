def filtrar_cadena(cadena, funcion_filtro):
    nueva_cadena = ""
    for caracter in cadena:
        if funcion_filtro(caracter):
            nueva_cadena = nueva_cadena + caracter
    return nueva_cadena


cadena_original = "¿Esto es la prueba 1 o la prueba 2?"
print("String original")
print(cadena_original)
print("String solo con las vocales")
cadena_vocales = filtrar_cadena(cadena_original, lambda car: car.lower() in {'a', 'e', 'i', 'o', 'u'})
print(cadena_vocales)

print("String solo con los caracteres en minúscula")
cadena_minusculas = filtrar_cadena(cadena_original, lambda car: car.islower())
print(cadena_minusculas)

print("String solo con los caracteres no alfabéticos")
cadena_no_alfabeticos = filtrar_cadena(cadena_original, lambda car: not car.isalpha())
print(cadena_no_alfabeticos)
