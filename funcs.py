from datetime import datetime
import time
import tracemalloc
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

def register():
    while True:
        try:
            # get name
            while True:
                nome = input("item name: ").strip()
                if nome: 
                    break
                print("type a name: ")

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

            # cost per unit
            # batch size

            consumos.append({
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
def check():
    # top down
    pass 

    # bottom up
    pass

def searcha():
    # top down
    pass 

    # bottom up
    pass


