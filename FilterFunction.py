#4 Filter() Function

def add7(x):
    return x + 7

def isOdd(x):
    return x % 2 != 0

def isTrue(x): # the return value is not 0 so the function is true
    return 'Hello'

def isFalse(x): # the return value is 0 so the function is false
    return 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(isOdd, a)) # filter decides if something is true or false based on a given function

# filter works very with with map

c = list(map(add7, b))

d = list(map(add7, filter(isOdd, a)))

e = list(map(add7, filter(isTrue, a)))

f = list(map(add7, filter(isFalse, a)))

print("-----Filter Function-----")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)