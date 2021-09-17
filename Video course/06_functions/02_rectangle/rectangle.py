def area(width, height):

    if not (isinstance(width,(int,float)) and isinstance(height,(int,float))):
        raise TypeError("Width, Height must be int/float")

    if not (width > 0 and height > 0):
        raise ValueError("Width,Height must be positive.")

    return width * height

def perimeter(width,height):

    if not (isinstance(width,(int,float)) and isinstance(height,(int,float))):
        raise TypeError("Width, Height must be int/float")

    if not (width > 0 and height > 0):
        raise ValueError("Width,Height must be positive.")

    return 2 * width + 2 * height

