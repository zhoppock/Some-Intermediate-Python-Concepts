#8 Collections Part 3 - Deque
import collections #optional import
from collections import deque

print("-----Deque Tutorial #1-----")
d = deque("hello")
print(d)
d.append('4') # add an element to the end of the list
d.append(5)
print(d)
d.appendleft(5) # add an element to the beginning of the list
print(d)
d.pop() # remove an element from the end of the list
d.popleft() # remove an element from the beginning of the list
print(d)
d.clear()
print(d)

print("\n-----Deque Tutorial #2-----")
d.extend('456') # add elements to the end of the list
print(d)
d.extend([1, 2, 3])
print(d)
d.extendleft('hey') # add elements to the beginning of the list
print(d)

print("\n-----Deque Tutorial #3-----")
d.rotate(-1) # shift elements 1 to the left
print(d)
d.rotate(-2) # shift elements 2 to the left
print(d)
d.rotate(1) # shift elements 1 to the right
print(d)

print("\n-----Deque Tutorial #4-----")
e = deque("hello", maxlen = 5) # sets up a list that has a max of 5 elements, cannot change the max length
print(e)
e.append(1) # puts in a new element on the right and deletes the first element on the left
print(e)
e.extend([2, 3]) # puts in 2 elements on the right and deletes the first 2 elements on the left
print(e)
print(e.maxlen)