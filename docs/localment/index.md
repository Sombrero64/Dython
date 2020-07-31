The Local Variables feature allows to you to store simlar variables into a variable assigned with the `Localment()` object. 

For example, you can try assign a variable with the said class regrading the scores of teams.

```py
scores = Localment()

scores.define('Red', 0)
scores.define('Blue', 0)
scores.define('Green', 0)
scores.define('Yellow', 0)

scores.change('Red', 3)
scores.change('Blue', 4)
scores.change('Green', 2)
scores.change('Yellow', 1)
```

- `new()` & `define()`
- `set()` & `change()`
- `rename()`
- `get()`
- `find()`
- `remove()` & `wipe()`
- `all()`
