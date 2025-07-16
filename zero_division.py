#!/usr/bin/env python3

value = 10
divider = 0

try:
    result = value / divider
    print(f"Result is: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero")
