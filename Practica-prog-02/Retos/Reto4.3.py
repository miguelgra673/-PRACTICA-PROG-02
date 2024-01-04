def esPalindromo(texto):
    texto = texto.lower()  
    texto_sin_espacios = ''.join(texto.split()) 
    return texto_sin_espacios == texto_sin_espacios[::-1]


texto_prueba = "OTTO"
resultado = esPalindromo(texto_prueba)
print(resultado)