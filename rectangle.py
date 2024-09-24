class Rectangle:
    def __init__(self, length: int, width: int):
        self.dimensions = {'length': length, 'width': width}

    def __iter__(self):
        return iter(self.dimensions.items())

# Example usage
rectangle = Rectangle(5, 10)
for dimension, value in rectangle:
    print({dimension: value})
