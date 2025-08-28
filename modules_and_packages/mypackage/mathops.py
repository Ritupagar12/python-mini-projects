""" Simple math utilities for demo."""

def add(a, b):
    """Return a + b"""
    return a + b

def factorial(n):
    """Return factorial of n (recursive)."""
    return 1 if n == 0 else n * factorial(n - 1)
