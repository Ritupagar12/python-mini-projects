"""mypackage - small demo package."""

from .mathops import add, factorial
from .stringops import reverse, is_palindrome

__all__ = ["add", "factorial", "reverse", "is_palindrome"]
__version__ = "0.1.0"
