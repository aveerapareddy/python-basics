# Python List Functions

Python lists are a powerful data structure that allows dynamic storage, manipulation, and traversal of elements. Below
is a comprehensive guide to commonly used list functions with examples.

## Table of Contents

- [Creating Lists](#creating-lists)
- [Accessing Elements](#accessing-elements)
- [Adding Elements](#adding-elements)
- [Removing Elements](#removing-elements)
- [Sorting & Reversing](#sorting--reversing)
- [List Operations](#list-operations)
- [List Comprehensions](#list-comprehensions)
- [Copying Lists](#copying-lists)
- [Other Useful List Functions](#other-useful-list-functions)

---

## Creating Lists

```python
# Creating a list
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "Hello", 3.5, True]
empty_list = []
```

---

## Accessing Elements

```python
my_list = [10, 20, 30, 40, 50]
print(my_list[0])  # 10 (First element)
print(my_list[-1])  # 50 (Last element)
print(my_list[1:4])  # [20, 30, 40] (Slicing)
```

---

## Adding Elements

| Function           | Description                                                  | Example                     |
|--------------------|--------------------------------------------------------------|-----------------------------|
| `append(x)`        | Adds an element `x` to the end of the list                   | `my_list.append(6)`         |
| `insert(i, x)`     | Inserts `x` at index `i`                                     | `my_list.insert(2, 99)`     |
| `extend(iterable)` | Extends the list by appending elements from another iterable | `my_list.extend([7, 8, 9])` |

```python
my_list = [1, 2, 3]
my_list.append(4)  # [1, 2, 3, 4]
my_list.insert(1, 99)  # [1, 99, 2, 3, 4]
my_list.extend([5, 6, 7])  # [1, 99, 2, 3, 4, 5, 6, 7]
```

---

## Removing Elements

| Function    | Description                                                 | Example             |
|-------------|-------------------------------------------------------------|---------------------|
| `remove(x)` | Removes the first occurrence of `x`                         | `my_list.remove(3)` |
| `pop(i)`    | Removes and returns the element at index `i` (default last) | `my_list.pop(2)`    |
| `clear()`   | Removes all elements from the list                          | `my_list.clear()`   |

```python
my_list = [10, 20, 30, 40]
my_list.remove(20)  # [10, 30, 40]
print(my_list.pop(1))  # 30 (Removed element)
my_list.clear()  # []
```

---

## Sorting & Reversing

| Function             | Description                        | Example                      |
|----------------------|------------------------------------|------------------------------|
| `sort()`             | Sorts the list in ascending order  | `my_list.sort()`             |
| `sort(reverse=True)` | Sorts the list in descending order | `my_list.sort(reverse=True)` |
| `reverse()`          | Reverses the list in place         | `my_list.reverse()`          |

```python
nums = [5, 2, 9, 1]
nums.sort()  # [1, 2, 5, 9]
nums.sort(reverse=True)  # [9, 5, 2, 1]
nums.reverse()  # [1, 2, 5, 9]
```

---

## List Operations

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]
duplicated = list1 * 2  # [1, 2, 3, 1, 2, 3]
```

---

## List Comprehensions

```python
# Create a list of squares
squares = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

---

## Copying Lists

| Method   | Description                             | Example                     |
|----------|-----------------------------------------|-----------------------------|
| `copy()` | Returns a shallow copy of the list      | `new_list = my_list.copy()` |
| `list()` | Creates a new list from an existing one | `new_list = list(my_list)`  |
| `[:]`    | Slices the entire list to create a copy | `new_list = my_list[:]`     |

```python
my_list = [1, 2, 3]
copy1 = my_list.copy()
copy2 = list(my_list)
copy3 = my_list[:]
```

---

## Other Useful List Functions

| Function        | Description                                      | Example                        |
|-----------------|--------------------------------------------------|--------------------------------|
| `len(list)`     | Returns the number of elements in the list       | `len(my_list)`                 |
| `sum(list)`     | Returns the sum of all elements in the list      | `sum([1, 2, 3])` → `6`         |
| `min(list)`     | Returns the smallest element in the list         | `min([3, 1, 4])` → `1`         |
| `max(list)`     | Returns the largest element in the list          | `max([3, 1, 4])` → `4`         |
| `list.index(x)` | Returns the index of the first occurrence of `x` | `[10, 20, 30].index(20)` → `1` |
| `list.count(x)` | Returns the count of occurrences of `x`          | `[1, 2, 2, 3].count(2)` → `2`  |

```python
numbers = [10, 20, 30, 20]
print(len(numbers))  # 4
print(sum(numbers))  # 80
print(min(numbers))  # 10
print(max(numbers))  # 30
print(numbers.index(20))  # 1
print(numbers.count(20))  # 2
```

---

## Contributing

If you find any errors or have suggestions for improvements, feel free to create a pull request!

## License

This project is licensed under the MIT License.

