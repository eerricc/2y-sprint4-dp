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
0 - exit
""")
                    # editing menu
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
                        # edit name
                        case 1:
                            new_name = input("new name: ").strip()
                            if new_name:
                                item["name"] = new_name
                                print("-> name updated")
                            else:
                                print("-> name cannot be empty")
                        # edit quant
                        case 2:
                            while True:
                                qtd_str = input("new quantity: ")
                                if qtd_str.isdigit() and int(qtd_str) > 0:
                                    item["quantity"] = int(qtd_str)
                                    print("-> quantity updated")
                                    break
                                print("-> quantity must be a positive number")
                        # edit date
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
                        # edit cost
                        case 4:
                            while True:
                                cos = input("new cost per unit: ")
                                if cos.isdigit() and int(cos) > 0:
                                    item["cost/unit"] = int(cos)
                                    print("-> cost updated")
                                    break
                                print("-> cost must be a positive number")
                        case 0:
                            print("-> Exiting...")
                            return   
                    return

            except KeyboardInterrupt:
                print("\n cancelled.")
                return

    print("-> item not found")