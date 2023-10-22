def arrange_clothes(clothes, capacity):
    shelves = 0
    current_shelf_load = 0

    for cloth in clothes:
        if current_shelf_load + cloth <= capacity:
            current_shelf_load += cloth
        else:
            shelves += 1
            current_shelf_load = cloth

    if current_shelf_load > 0:
        shelves += 1

    return shelves

clothes = [int(x) for x in input().split()]
capacity = int(input())

shelves_used = arrange_clothes(clothes, capacity)

print(shelves_used)
