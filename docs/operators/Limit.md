The `limit()` function takes a number and returns it with a maximum and minimum. If the number is greater than its maximum, then it returns the max instend. Same thing goes with the minimum if the number is smaller than it.

```py
print(limit(5, 1, 10))
print(limit(7, 1, 10))
print(limit(-2, 1, 10))
print(limit(14, 1, 10))
print(limit(3, 1, 10))
```

```
5
7
1
10
3
```
