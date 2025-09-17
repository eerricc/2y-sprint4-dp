from funcs import queuea, stacka, searcha, sorta

def main():
    while True:
        print("""
            1 - register items
            2 - consult items
            3 - locate items
            4 - sort items
            """)
        
        while True:
            try:
                num = int(input("type a number: "))
                break
            except ValueError:
                print("type a **number**")

        match num:
            case 1:
                queuea()
            case 2:
                stacka()
            case 3:
                searcha()
            case 4:
                sorta()
            case _:
                print("1 - 4 only")

if __name__ == "__main__":
    main()