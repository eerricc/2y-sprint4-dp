from datetime import datetime

def edit(lista):
    if not lista:
        print("empty list")
        return
    inp = input("name of the product to edit: ").strip()
    for item in lista:
        if item.get("name") == inp:
            try:
                while True:
                    print("""\n--- edit menu ---\n
1 - edit name
2 - edit quantity
3 - edit expiration date
4 - edit cost
5 - edit batch
0 - exit
""")

                    while True:
                        try:
                            num = int(input("type a number: ").strip())
                            if 0 <= num <= 5:
                                break
                            else:
                                print("-> 0-5 only")
                        except ValueError:
                            print("-> type a NUMBER")

                    match num:
                        case 1:
                            new_name = input("new name: ").strip()
                            if new_name:
                                item["name"] = new_name
                                print("-> name updated")
                            else:
                                print("-> name cannot be empty")
                        case 2:
                            while True:
                                qtd_str = input("new quantity: ")
                                if qtd_str.isdigit() and int(qtd_str) > 0:
                                    item["quantity"] = int(qtd_str)
                                    print("-> quantity updated")
                                    break
                                print("-> quantity must be a positive number")
                        case 3:
                            while True:
                                validade = input("new expiration date (dd/mm/yyyy): ").strip()
                                try:
                                    exp_date = datetime.strptime(validade, "%d/%m/%Y")
                                    if exp_date < datetime.now():
                                        print("-> this item has already expired")
                                        confirm = input("-> continue anyway? (y/n): ").lower()
                                        if confirm != 'y':
                                            continue
                                    item["validade"] = validade
                                    print("-> expiration date updated")
                                    break
                                except ValueError:
                                    print("-> invalid date format")
                        case 4:
                            while True:
                                cos = input("new cost per unit: ")
                                if cos.isdigit() and int(cos) > 0:
                                    item["cost/unit"] = int(cos)
                                    print("-> cost updated")
                                    break
                                print("-> cost must be a positive number")
                        case 5:
                            while True:
                                bat = input("new batch size: ")
                                if bat.isdigit() and int(bat) > 0:
                                    item["batch"] = int(bat)
                                    print("-> batch updated")
                                    break
                                print("-> batch size must be a positive number")
                        case 0:
                            print("-> Exiting...")
                            return
                        
                    quantidade = int(item.get("quantity", 0))
                    cost = int(item.get("cost/unit", 0))
                    batch = int(item.get("batch", 1))
                    item["total value"] = quantidade * cost * batch
                    return

            except KeyboardInterrupt:
                print("\n cancelled.")
                return

    print("-> item not found")