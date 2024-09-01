def pares_menor_diferenca(arr):
    arr.sort()
    
    menor_diferenca = float('inf')
    
    pares = []
   
    for i in range(len(arr) - 1):
        diferenca = arr[i + 1] - arr[i]
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            pares = [(arr[i], arr[i + 1])]
        elif diferenca == menor_diferenca:
            pares.append((arr[i], arr[i + 1]))
    
    return pares

arr = [4, 9, 1, 32, 13, 5]
resultado = pares_menor_diferenca(arr)
print(resultado)