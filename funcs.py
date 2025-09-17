from datetime import datetime
import time
import tracemalloc

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
                print("quantity must be positive")

            # get expiration date
            while True:
                validade = input("expiration date (dd/mm/yyyy): ").strip()
                try:
                    datetime.strptime(validade, "%d/%m/%Y")  # validate format
                    break
                except ValueError:
                    print("invalid date format. use dd/mm/yyyy")

            # If all good, append
            consumos.append({
                "name": nome,
                "quant": quantidade,
                "validade": validade
            })

            print("success\n")

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

# search
def searcha():
    while True:
        print("""
              1 - sequencial
              2 - binaria  
        """)
    
        while True:
            try:
                num = int(input("digite um numero"))
                break
            except ValueError:
                print("number please")

        match num:
            case 1:
                if not consumos:
                    print("nenhum registro")

                targ = input("digite o nome do item:")

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

                print(f"time: {(end_time - start_time)*1000:.3f} ms")
                print(f"memory usage: {current/1024:.3f} KB | peak: {peak/1024:.3f} KB")

            case 2:
                pass

# sort
def sorta():
    while True:
        print("""
        1 - nome
        2 - quantidade
        3 - validade  
        """)

        while True:
            try:
                num = int(input("digite um numero: "))
                break
            except ValueError:
                print("numeroooo")

        match num:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass