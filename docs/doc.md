# Dython Documentation
**Dython** is an open-source Python library created by [Daniel Lawson](https://github.com/Sombrero64), that includes functions that saves room and time.

### Table of Contents

[Instailing Dython](#instailing-dython)

[Oprations](#oprations)

## Instailing Dython
1. Download Dython, and extract it. ([ZIP](https://github.com/Sombrero64/Dython/zipball/master)/[TAR](https://github.com/Sombrero64/Dython/tarball/master))
2. Take the Dython's script, **Dython.py**, and insert in your project's folder.
3. Edit scripts that requires Dython's functions, and add an `import` command.

```py
from Dython import *
```

## Oprations
The oprations (`math`) class contains functions regrading oprating values and objects. There are currently 8 functions under this class.

- `expon()`: returns the expontent of a number (first argument) to the secound argument.

  ```py
  print(math.expon(4, 2))
  print(math.expon(4, 3))
  ```
  ```
  16.0
  64.0
  ```
- `itemsAdd()`, `itemsSub()`, `itemsMulti()`, & `itemsDivd()`: returns the sum, difference, product, or quotient of all items in a list (argument).
  ```py
  print(math.itemsAdd([1, 2, 3]))
  print(math.itemsSub([5, 3, 0.5]))
  print(math.itemsMulti([5, 5, 4]))
  print(math.itemsDivd([100, 4]))
  ```
  ```
  6.0
  1.5
  100.0
  25.0
  ```
- `joinStrs()`: returns a joined string of all items in a list (argument).
  ```py
  name = "Davis"
  print(math.joinStrs(["Hello, ", name, "!"]))
  ```
  ```
  Hello, Davis!
  ```
- `itemCount()`: returns the amount of items in a list (first argument) that matches the secound argument.
  ```py
  print(math.itemCount(["a", "a", "b"], "a"))
  print(math.itemCount(["a", "a", "b"], "b"))
  print(math.itemCount(["a", "a", "b"], "c"))
  ```
  ```
  2
  1
  0
  ```
- `rangeLimit()`: sets a limit to a number's (first) range with a minimum and maximum (secound and third argument).
  ```py
  print(math.rangeLimit(5, 0, 10))
  print(math.rangeLimit(11, 0, 10))
  print(math.rangeLimit(-3, 0, 10))
  print(math.rangeLimit(7, 0, 10))
  ```
  ```
  5
  10
  0
  7
  ```
