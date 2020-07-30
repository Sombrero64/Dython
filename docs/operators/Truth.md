The `truth()` function takes a string/number and convert it into **true**, **false**, or **none** depending its value. It returns ___1___ if it doesn't match any keywords.

```py
# take string
print(truth('yes'))
print(truth('no'))
print(truth('nothing'))
print('')

# take number
print(truth(1))
print(truth(0))
print('')

# return 1
print(truth(42))
print(truth('yo dog'))
```

```
True
False
None

True
False

42
yo dog
```

### Keywords
It returns **true** if ___1___ is "true", "yes", "correct", "on" or one.

Returns **false** if ___1___ is "false", "no", "incorrect", "off" or zero.

Returns **none** if ___1___ is "none", "nothing", "nil", "null", or an empty string.
