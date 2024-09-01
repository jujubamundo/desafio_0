def pares_menor_diferenca(arr, allow_duplicates=True, sorted_pairs=False, unique_pairs=False):
    arr.sort()
    
    
    menor_diferenca = float('inf')
    
    
    pares = []
    
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            diferenca = abs(arr[i] - arr[j])

            if not allow_duplicates and arr[i] == arr[j]:
                continue

            if diferenca < menor_diferenca:
                menor_diferenca = diferenca
                pares = [(arr[i], arr[j])]
            elif diferenca == menor_diferenca:
                pares.append((arr[i], arr[j]))
    
    if sorted_pairs:
        pares = [tuple(sorted(par)) for par in pares]
    
    if unique_pairs:
        pares = list(set(frozenset(par) for par in pares))
        pares = [tuple(sorted(par)) for par in pares]

    return pares

arr = [4, 9, 1, 32, 13, 5, 5]
resultado = pares_menor_diferenca(arr, allow_duplicates=False, sorted_pairs=True, unique_pairs=True)
print(resultado)