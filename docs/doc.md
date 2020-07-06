# Documentation
Python# (Python Sharp) is a free open-source Python module created by Daniel Lawson that allows the convenient creation of objects, with plenty of useful features when making a Python project. Download Python#: ([ZIP](https://github.com/Sombrero64/Python-/zipball/master)/[TAR](https://github.com/Sombrero64/Python-/tarball/master))

# Table of Contents

- [Functions](#functions)

- [Local Variables](#local-variables)

- [Objects](#objects)

  - Info Functions

  - Children Functions

  - Children Locator Functions

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

- `listInit()`: returns a number regrading the first instance of an item in a list (_first_) that matches _secound_. Returns ***None*** if there was no items that matched _secound_.

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

- `menu()`: allows you to provide a mutlichoice input into a console for the user to pick from. Provide a list of options with a list (_secound_).
  
  ```py
  answer = menu(None, ['first', 'secound', 'third'], False)
  ```
  ```
  0: first
  1: secound
  2: third
  └> 
  ```
  
  If you want to provide a caption for your input, provide a string for _first_. Otherwise not, provide an empty string or ***None***.
  
  ```py
  answer = menu('anwser below', ['first', 'secound', 'third'], False)
  ```
  ```
  anwser below
  0: first
  1: secound
  2: third
  └> 
  ```
  
  To allow an empty response, set _third_ to true. If the user provided as such, it would return ***None***.

### Local Variables
**Local Variables** allows you to make variables for temporary use. After their main use is over, they can be removed later on. These variables can also be renamed as well. Let's assign `localment()` to **`teams`** to make it a home for variables regrading teams.

```py
teams = localment()
```

  - `new()` & `define()`: creates a local variable named after _first_. The *`new()`* function would set the value to ***None***. The other one, *`define()`*, whould set it to _secound_.

  ```py
  teams.define('red', 0)
  teams.define('blue', 0)
  teams.define('yellow', 0)
  teams.define('green', 0)
  ```

  - `set()`: changes the value of a local variable (_first_) to _secound_.

  ```py
  teams.set('red', 8)
  teams.set('blue', 10)
  teams.set('yellow', 2)
  teams.set('green', 5)
  ```

  - `get()`: returns the value of a local variable (_first_). Returns ***None*** if variable doesn't exist.

  ```py
  print(teams.get('red'))
  print(teams.get('blue'))
  print(teams.get('yellow'))
  print(teams.get('green'))
  print(teams.get('purple'))
  ```
  ```
  8
  10
  2
  5
  None
  ```
  
  - `find()`: returns the name of a variable in their housing variable based on index (_first_). Returns ***None*** if variable doesn't exist.
  
  ```py
  print(teams.find(0)) # red
  print(teams.find(1)) # blue
  print(teams.find(2)) # yellow
  print(teams.find(3)) # green
  print(teams.find(4)) # purple (doesn't exist)
  ```
  ```
  red
  blue
  yellow
  green
  None
  ```

  - `rename()`: renames a local variable (_first_) to _secound_.
  
  ```py
  teams.rename('red', 'Red Team')
  teams.rename('blue', 'Blue Team')
  teams.rename('yellow', 'Yellow Team')
  teams.rename('green', 'Green Team')
  ```
  
  - `remove()`: remove a local varaible (_first_).
  
  ```py
  teams.remove('yellow')

  print(teams.get('red'))
  print(teams.get('blue'))
  print(teams.get('yellow'))
  print(teams.get('green'))
  ```
  ```
  8
  10
  None
  5
  ```
  
  - `items()`: returns the list of all local variables in a variable.
  
  ```py
  print(teams.items())
  ```
  
  ```
  [['red', 8], ['blue', 10], ['green', 5]]
  ```

### Objects
**Objects** is a feature that allows you to create instances that contains names (subjects), classes, and properties (props for short). Using the `Instance()` function, you can create objects with this. Let's assign this to **`workspace`** to make a master object (service).

```py
workspaceProps = [prop('Project Name', 'Project')]
workspace = Instance('Workspace', 'Workspace', workspaceProps)
```

#### Info Functions
These functions would gather and modify infomation about an object; their subject, class, and props, and return them.

- `gitSub()`, `gitClass()`, & `gitProps()`: returns an object's subject, class, or props.

  ```py
  print(workspace.gitSub())
  print(workspace.gitClass())
  print(workspace.gitProps())
  ```
  ```
  Workspace
  Workspace
  [['Project Name', 'Project', 'Project']]
  ```
  
- `sitSub()`, `sitClass()`, & `sitProps()`: sets an object's subject, class, or props to _first_.

  ```py
  workspace.sitSub('Workspace?')
  workspace.sitClass('workSpace')
  workspace.sitProps([workspaceProps[0], prop('Oragnic?', False)])

  print(workspace.gitSub())
  print(workspace.gitClass())
  print(workspace.gitProps())
  ```
  ```
  Workspace?
  workSpace
  [['Project Name', 'Project', 'Project'], ['Oragnic?', False, False]]
  ```
  
- `findProp()`: returns a list of a prop (_first_)'s infomation: name, current value, and default value.

  ```py
  print(workspace.findProp('Project Name'))
  ```
  ```
  ['Project Name', 'Project', 'Project']
  ```
  
- `gitProp()`: returns the current value of a prop (_first_).

  ```py
  print(workspace.gitProp('Project Name'))
  ```
  ```
  Project
  ```
  
- `sitProp()`: sets the value of a prop (_first_) to _secound_. Use `ritProp()` to set the prop to the default value.

  ```py
  workspace.sitProp('Project Name', 'Cool Game')
  print(workspace.gitProp('Project Name'))
  ```
  ```
  Cool Game
  ```
  
#### Children (Nested Objects) Functions

- `newChild()`: adds a new object inside an instance.

  ```py
  workspace.newChild(Instance('Score', 'IntStore', [prop('Value', 0)]))
  ```
  
- `clearChild()`: removes a child from an instance based on _first_'s object.

  ```py
  child = workspace.findChild('Score')
  workspace.clearChild(child)
  ```

- `clearChildren()`: removes children from an instance based on _first_'s object.

  ```py
  workspace.clearChildren()
  ```

- `clearAllChildren()`: removes all children from an instance.

  ```py
  workspace.clearAllChildren()
  ```
  
- `replaceChild()`: replaces a child with a new object (_secound_) inside an instance.

  ```py
  child = workspace.findChild('Score')
  newObj = Instance('Score', 'FloatStore', [prop('Value', 0.0)])
  workspace.replaceChild(child, newObj)
  ```
  
- `replaceChildren()`: replaces all matching children with a new object (_secound_) inside an instance.

  ```py
  workspace.replaceChildren(children, newObj)
  ```

- `parent()`: returns the object's parent as an object, allowing you to get its subject, class, props, and even children. You can also moddify them and manage their children.

  ```py
  workspace.newChild(Instance('Some Object', 'object', []))
  someObject = workspace.findChild('Some Object')

  print(someObject.gitSub())
  print(someObject.parent().gitSub())
  ```
  ```
  Some Object
  Workspace
  ```
  
  If necessary, you can use the `assignParentAs()` function to change an object's parent.
  
  ```py
  someObject.assignParentAs(objectStore)
  ```
  
#### Children Locator Functions

- `getChildren()`: returns the list of all children from an instance.

  ```py
  print(workspace.getChildren())
  ```
  
- `findChild()`: finds the first child named as such (_first_) from an instance. Returns ***None*** if no child exist named as such.

  ```py
  print(workspace.findChild('Score').gitClass())
  ```
  ```
  IntStore
  ```
  
- `findFirstChild()`: finds the first child based on finding its class (_first_). Returns ***None*** if no child exist classed as such.

  ```py
  print(workspace.findFirstChild('IntStore').gitSub())
  ```
  ```
  Score
  ```
  
- `locateForChild()`: finds the first child named (_first_) and classed (_secound_) as such. Returns ***None*** if no child exist named/classed as such.

  ```py
  print(workspace.locateForChild('Score', 'IntStore').gitSub())
  ```
  ```
  Score
  ```

- `findFirstChildren()`: returns a list of objects that are classed (_first_) as such.

  ```py
  workspace.findFirstChildren('IntStore')
  ```
  
- `findRelatedChildren()`: returns a list of objects named as such (_first_) from an instance.

  ```py
  workspace.findRelatedChildren('Score')
  ```
  
- `locateRelatedChildren()`: returns a list of objects named (_first_) and classed (_secound_) as such.

  ```py
  workspace.locateRelatedChildren('Score', 'IntScore')
  ```
