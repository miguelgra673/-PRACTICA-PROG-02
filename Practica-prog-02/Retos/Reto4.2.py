def fibonacci(num):
    if num < 0 or num > 20:
        return "Número fuera del rango válido"
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, num + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[num]


resultado_fibonacci = fibonacci(0)
print(resultado_fibonacci)