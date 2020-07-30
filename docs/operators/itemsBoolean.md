The there functions, `orItems()`, `andItems()` & `xorItems()` prefroms an _or_, _and_ or _xor_ operation on all items in a list, then returns a Boolean depending on the result.

```py
print(orItems([False, False]))
print(orItems([True, False]))
print(orItems([True, True]))
print('')

print(andItems([False, False]))
print(andItems([True, False]))
print(andItems([True, True]))
print('')

print(xorItems([False, False]))
print(xorItems([True, False]))
print(xorItems([True, True]))
```

```
False
True
True

False
False
True

False
True
False
```
