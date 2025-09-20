from funcs import queuea, consulta, searcha, sorta

def main():
    while True:
        print("""\n--- menu ---\n
1 - register items
2 - consult items
3 - locate items
4 - sort items
0 - exit
        """)

        while True:
            try:
                print("----------")
                num = int(input("type a number: ").strip())
                if 0 <= num <= 4:
                    break
                else:
                    print("-> 1-4 or 0 only\n")
            except ValueError:
                print("-> type a **number**\n")

        match num:
            case 1:
                queuea()
            case 2:
                consulta()
            case 3:
                searcha()
            case 4:
                sorta()
            case 0:
                print("-> Exiting...")
                return
            
if __name__ == "__main__":
    main()