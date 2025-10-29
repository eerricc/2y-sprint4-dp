from datetime import datetime

def register(lista):
    print("\n --- MEDICAL INVENTORY REGISTRATION ---")
    while True:
        try:
            # get name
            while True:
                nome = input("item name: ").strip()
                break

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
                    exp_date = datetime.strptime(validade, "%d/%m/%Y")
                    # Check if date is in the future
                    if exp_date < datetime.now():
                        print("-> this item has already expired")
                        confirm = input("-> continue anyway? (y/n): ").lower()
                        if confirm != 'y':
                            continue
                    break
                except ValueError:
                    print("-> invalid date format")

            # get cost per unit
            while True:
                cos = input("cost per unit: ")
                if cos.isdigit() and int(cos) > 0:
                    cost = int(cos)
                    break
                print("-> cost must be a positive number")

            # append all data
            lista.append({
                "name": nome,
                "quantity": quantidade,
                "validade": validade,
                "cost/unit": cost,
            })

            print(f"\n item '{nome}' registered!")
            print(f" units: {quantidade}")
            print(f" expires: {validade}")
            return

        except KeyboardInterrupt:
            print("\n cancelled.")
            break