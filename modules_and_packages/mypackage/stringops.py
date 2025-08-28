"""Simple string utilities."""

def reverse(s):
    """Return reversed string."""
    return s[::-1]

def is_palindrome(s):
    """Return True if s is palindrome (case-sensitive)."""
    return s == s[::-1]
