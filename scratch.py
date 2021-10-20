def less_50(operated_number) -> bool:
    return operated_number < 50


a = [30, 35, 40, 45, 50, 55]

list_2 = []
for element in a:
    print(less_50(element))
    if not less_50(element):
        a.remove(element)
print(a)
