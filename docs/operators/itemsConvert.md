The four functions, `itemsInt()`, `itemsFloat()`, `itemsStr()` & `itemsList()` converts all items in a list into an integer, float, string, or list.

```py
print(itemsInt([1, 2.0, '3', '4.2']))
print(itemsFloat([4.2, 5, '6', '7.3']))
print(itemsStr(['numbers', 'are', '8', 9.3, 10]))
print(itemsList(['11', '12.0', '13.5']))
```

```
[1, 2, 3, 4]
[4.2, 5.0, 6.0, 7.3]
['numbers', 'are', '8', '9.3', '10']
[['1', '1'], ['1', '2', '.', '0'], ['1', '3', '.', '5']]
```

There's also `shutItems()` which is simlar to `itemsList()` by converting them to lists, but it places it in an empty list instend converting as such.

```py
print(itemsList(['ab', 'cd', 'ef']))
print(shutItems(['ab', 'cd', 'ef']))
```

```
[['a', 'b'], ['c', 'd'], ['e', 'f']]
[['ab'], ['cd'], ['ef']]
```
