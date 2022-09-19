from cat import Cat

cat = Cat("Sam", "m", 2)
print("Cat:")
for i in range(len(cat())):
    if i == 0:
        print("\tname =", cat.name)
    elif i == 1:
        print("\tsex =", cat.sex)
    else:
        print("\tage =", cat.age)

