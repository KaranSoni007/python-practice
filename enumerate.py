# enumerate

names = ["Om", "Jay", "Het"]
marks = [80, 70, 90]

for index, name in enumerate(names):
    print(index, name)

# for i in range(len(names)):
#     print(i, names[i])

# zip

for name, mark in zip(names, marks):
    print(f"{name} -> {mark}")