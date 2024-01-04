def factorial(num):
    if num < 0 or num > 10:
        return "Número fuera del rango válido"
    elif num == 0 or num == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, num + 1):
            resultado *= i
        return resultado


resultado_factorial = factorial(3)
print(resultado_factorial)