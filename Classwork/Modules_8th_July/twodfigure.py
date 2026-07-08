# ==========================================
# File Name : twodfigures.py
# Purpose   : User-defined module
# Contains functions for Area and Perimeter
# of different 2D figures.
# ==========================================

# Importing math module for value of pi
import math


# ---------- SQUARE ----------

def square_area(side):
    """Returns area of a square."""
    return side * side


def square_perimeter(side):
    """Returns perimeter of a square."""
    return 4 * side


# ---------- CIRCLE ----------

def circle_area(radius):
    """Returns area of a circle."""
    return math.pi * radius * radius


def circle_perimeter(radius):
    """Returns circumference of a circle."""
    return 2 * math.pi * radius


# ---------- RECTANGLE ----------

def rectangle_area(length, breadth):
    """Returns area of a rectangle."""
    return length * breadth


def rectangle_perimeter(length, breadth):
    """Returns perimeter of a rectangle."""
    return 2 * (length + breadth)


# ---------- TRIANGLE ----------

def triangle_area(base, height):
    """Returns area of a triangle."""
    return 0.5 * base * height


def triangle_perimeter(side1, side2, side3):
    """Returns perimeter of a triangle."""
    return side1 + side2 + side3