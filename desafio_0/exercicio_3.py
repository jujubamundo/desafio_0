from itertools import chain, combinations

def todos_subconjuntos(conjunto):
 
    subconjuntos = list(chain.from_iterable(combinations(conjunto, r) for r in range(len(conjunto) + 1)))
    return [list(subconjunto) for subconjunto in subconjuntos]

conjunto = [1, 2]
resultado = todos_subconjuntos(conjunto)
print(resultado)