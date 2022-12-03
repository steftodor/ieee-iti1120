from Point import Point

# Example with __init__ overloading
p = Point(3, 4)
print(p.get())
p.move(2,2)             # call the move method to move the point
print(p.get())          # call the get method to get the point

# Example with Default Values
p2 = Point()
print(p2.get())

# Example with __str__ overloading
p3 = Point(5, 6)
print(p3)

