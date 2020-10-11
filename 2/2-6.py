
goods_amount = int(input("How many goods you want to add? "))
structure = []
analytycs = {}
final_structure = []

for i in range(goods_amount):
    item = input(f"Enter item {i+1}: ")
    price = int(input(f"Enter price {i+1}: "))
    qty = int(input(f"Enter quantity {i+1}: "))
    unit = input(f"Enter unit {i+1}: ")
    structure = (i+1, {"Item":item, "Price":price, "Quantity":qty, "Unit":unit})
    final_structure.append(structure)
    for k in final_structure[i][1::]:
        for key, val in k.items():
            analytycs.setdefault(key, []).append(val)


print(final_structure)
print(analytycs)









