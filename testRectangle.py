from rectangle import Rectangle

r1 = Rectangle(10,5)
r2 = Rectangle(9,9)

print("r1.per=", r1())
print("r1.def=", r1.getSizes())


r1.height = 3
print("r1.per=", r1())
print("r1.def=", r1.getSizes())
# print("r1.getWidth=", r1.getWidth())
# print("r1.getArea=", r1())
# print("r2.width=", r2.width)
# print("r2.height=", r2.height)
# print("r2.getWidth=", r2.getWidth)
# print("r2.getHeight=", r2.getHeight())
# print("r2.getArea=", r2.getArea())