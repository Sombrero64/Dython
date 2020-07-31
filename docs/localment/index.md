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

- [`define()`](https://sombrero64.github.io/PythonSharp/docs/localment/create)
- [`set()` & `change()`](https://sombrero64.github.io/PythonSharp/docs/localment/change)
- [`rename()`](https://sombrero64.github.io/PythonSharp/docs/localment/rename)
- [`get()`](https://sombrero64.github.io/PythonSharp/docs/localment/get)
- [`find()`](https://sombrero64.github.io/PythonSharp/docs/localment/find)
- [`remove()` & `wipe()`](https://sombrero64.github.io/PythonSharp/docs/localment/remove)
- [`all()`](https://sombrero64.github.io/PythonSharp/docs/localment/all)
