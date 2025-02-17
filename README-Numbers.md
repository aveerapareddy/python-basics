# Python Math Functions

Python provides a variety of built-in mathematical functions for performing arithmetic operations, rounding, power
calculations, logarithms, and more. Below is a comprehensive list of commonly used math functions with examples.

## Table of Contents

- [Basic Arithmetic Operations](#basic-arithmetic-operations)
- [Rounding & Absolute Value](#rounding--absolute-value)
- [Exponents & Logarithms](#exponents--logarithms)
- [Trigonometric Functions](#trigonometric-functions)
- [Min, Max & Sum](#min-max--sum)
- [Random Number Generation](#random-number-generation)
- [Mathematical Constants](#mathematical-constants)

---

## Basic Arithmetic Operations

```python
x = 10
y = 3

print(x + y)  # Addition → 13
print(x - y)  # Subtraction → 7
print(x * y)  # Multiplication → 30
print(x / y)  # Division → 3.3333...
print(x // y)  # Floor Division → 3
print(x % y)  # Modulus → 1
print(x ** y)  # Exponentiation → 1000
```

---

## Rounding & Absolute Value

| Function      | Description                             | Example                      |
|---------------|-----------------------------------------|------------------------------|
| `round(x, n)` | Rounds `x` to `n` decimal places        | `round(3.14159, 2)` → `3.14` |
| `abs(x)`      | Returns the absolute value of `x`       | `abs(-7)` → `7`              |
| `pow(x, y)`   | Computes `x` raised to the power of `y` | `pow(2, 3)` → `8`            |

---

## Exponents & Logarithms

| Function        | Description                          | Example                      |
|-----------------|--------------------------------------|------------------------------|
| `math.exp(x)`   | Returns `e^x`                        | `math.exp(1)` → `2.7182...`  |
| `math.log(x)`   | Returns the natural logarithm of `x` | `math.log(10)` → `2.3025...` |
| `math.log10(x)` | Returns the base-10 logarithm of `x` | `math.log10(100)` → `2.0`    |
| `math.sqrt(x)`  | Returns the square root of `x`       | `math.sqrt(25)` → `5.0`      |

```python
import math

print(math.exp(1))  # 2.718281828459045
print(math.log(10))  # 2.302585092994046
print(math.log10(100))  # 2.0
print(math.sqrt(25))  # 5.0
```

---

## Trigonometric Functions

| Function          | Description                             | Example                           |
|-------------------|-----------------------------------------|-----------------------------------|
| `math.sin(x)`     | Returns the sine of `x` (in radians)    | `math.sin(math.pi/2)` → `1.0`     |
| `math.cos(x)`     | Returns the cosine of `x` (in radians)  | `math.cos(math.pi)` → `-1.0`      |
| `math.tan(x)`     | Returns the tangent of `x` (in radians) | `math.tan(math.pi/4)` → `1.0`     |
| `math.degrees(x)` | Converts radians to degrees             | `math.degrees(math.pi)` → `180.0` |
| `math.radians(x)` | Converts degrees to radians             | `math.radians(180)` → `3.1415...` |

```python
import math

print(math.sin(math.pi / 2))  # 1.0
print(math.cos(math.pi))  # -1.0
print(math.tan(math.pi / 4))  # 1.0
print(math.degrees(math.pi))  # 180.0
print(math.radians(180))  # 3.141592653589793
```

---

## Min, Max & Sum

| Function        | Description                   | Example                    |
|-----------------|-------------------------------|----------------------------|
| `min(iterable)` | Returns the smallest value    | `min([3, 7, 1, 9])` → `1`  |
| `max(iterable)` | Returns the largest value     | `max([3, 7, 1, 9])` → `9`  |
| `sum(iterable)` | Returns the sum of all values | `sum([3, 7, 1, 9])` → `20` |

```python
print(min(3, 7, 1, 9))  # 1
print(max(3, 7, 1, 9))  # 9
print(sum([3, 7, 1, 9]))  # 20
```

---

## Random Number Generation

Python’s `random` module provides functions to generate random numbers.

```python
import random

print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.random())  # Random float between 0 and 1
print(random.uniform(1, 10))  # Random float between 1 and 10
print(random.choice(["red", "blue", "green"]))  # Random choice from a list
```

| Function               | Description                                  | Example                          |
|------------------------|----------------------------------------------|----------------------------------|
| `random.randint(a, b)` | Returns a random integer between `a` and `b` | `random.randint(1, 10)`          |
| `random.random()`      | Returns a random float between `0` and `1`   | `random.random()`                |
| `random.uniform(a, b)` | Returns a random float between `a` and `b`   | `random.uniform(1, 10)`          |
| `random.choice(seq)`   | Returns a random element from a sequence     | `random.choice(["a", "b", "c"])` |

---

## Mathematical Constants

Python's `math` module provides several useful mathematical constants.

| Constant   | Description         | Example             |
|------------|---------------------|---------------------|
| `math.pi`  | The value of π      | `3.141592653589793` |
| `math.e`   | Euler’s number (e)  | `2.718281828459045` |
| `math.tau` | The value of τ (2π) | `6.283185307179586` |
| `math.inf` | Positive infinity   | `math.inf`          |
| `math.nan` | Not a number (NaN)  | `math.nan`          |

```python
import math

print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
print(math.tau)  # 6.283185307179586
print(math.inf)  # inf
print(math.nan)  # nan
```

---

## Contributing

If you find any errors or have suggestions for improvements, feel free to create a pull request!

## License

This project is licensed under the MIT License.

