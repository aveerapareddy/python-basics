# Python Naming Conventions

Following proper naming conventions in Python improves **readability**, **maintainability**, and **consistency**. Below
is a structured guide based on **PEP 8 (Python's official style guide).**

---

## **1. General Naming Rules**

✅ Use **meaningful and descriptive names**  
✅ Use **lowercase letters with underscores (`snake_case`) for readability**  
✅ Avoid **single-letter names** (except loop variables like `i, j, k`)  
✅ Be **consistent** across your project

---

## **2. Variable Naming**

🔹 Use **snake_case** for variable names  
🔹 Use **descriptive names** instead of single-letter variables

```python
# Good
user_name = "Alice"
total_amount = 100.50

# Bad
usrNm = "Alice"
amt = 100.50
```

---

## **3. Constant Naming** (Global Variables)

🔹 Use **UPPERCASE** with underscores  
🔹 Constants should be **declared at the top** of the module

```python
# Good
PI = 3.14159
MAX_CONNECTIONS = 100

# Bad
pi_value = 3.14159
maxConn = 100
```

---

## **4. Function Naming**

🔹 Use **snake_case** for function names  
🔹 Function names should be **verbs** describing their action

```python
# Good
def calculate_total():
    pass


def get_user_info():
    pass


# Bad
def CalculateTotal():
    pass


def getUserInfo():
    pass
```

---

## **5. Class Naming**

🔹 Use **PascalCase** (Each word capitalized, no underscores)  
🔹 Class names should be **nouns**

```python
# Good
class UserProfile:
    pass


class OrderManager:
    pass


# Bad
class user_profile:
    pass


class order_manager:
    pass
```

---

## **6. Method Naming (Inside Classes)**

🔹 Use **snake_case** (like functions)  
🔹 Private methods should start with **a single underscore** (`_`)

```python
class User:
    def get_full_name(self):
        pass  # Public method

    def _validate_age(self):
        pass  # Private method
```

---

## **7. Naming for Modules & Packages**

🔹 Use **snake_case** for module (file) names  
🔹 Use **lowercase without underscores** for package names

```python
# Module (Python file)
# Good
user_auth.py
order_processing.py

# Bad
UserAuth.py
OrderProcessing.py

# Package (Folder containing modules)
# Good
ecommerce
database_utils

# Bad
EcommerceApp
Database_Utils
```

---

## **8. Naming for Exceptions**

🔹 Use **PascalCase** and **end with `Error`**

```python
# Good
class InvalidUserError(Exception):
    pass


class ConnectionTimeoutError(Exception):
    pass


# Bad
class invalidusererror(Exception):
    pass


class connectiontimeout(Exception):
    pass
```

---

## **9. Naming for Boolean Variables & Functions**

🔹 Use **`is_` or `has_` prefix** for boolean variables/functions

```python
# Good
is_logged_in = True
has_permission = False


def is_valid_user():
    return True


# Bad
loggedIn = True
permission = False
```

---

## **10. Naming for Private & Protected Members**

🔹 Use **a single underscore (`_`)** for protected variables/methods  
🔹 Use **double underscore (`__`)** for private variables/methods (name-mangling applied)

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected variable
        self.__account_number = "12345XYZ"  # Private variable

    def _calculate_interest(self):  # Protected method
        pass

    def __verify_account(self):  # Private method
        pass
```

---

## **11. Naming for Test Functions**

🔹 Use `test_` as a prefix to indicate test functions

```python
def test_user_login():
    pass


def test_calculate_discount():
    pass
```

---

## **12. Naming Conventions for Database Fields**

🔹 Use **snake_case** for table and column names

```sql
-- Good
CREATE TABLE user_accounts (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    created_at TIMESTAMP
);

-- Bad
CREATE TABLE UserAccounts (
    UserId SERIAL PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    CreatedAt TIMESTAMP
);
```

---

## **13. Naming for Enums**

🔹 Use **PascalCase** for enum names  
🔹 Use **UPPERCASE** for enum members

```python
from enum import Enum


class UserRole(Enum):
    ADMIN = 1
    USER = 2
    GUEST = 3
```

---

## **14. Naming for Docstrings & Comments**

🔹 Use **triple quotes (`"""`)** for docstrings  
🔹 Use `#` for single-line comments

```python
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

# This is a single-line comment
```

---

## **Quick Summary**

| Element             | Convention        | Example                   |
|---------------------|-------------------|---------------------------|
| **Variables**       | `snake_case`      | `user_name = "Alice"`     |
| **Constants**       | `UPPER_CASE`      | `MAX_USERS = 100`         |
| **Functions**       | `snake_case`      | `def get_user_info():`    |
| **Classes**         | `PascalCase`      | `class UserProfile:`      |
| **Methods**         | `snake_case`      | `def update_profile():`   |
| **Modules**         | `snake_case.py`   | `user_auth.py`            |
| **Packages**        | `lowercase`       | `ecommerce`               |
| **Boolean Vars**    | `is_/has_`        | `is_active = True`        |
| **Private Members** | `_protected`      | `self._balance`           |
| **Private Members** | `__private`       | `self.__account_number`   |
| **Exceptions**      | `PascalCaseError` | `class InvalidUserError:` |
| **Test Functions**  | `test_` prefix    | `test_login()`            |

---

## **Conclusion**

Following Python’s **PEP 8 naming conventions** ensures your code is **clean, professional, and maintainable**. 🚀

Feel free to contribute or suggest improvements! 😊

