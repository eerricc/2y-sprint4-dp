from funcs.check import check
from funcs.register import register
from funcs.search import searcha
from funcs.edit import edit


lista = [
    {
        "name": "Paracetamol 500mg",
        "quantity": 50,
        "validade": "15/12/2025",
        "cost/unit": 2,
        "batch": 1,
        "total value": 50 * 2 * 1
    },
    {
        "name": "Aspirin 100mg",
        "quantity": 20,
        "validade": "01/01/2020",
        "cost/unit": 3,
        "batch": 2,
        "total value": 20 * 3 * 2
    },
    {
        "name": "Insulin",
        "quantity": 10,
        "validade": "01/03/2026",
        "cost/unit": 50,
        "batch": 1,
        "total value": 10 * 50 * 1
    }
]

def main():
    while True:
        print("""\n--- menu ---\n
1 - register items
2 - check items
3 - search
4 - edit
0 - exit
        """)

        while True:
            try:
                num = int(input("type a number: ").strip())
                if 0 <= num <= 4:
                    break
                else:
                    print("-> 1-4 or 0 only\n")
            except ValueError:
                print("-> type a **number**\n")

        match num:
            case 1:
                register(lista)
            case 2:
                check(lista)
            case 3:
                searcha(lista)
            case 4:
                edit(lista)
            case 0:
                print("-> Exiting...")
                return
            
if __name__ == "__main__":
    main()