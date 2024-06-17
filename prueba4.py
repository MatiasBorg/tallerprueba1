def fibonacci(n):
    if n <= 0:
        return "El número debe ser mayor que cero."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_number = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_number)
        return fib_sequence

# Ejemplo de uso
n = 10
resultado = fibonacci(n)
print(resultado)
