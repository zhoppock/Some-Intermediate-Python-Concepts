#6 Collections Part 1 - Counter
import collections #optional import
from collections import Counter

#Containers
#list
#set
#dict
#tuple - inmuttable

#Types
#1 counter <- this program
#2 deque
#3 namedTuple()
#4 orderedDict
#5 defaultdict

print("-----Counter Tutorial #1-----")
c = Counter('gallad')
print(c)

c = Counter(['a', 'a', 'b', 'c', 'c'])
print(c)
print(list(c.elements()))
print(c.most_common(2)) # prints out number of occurences of a value

c = Counter({'a': 1, "b": 2})
print(c)
print(list(c.elements())) # for a dictionary, prints a value as many times as it's associated value is set to

c = Counter(cats = 4, dogs = 7)
d = {'cat':2}
print(c)
print(c['cats'])
print(c['pet']) # results in 0
# print(d['pet'])   # results in error
print(list(c.elements()))

print("\n-----Counter Tutorial #2-----")
d = Counter(a = 4, b = 2, c = 0, d = -2)
e = ['a', 'b', 'b', 'c']
d.subtract(e)
print(d)
d.update(e)
print(d)
d.clear()
print(d)

print("\n-----Counter Tutorial #3-----")
f = Counter(a = 4, b = 2, c = 0, d = -2)
g = Counter(['a', 'b', 'b', 'c'])
print(f + g)
print(f - g) # if element count is less than 0, it will not be shown when printed
print(f & g) # an intersection of each Counter's elements
print(f | g) # an union of each Counter's elements