


def total_inventory_value_top(lista):
    """
    top-down 
    (recursive + memo) 
    calculation of total inventory value
    """
    memo = {}
    def helper(idx):
        if idx in memo:
            return memo[idx]
        if idx >= len(lista):
            return 0
        item = lista[idx]
        try:
            qty = int(item.get("quantity", 0))
        except (TypeError, ValueError):
            qty = 0
        try:
            cost = int(item.get("cost/unit", 0))
        except (TypeError, ValueError):
            cost = 0
        val = qty * cost + helper(idx + 1)
        memo[idx] = val
        return val

    return helper(0)


def total_inventory_value_bot(lista):
    """
    bottom-up 
    (iterative) 
    calculation of total inventory value
    """
    total = 0
    for item in lista:
        try:
            qty = int(item.get("quantity", 0))
        except (TypeError, ValueError):
            qty = 0
        try:
            cost = int(item.get("cost/unit", 0))
        except (TypeError, ValueError):
            cost = 0
        total += qty * cost
    return total


def highest_total_product_top(lista):
    """
    top-down 
    (recursive + memo)
    find the product with highest total value
    """
    if not lista:
        return None
    memo = {}
    def helper(idx):
        # returns tuple (best_index, best_value) for sublist starting at idx
        if idx in memo:
            return memo[idx]
        if idx >= len(lista):
            return (None, -1)
        item = lista[idx]
        try:
            qty = int(item.get("quantity", 0))
            cost = int(item.get("cost/unit", 0))
        except (TypeError, ValueError):
            qty = 0
            cost = 0
        curr_val = qty * cost
        next_best_idx, next_best_val = helper(idx + 1)
        if curr_val >= next_best_val:
            res = (idx, curr_val)
        else:
            res = (next_best_idx, next_best_val)
        memo[idx] = res
        return res

    best_idx, best_val = helper(0)
    if best_idx is None:
        return None
    return {"item": lista[best_idx], "total_value": best_val}


def highest_total_product_bot(lista):
    """
    bottom-up 
    (iterative)
    find the product with highest total value
    """
    if not lista:
        return None
    best_item = None
    best_value = -1
    for item in lista:
        try:
            qty = int(item.get("quantity", 0))
            cost = int(item.get("cost/unit", 0))
        except (TypeError, ValueError):
            continue
        val = qty * cost
        if val > best_value:
            best_value = val
            best_item = item
    if best_item is None:
        return None
    return {"item": best_item, "total_value": best_value}