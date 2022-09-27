# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
import sys
import math
# We are not controlling the number of arguments
# Only getting the first

radius = float(sys.argv[1])
area = math.pi * radius**2

print(f"Area: {area}")
