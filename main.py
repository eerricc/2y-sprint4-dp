from funcs.check import check
from funcs.register import register
from funcs.search import searcha
from funcs.edit import edit
from funcs.dp import * 
from utils import compare_methods


# wrap top-down and bottom-up implementations
total_inventory_value_top = compare_methods(total_inventory_value_bot)(total_inventory_value_top)
highest_total_product_top = compare_methods(highest_total_product_bot)(highest_total_product_top)

# dummy data
lista = [
    {
        "name": "Paracetamol 500mg",
        "quantity": 50,
        "validade": "15/12/2025",
        "cost/unit": 2,
        "batch": 1,
    },
    {
        "name": "Aspirin 100mg",
        "quantity": 20,
        "validade": "01/01/2020",
        "cost/unit": 3,
        "batch": 2,
    },
    {
        "name": "Insulin",
        "quantity": 10,
        "validade": "01/03/2026",
        "cost/unit": 50,
        "batch": 1,
    }
]

def main():
    while True:
        print("""\n--- menu ---\n
1 - register items
2 - check items
3 - search
4 - edit
5 - check total value
0 - exit
        """)

        while True:
            try:
                num = int(input("type a number: ").strip())
                if 0 <= num <= 5:
                    break
                else:
                    print("-> 0-5 only\n")
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
            case 5:
                total_top_res, total_bot_res, td_time, bu_time, td_mem, bu_mem = total_inventory_value_top(lista)
                best_top_res, best_bot_res, best_td, best_bu, best_td_mem, best_bu_mem = highest_total_product_top(lista)

                print("\n--- total cost ---")
                print(f"Top-down total: {total_top_res} (time={td_time:.6f}s, peak_mem={td_mem/1024:.2f} KB)")
                print(f"Bottom-up total: {total_bot_res} (time={bu_time:.6f}s, peak_mem={bu_mem/1024:.2f} KB)")

                print("\n--- highest product value ---")
                if best_top_res:
                    bi = best_top_res.get("item", {})
                    print(f"Top-down best product: {bi.get('name')} (value={best_top_res.get('total_value')}) (time={best_td:.6f}s, peak_mem={best_td_mem/1024:.2f} KB)")
                else:
                    print("Top-down best product: none")

                if best_bot_res:
                    bi = best_bot_res.get("item", {})
                    print(f"Bottom-up best product: {bi.get('name')} (value={best_bot_res.get('total_value')}) (time={best_bu:.6f}s, peak_mem={best_bu_mem/1024:.2f} KB)")
                else:
                    print("Bottom-up best product: none")
            case 0:
                print("-> Exiting...")
                return
            
if __name__ == "__main__":
    main()