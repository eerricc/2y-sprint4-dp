from funcs import register, check, searcha

def main():
    while True:
        print("""\n--- menu ---\n
1 - register items
2 - check items
3 - locate items
4 - 
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
                register()
            case 2:
                check()
            case 3:
                searcha()
            case 4:
                pass
            case 0:
                print("-> Exiting...")
                return
            
if __name__ == "__main__":
    main()