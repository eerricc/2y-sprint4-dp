consumos = []

# queue
def queuea():
    nome = input("Nome do insumo: ")
    quantidade = int(input("Quantidade consumida: "))
    validade = input("Validade (AAAA-MM-DD): ")

    consumos.append({
    "name": nome,
    "quant": quantidade,
    "validade": validade
    })
    
    print("success")

# stack
def stacka():
    if not consumos:
        print("Nenhum consumo registrado.")
        return

    for item in reversed(consumos):
        print(item)

# search
def searcha():
    while True:
        print("""
              1 - sequencial
              2 - binaria  
        """)
    
        while True:
            try:
                num = int(input("digite um numero"))
                break
            except ValueError:
                print("number please")

        match num:
            case 1:
                if not consumos:
                    print("nenhum registro")

                targ = input("digite o nome do item:")

                for item in consumos:
                    if item["name"] == targ:
                        print("encontrado: ", item)
                        break
                else:
                    print("nao encontrado")
            
            case 2:

# sort
def sorta():
    while True:
        print("""
        1 - nome
        2 - quantidade
        3 - validade  
        """)

        while True:
            try:
                num = int(input("digite um numero: "))
                break
            except ValueError:
                print("numeroooo")

        match num:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass