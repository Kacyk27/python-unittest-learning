width = int(input("Enter the width of the rectangle: "))
assert width > 0, "Must be positive."
height = int(input("Enter the height of the rectangle: "))
assert height > 0, "Must be positive."


area = width *height
print(area)