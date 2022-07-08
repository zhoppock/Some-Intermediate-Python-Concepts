#3 Map() Function

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x ** x

# for loop method
print("-----For Loop Method-----")
newList = []
for x in li:
    newList.append(func(x))
print(newList)

# map method
print("\n-----Map Method-----")
print(list(map(func, li)))

# list comprehension method
print("\n-----List Comprehension Method-----")
print([func(x) for x in li])
print([func(x) for x in li if x % 2 == 0])