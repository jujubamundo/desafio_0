def gerar_asteriscos(n):
    return ['*' * i for i in range(1, n + 1)]

n = 5
resultado = gerar_asteriscos(n)
print(resultado)