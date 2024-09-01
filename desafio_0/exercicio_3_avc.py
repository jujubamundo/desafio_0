from itertools import chain, combinations

def todos_subconjuntos(conjunto, max_size=None, min_size=0, distinct_only=False, sort_subsets=False):
    
    if distinct_only:
        conjunto = list(set(conjunto))
    
    subconjuntos = list(chain.from_iterable(combinations(conjunto, r) for r in range(min_size, (max_size or len(conjunto)) + 1)))
    
    subconjuntos = [list(subconjunto) for subconjunto in subconjuntos]
    
    if sort_subsets:
        subconjuntos = [sorted(subconjunto) for subconjunto in subconjuntos]
    
    if sort_subsets:
        subconjuntos.sort()

    return subconjuntos

conjunto = [1, 2, 2, 3]
resultado = todos_subconjuntos(conjunto, max_size=2, min_size=1, distinct_only=True, sort_subsets=True)
print(resultado)