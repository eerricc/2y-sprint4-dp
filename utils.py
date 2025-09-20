def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    menores = []
    maiores = []
    for elemento in lista[1:]:
        if elemento["quantity"] < pivot["quantity"]:
            menores.append(elemento)
        else:
            maiores.append(elemento)
    menores = quicksort(menores)
    maiores = quicksort(maiores)
    return menores + [pivot] + maiores

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i]["quantity"] > lst[i+1]["quantity"]:
            return False
    return True
