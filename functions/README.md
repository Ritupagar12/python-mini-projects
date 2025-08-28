## Functions 

This folder contains mini projects to learn Python functions.

### 1. [Calculator](calculator_function.py)
Performs basic arithmetic operations using functions.
**Features:**
- Functions for add, subtract, multiply and divide.
- Handles divide by zero gracefully.
- Menu-driven program for user input.
- Clean function separation for modularity.

**RUN:**
```bash
python calculator_function.py
```

### 2. [Unit Converter App](unit_converter.py)
Converts unitd(km <-> miles, Celcius <-> fahrenheit).

**Features:**
- Functions for each conversion type.
- User-friendly menu-based choice system.
- Handles both distance and temperature conversions.
- Easy to extend with more conversions.

**RUN:**
```bash
python unit_converter.py
```

### 3. [Factorial Finder](factorial_finder.py)
Finds factorial of a number using recursion.

**Features:**
- Demonstrates recursive function calls.
- Works for both 0 and positive integers.
- Easy to extend for iterative version as well.

**RUN:**
```bash
python factorial_finder.py
```

### 4. [Palindrome Checker](palindrome_checker.py)
Checks if a word is a palindrome.

**Features:**
- Uses slicing([::-1]) to reverse a string.
- Case-sensitive palindrom check.
- Simple function returning True/False.

**RUN:**
```bash
python palindrome_checker.py
```

### 5. [Prime Number Checker](prime_number_checker.py)
Determines if a number is prime.

**Features:**
- Efficient check using square root optimization.
- Function returns True for primes and False otherwise.
- Handles egde cases (0, 1, negative numbers)

**RUN:**
```bash
python prime_number_checker.py
```

### 6. [Word Counter](word_counter.py)
Counts number of words in a sentence.

**Features:**
- Uses string.split() mehod.
- Simple and reusable function.
- Works for any sentence input.

**RUN:**
```bash
python word_counter.py
```

### 7. [Fibonacci Sequence Generator](fibonacci_sequence_generator.py)
Generates the first n numbers of the Fibonacci sequence.

**Features:**
- Iterative function implementation.
- Efficient without recursion (avoid stack overflow)
- Prints numbers in sequence format.

**RUN:**
```bash
python fibonacci_sequence_generator.py
```

### 8. [Grading System](grading_system.py)
Returns a grade based on marks.

**Features:**
- Uses conditional statements inside a function.
- Supports multiple grade ranges (A, B, C, Fail)
- Easy to customize grading scale.

**RUN:**
```bash
python grading_system.py
```

### 9. [Lambda Sorter](lambda_sorter.py)

**Features:**
- Sort dictionary items by name or price.

**RUN:**
```bash
python lambda_sorter.py
```

### 10. [Lambda Map filter](lambda_map_filter.py)

**Features:**
- Ask user to enter integers
- provide square of even integers.

**RUN:**
```bash
python lambda_map_filter.py
```

### 11. [Countdown Generator](generator_countdown)

**Features:**
- Uses yield to generate values one by one (like a lazy iterator).
- Implements a countdown timer from n down to 1.
- Demonstrates how generators pause and resume execution.
- Very memory-efficient since it does not store all numbers at once.

**RUN:**
```bash
python generator_countdown.py
```

### 12. [Gloabal Variables Controller](globals_toggle.py)

**Features:**
- Shows how to use the globals() functions to dynamically modify global variables inside functions.
- toggle_debug() switches DEBUG variable between True and False.
- set_theme() updates the THEME variable globally.
- Demonstrates the difference between local scope and global scope.
- Useful for configuration toggles in larger projects.

**RUN:**
```bash
python globals_toggle.py
```