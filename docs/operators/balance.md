The `balance()` function checks all items' Boolean and counts up for each **true** ones. It returns **true** if the counter is around ___2___, ___3___ or bewteen of both.

For example, this returns **true** if 0-1 Booleans are **true**.

```py
print(balance([False, False, False], 0, 1))
print(balance([True, False, False], 0, 1))
print(balance([True, True, False], 0, 1))
print(balance([True, True, True], 0, 1))
```

```
True
True
False
False
```
