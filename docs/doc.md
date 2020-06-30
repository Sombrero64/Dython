# Dython's Documentation
Dython is a free open-source Python library/module created by Daniel Lawson that contains pently of useful features when making a Python project.
Download Dython: ([ZIP](https://github.com/Sombrero64/Dython/zipball/master)/[TAR](https://github.com/Sombrero64/Dython/tarball/master))

## Functions

- `itemsMerge()`: returns a number when adding/subtracting all items in a list (_first_).

  ```py
  print(itemsMerge([42, 5, -2]))
  ```
  ```
  45.0
  ```

- `itemsMulty()`: returns the product of all items in a list (_first_).

  ```py
  print(itemsMulty([25, 4, 4]))
  ```
  ```
  400.0
  ```

- `rangeLimit()`: sets a limit of the _first_'s range. If higher than the maximum (_secound_), it returns the _secound_'s value; and vice versa.

  ```py
  print(rangeLimit(1, 0, 10))
  print(rangeLimit(5, 0, 10))
  print(rangeLimit(12, 0, 10))
  print(rangeLimit(-5, 0, 10))
  print(rangeLimit(3, 0, 10))
  ```
  ```
  1
  5
  10
  0
  3
  ```

- `feturn()`: returns either _secound_ or _third_ depending on the Boolean of _first_. If true, then _secound_. If false, then _third_.

  ```py
  print(feturn(False, 'Yes', 'No'))
  print(feturn(True, 'Yes', 'No'))
  ```
  ```
  No
  Yes
  ```

- `listInit()`: returns a number regrading the first instance of an item in a list (_first_) that matches _secound_. Returns _**None**_ if there was no items that matched _secound_.

  ```py
  print(listInit([0, 2, 1], 0))
  print(listInit([0, 2, 1], 2))
  print(listInit([0, 2, 1], 1))
  ```
  ```
  0
  1
  2
  ```

- `listInits()`: returns a list of numbers regrading instances of items that matches _secound_ in _first_.

  ```py
  numbers = [0, 1, 0, 2, 0, 2, 0, 4, 4, 0]

  print(listInits(numbers, 0))
  print(listInits(numbers, 2))
  print(listInits(numbers, 4))
  ```
  ```
  [0, 2, 4, 6, 9]
  [3, 5]
  [7, 8]
  ```

- `filterList()`: returns a copy of list of _first_ without items that matches _secound_.
  
  ```py
  numbers = [0, 1, 0, 0, 2, 0, 3, 4, 0, 5]
  print(filterList(numbers, 0))
  ```
  ```
  [1, 2, 3, 4, 5]
  ```

- `menu()`: allows you to provide a mutlichoice input into a console for the user to pick from.

### Local Variables
