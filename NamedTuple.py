#7 Collections Part 2 - NamedTuple
import collections #optional import
from collections import namedtuple

print("-----NamedTuple Tutorial #1-----")
Point1 = namedtuple('Point', 'x y z') # x, y, and z get broken up into separate parameters
newP1 = Point1(3, 4, 5)
print(newP1)
Point2 = namedtuple('Point', 'x gy zc h')
newP2 = Point2(3, 4, 5, 8)
print(newP2)

print("\n-----NamedTuple Tutorial #2-----")
Point3 = namedtuple('Point', ['x', 'y', 'l']) # works with a list
newP3 = Point3(3, 4, 5)
print(newP3)

print("\n-----NamedTuple Tutorial #3-----")
Point4 = namedtuple('Point', {'x': 0, 'y': 0, 'z': 0}) # works with a dictionary, only recognizing the key names
newP4 = Point4(3, 4, 5)
print(newP4)
print(newP4.x, newP4.y, newP4.z)
print(newP4[0])
print(newP4._asdict())
print(newP4._fields)
print(newP4._replace(y = 6))
# or
newP5 = newP4._replace(x = 6)
print(newP5)

print("\n-----NamedTuple Tutorial #4-----")
p2 = Point4._make(['a', 'b', 'c'])
print(p2)