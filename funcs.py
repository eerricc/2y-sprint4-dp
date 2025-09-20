from datetime import datetime
import time
import tracemalloc
from utils import quicksort
import random

# dummy medical items
consumos = [
    {"name": "Bandage", "quantity": 50, "validade": "15/12/2025"},
    {"name": "Syringe", "quantity": 120, "validade": "01/07/2026"},
    {"name": "Antibiotic", "quantity": 30, "validade": "20/05/2025"},
    {"name": "Painkiller", "quantity": 75, "validade": "11/11/2027"},
    {"name": "Saline Bag", "quantity": 40, "validade": "09/03/2026"}
]

random.shuffle(consumos)

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
                print("-> quantity must be a positive number")

            # get expiration date
            while True:
                validade = input("expiration date (dd/mm/yyyy): ").strip()
                try:
                    datetime.strptime(validade, "%d/%m/%Y")  # format
                    break
                except ValueError:
                    print("-> invalid date format")

            consumos.append({ # append to put everything in the end of the queue
                "name": nome,
                "quantity": quantidade,
                "validade": validade
            })

            print("-> success\n")
            return

        except KeyboardInterrupt:
            print("\n-> stopping.")
            break

# look
def consulta():
    if not consumos:
        print("-> there are no registers")
        return

    for item in reversed(consumos): # stack
        print(item)
    return

# search
def searcha():
    if not consumos:
        print("-> here are no registers")
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
                print("-> number please")

        match num:
            case 1:
                targ = input("type item name: ")

                tracemalloc.start()
                start_time = time.perf_counter()

                for item in consumos:
                    if item["name"] == targ:
                        print("-> found:", item)
                        break
                    else:
                        print("-> item not found")

                end_time = time.perf_counter()
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()


                print(f"time: {(end_time - start_time)*1000:.3f} ms")
                print(f"memory: {current/1024:.3f} KB | peak: {peak/1024:.3f} KB")
                return

            case 2:
                if consumos == sorted(consumos, key=lambda x: x["quantity"]):
                    pass
                else:
                    print("-> the queue is unsorted, sort it first")
                    return


                while True:
                    targ = input("type item amount: ")
                    if targ.isdigit() and int(targ) >= 0:
                        targ = int(targ)
                        break
                    else:
                        print("please type a non-negative number")

                tracemalloc.start()
                start_time = time.perf_counter()

                low, high = 0, len(consumos) - 1
                found = False
                while low <= high:
                    mid = (low + high) // 2
                    if consumos[mid]["quantity"] == targ:
                        print("-> found:", consumos[mid])
                        found = True
                        break
                    elif consumos[mid]["quantity"] < targ:
                        low = mid + 1
                    else:
                        high = mid - 1
                if not found:
                    print("item not found")

                end_time = time.perf_counter()
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                print(f"time: {(end_time - start_time)*1000:.3f} ms")
                print(f"memory: {current/1024:.3f} KB | peak: {peak/1024:.3f} KB")
                return



# sort
def sorta():
    global consumos

    if not consumos:
        print("-> there are no registers")
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

