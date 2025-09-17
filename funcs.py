from datetime import datetime
import time
import tracemalloc
from utils import merge_sort, quick_sort

consumos = []

def queuea():
    while True:
        try:
            # get name
            while True:
                nome = input("item name: ").strip()
                if nome: 
                    break
                print("type a name")

            # get quantity
            while True:
                qtd_str = input("item quantity: ")
                if qtd_str.isdigit() and int(qtd_str) > 0:
                    quantidade = int(qtd_str)
                    break
                print("quantity must be a positive number")

            # get expiration date
            while True:
                validade = input("expiration date (dd/mm/yyyy): ").strip()
                try:
                    datetime.strptime(validade, "%d/%m/%Y")  # format
                    break
                except ValueError:
                    print("invalid date format. use dd/mm/yyyy")

            consumos.append({
                "name": nome,
                "quant": quantidade,
                "validade": validade
            })

            print("success\n")
            return

        except KeyboardInterrupt:
            print("\nstopping.")
            break

# stack
def stacka():
    if not consumos:
        print("there are no registers")
        return

    for item in reversed(consumos):
        print(item)
    return

# search
def searcha():
    if not consumos:
        print("there are no registers")
        return
    
    while True:
        print("""
              1 - sequential
              2 - binary
        """)

        while True:
            try:
                num = int(input("digite um numero: "))
                break
            except ValueError:
                print("number please")

        match num:
            case 1:
                targ = input("digite o nome do item: ")

                tracemalloc.start()
                start_time = time.perf_counter()

                found = None
                for item in consumos:
                    if item["name"] == targ:
                        found = item
                        break

                end_time = time.perf_counter()
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                if found:
                    print("encontrado:", found)
                else:
                    print("nao encontrado")

                print(f"Tempo: {(end_time - start_time)*1000:.3f} ms")
                print(f"Memória usada: {current/1024:.3f} KB | Pico: {peak/1024:.3f} KB")

            case 2:
                pass


# sort
def sorta():
    global consumos

    if not consumos:
        print("there are no registers")
        return

    while True:
        print("""
        1 - merge sort
        2 - quick sort
        """)
        try:
            algo_choice = int(input("algo choice: "))
        except ValueError:
            print("numbers only")
            continue
        if algo_choice in (1,2):
            break
        print("either 1 or 2")

    # run chosen algorithm and measure
    tracemalloc.start()
    start_time = time.perf_counter()

    if algo_choice == 1:
        consumos = merge_sort(consumos)
        method = "merge sort"
    else:
        consumos = quick_sort(consumos)
        method = "quick sort"

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"list ordered by quantity using {method}.")
    print(f"time: {(end_time - start_time)*1000:.3f} ms")
    print(f"memory: {current/1024:.3f} KB | peak: {peak/1024:.3f} KB")
    return

