def is_fibonacci(num):
    a = 0
    b = 1

    while a < num:
        prox_valor = a
        a = b
        b = prox_valor + b

    if a == num:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."
    
numero = int(input("Informe um número: "))
print(is_fibonacci(numero))