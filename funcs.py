from datetime import datetime
import time
import tracemalloc
from utils import quicksort

consumos = [] # queue

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

            consumos.append({ # append to put everything in the end of the queue
                "name": nome,
                "quant": quantidade,
                "validade": validade
            })

            print("success\n")
            return

        except KeyboardInterrupt:
            print("\nstopping.")
            break

# look
def consulta():
    if not consumos:
        print("there are no registers")
        return

    for item in reversed(consumos): # stack
        print(item)
    return

# search
def searcha():
    if not consumos:
        print("there are no registers")
        return
    
    while True:
        print("""
              1 - search by name (sequential)
              2 - search by quantity (binary)
        """)

        while True:
            try:
                num = int(input("pick a number: "))
                if num == 1 or num == 2:
                    break
                else:
                    return False
                
            except ValueError:
                print("number please")

        match num:
            case 1:
                targ = input("type item name: ")

                tracemalloc.start()
                start_time = time.perf_counter()

                for item in consumos:
                    if item["name"] == targ:
                        print("found:", item["name"])
                        break
                    else:
                        print("item not found")

                end_time = time.perf_counter()
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()


                print(f"Tempo: {(end_time - start_time)*1000:.3f} ms")
                print(f"Memória usada: {current/1024:.3f} KB | Pico: {peak/1024:.3f} KB")

            case 2:
                if consumos == sorted(consumos):
                    continue
                else:
                    print("the queue is unsorted, sort it first")

                # binary search


                targ = input("type item amount: ")

                tracemalloc.start()
                start_time = time.perf_counter()

                end_time = time.perf_counter()
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                print(f"Tempo: {(end_time - start_time)*1000:.3f} ms")
                print(f"Memória usada: {current/1024:.3f} KB | Pico: {peak/1024:.3f} KB")



# sort
def sorta():
    global consumos

    if not consumos:
        print("there are no registers")
        return

    tracemalloc.start()
    start_time = time.perf_counter()

    consumos = quicksort(consumos)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"list ordered by quantity using quicksort.")
    print(f"time: {(end_time - start_time)*1000:.3f} ms")
    print(f"memory: {current/1024:.3f} KB | peak: {peak/1024:.3f} KB")
    return

