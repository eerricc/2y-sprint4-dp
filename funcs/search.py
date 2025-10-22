def searcha(lista):
    user = input("what item are you looking for? ").strip()
    for item in lista:
        if item.get("name") == user:
            print(item)
            return
    print("-> item not found")


