Here are the changes made:

1. Added `print_symbol` as a class attribute and initialized it to "#":

```python
print_symbol = "#"
```

2. Modified the `__str__` method to use the `print_symbol` attribute:

```python
def __str__(self):
    """Return the string representation of the rectangle with print_symbol"""
    if self.width == 0 or self.height == 0:
        return ""
    return "\n".join([str(self.print_symbol) * self.width for _ in range(self.height)])
```

Changed the "#" symbol to the class attribute `self.print_symbol` and converted it to a string, in case the print_symbol is not a string:

```python
str(self.print_symbol) * self.width
```

3. Updated the test cases to showcase the usage of `print_symbol`:

```python
r3 = Rectangle(2, 4)
Rectangle.print_symbol = "*"
print(r3)
r3.print_symbol = "$"
print(r3)
print("Number of instances:", Rectangle.number_of_instances)
```