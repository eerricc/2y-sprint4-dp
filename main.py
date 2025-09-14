def main():
    while True:
        print("""
            1 - registrar consumo
            2 - consultar consumo
            3 - localizar consumo
            4 - ordenar consumo
            """)
        
        while True:
            try:
                num = int(input("digite um numero: "))
                break
            except ValueError:
                print("digite um **numero**")

        match num:
            case 1:
                queuea()
            case 2:
                stacka()
            case 3:
                searcha()
            case 4:
                sorta()

if __name__ == "__main__":
    main()