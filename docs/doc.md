# Documentation
__Python# (Python Sharp)__ is a free open-source Python module created by Daniel Lawson that allows the braching, convenient creation of objects.

Download Python#: ([ZIP](https://github.com/Sombrero64/Python-/zipball/master)/[TAR](https://github.com/Sombrero64/Python-/tarball/master))

```py
from PythonSHARP import *

playerInfoStuff = [
    Instance('Health', 'IntStore', [['Value', 0, 0]]),
    Instance('Level', 'IntStore', [['Value', 1, 0]]),
    Instance('XP', 'FloatStore', [['Value', 0.0, 0.0]]),
    Instance('XP Max', 'FloatStore', [['Value', 10.0, 0.0]]),
    Instance('Health', 'IntStore', [['Value', 100, 0]),
    Instance('Name', 'StringStore', [['Name', '', '']]),
    Instance('Character', 'ObjectStore', [['Value', None, None]])
    ]

objects = Instance('ObjectStorage', 'service', [])

objects.newChild(Instance('PlayerInfo', 'folder', []))
playerInfo = objects.findSpecificChild('PlayerInfo', 'folder')

for s in list(playerInfoStuff): playerInfo.newChild(s)
```

# Table of Contents

- [Functions](#functions)

- [Local Variables](#local-variables)

- [Instances](#instances)

  - Info Functions

  - Children Functions

  - Children Locator Functions
  
  - Instance Variables

## Functions

- `itemsAddty()`: returns the sum of all items in a list (_first_).

    ```py
    print(itemsAddty([42, 5, -2]))
    ```
    ```
    45.0
    ```
  
- `itemsSubty()`: returns the diffence of all items in a list (_first_).

    ```py
    print(itemsSubty([100, 50, 25, 5, -1]))
    ```
    ```
    21.0
    ```

- `itemsMulty()`: returns the product of all items in a list (_first_).

    ```py
    print(itemsMulty([25, 4, 4]))
    ```
    ```
    400.0
    ```
  
- `itemsDidty()`: returns the quotient of all items in a list (_first_).

    ```py
    print(itemsDidty([42, 7, 3]))
    ```
    ```
    2.0
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

- `findGreatest()`: returns the biggest item in a list (_first_).
    
    ```py
    print(findGreatest([0, 2, 4, 1, 3, 5.2, 5]))
    ```
    ```
    5.2
    ```
    
 - `findSmallest()`: returns the smallest item in a list (_first_).
    
    ```py
    print(findSmalest([0, 2, 4, 1, 3, 5.2, 5]))
    ```
    ```
    0
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
**Local Variables** allows you to make variables for temporary use. After their main use is over, they can be removed later on. These variables can also be renamed as well. Let's assign `Localment()` to **`teams`** to make it a home for variables regrading teams.

```py
teams = Localment()
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
  
  - `change()`: increases the value of an variable (_first_) by _secound_. Using `bange()` world decrease it.
  
  ```py
  teams.define('red', 0)
  teams.define('blue', 0)
  teams.define('yellow', 0)
  teams.define('green', 0)
  
  teams.change('red', 8)
  teams.change('blue', 10)
  teams.chnage('yellow', -2)
  teams.change('green', 5)
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
  
  - `variables()`: returns the list of all local variables in a variable.
  
  ```py
  print(teams.variables())
  ```
  
  ```
  [['red', 8], ['blue', 10], ['green', 5]]
  ```

### Instances
**Instances** is a feature that allows you to create branching objects that contains names (subjects), classes, and properties (props for short). Using the `Instance()` function, you can create objects with this. Let's assign this to **`workspace`** to make a master object (service).

```py
workspaceProps = [['Project Name', 'Project', 'untitled']]
workspace = Instance('Workspace', 'Workspace', workspaceProps)
```

#### Info Functions
These functions would gather and modify infomation about an object; their subject, class, and props, and return them.

- `Sub()`, `Class()`, & `Props()`: returns an object's subject, class, or props.

    ```py
    print(workspace.Sub())
    print(workspace.Class())
    print(workspace.Props())
    ```
    ```
    Workspace
    Workspace
    [['Project Name', 'Project', 'untitled']]
    ```
  
- `sitSub()`, `sitClass()`, & `sitProps()`: sets an object's subject, class, or props to _first_.

    ```py
    workspace.sitSub('Workspace?')
    workspace.sitClass('workSpace')
    workspace.sitProps([workspaceProps[0], ['Oragnic?', False, False]])

    print(workspace.Sub())
    print(workspace.Class())
    print(workspace.Props())
    ```
    ```
    Workspace?
    workSpace
    [['Project Name', 'Project', 'untitled'], ['Oragnic?', False, False]]
    ```
  
- `findProp()`: returns a list of a prop (_first_)'s infomation: name, current value, and default value.

    ```py
    print(workspace.findProp('Project Name'))
    ```
    ```
    ['Project Name', 'Project', 'untitled']
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
  
- `parent()`: returns the object's parent as an object, allowing you to get its subject, class, props, and even children. You can also moddify them and manage their children.

    ```py
    workspace.newChild(Instance('Some Object', 'object', []))
    someObject = workspace.findChild('Some Object')

    print(someObject.Sub())
    print(someObject.parent().Sub())
    ```
    ```
    Some Object
    Workspace
    ```
  
    If necessary, you can use the `assignParentAs()` function to change an object's parent.
  
    ```py
    someObject.assignParentAs(objectStore)
    ```
  
#### Children (Nested Objects) Functions

- `newChild()`: adds a new object inside an instance.

    ```py
    workspace.newChild(Instance('Score', 'IntStore', [['Value', 0, 0]]))
    ```
    
    You can also make clones of the instance easily with the `clone()` function.
  
- `clearChild()`: removes a child from an instance based on _first_'s object.

    ```py
    child = workspace.findChild('Score')
    workspace.clearChild(child)
    ```
    
    You can use `clear()` to remove the instance.

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
    newObj = Instance('Score', 'FloatStore', [['Value', 0.0, 0.0]])
    workspace.replaceChild(child, newObj)
    ```
  
- `replaceChildren()`: replaces all matching children with a new object (_secound_) inside an instance.

    ```py
    workspace.replaceChildren(children, newObj)
    ```
  
#### Children Locator Functions

- `getChildren()`: returns the list of all children from an instance.

  ```py
  print(workspace.getChildren())
  ```
  
- `getChildbyIndex()`: returns a children based on index.

  ```py
  workspace.newChild(Instance('Object1', 'object', []))
  workspace.newChild(Instance('Object2', 'object', []))
  workspace.newChild(Instance('Object3', 'object', []))
  
  print(workspace.getChildbyIndex(0).Sub())
  print(workspace.getChildbyIndex(1).Sub())
  print(workspace.getChildbyIndex(2).Sub())
  print(workspace.getChildbyIndex(3))
  ```
  ```
  Object1
  Object2
  Object3
  None
  ```
  
- `findChild()`: finds the first child named as such (_first_) from an instance. Returns ***None*** if no child exists named as such.

  ```py
  print(workspace.findChild('Score').Class())
  ```
  ```
  IntStore
  ```
  
- `findFirstChild()`: finds the first child based on finding its class (_first_). Returns ***None*** if no child exists classified as such.

  ```py
  print(workspace.findFirstChild('IntStore').Sub())
  ```
  ```
  Score
  ```
  
- `findSpecificChild()`: finds the first child named (_first_) and classified (_secound_) as such. Returns ***None*** if no child exists named/classified as such.

  ```py
  print(workspace.findSpecificChild('Score', 'IntStore').Sub())
  ```
  ```
  Score
  ```

- `findFirstChildren()`: returns a list of objects that are classified (_first_) as such.

  ```py
  workspace.findFirstChildren('IntStore')
  ```
  
- `findRelatedChildren()`: returns a list of objects named as such (_first_) from an instance.

  ```py
  workspace.findRelatedChildren('Score')
  ```
  
- `locateRelatedChildren()`: returns a list of objects named (_first_) and classified (_secound_) as such.

  ```py
  workspace.locateRelatedChildren('Score', 'IntScore')
  ```

- `waitForChild()`: waits for a child (_first_) in an instance for their existence \[subject]\. Delays the script until found.
  
  ```py
  workspace.waitForChild('Score')
  ```
  
- `waitForFirstChild()`: waits for a child (_first_) in an instance for their existence \[class]\. Delays the script until found.

  ```py
  workspace.waitForFirstChild('IntStore')
  ```
  
- `waitForSpecificChild()`: waits for a child (_first_ & _secound_) in an instance for their existence \[name & class]\. Delays the script until found.

  ```py
  workspace.waitForSpecificChild('Score', 'IntStore')
  ```

- `doesChildExist()`: returns a Boolean if it's true if the instance owns a child named as such.

  ```py
  print(workspace.doesChildExist('Score'))
  print(workspace.doesChildExist('HighScore'))
  ```
  ```
  True
  False
  ```
  
- `doesFirstChildExist()`: returns a Boolean if it's true if the instance owns a child classified as such.

  ```py
  print(workspace.doesFirstChildExits('IntStore'))
  print(workspace.doesFirstChildExits('StringStore'))
  ```
  ```
  True
  False
  ```

- `doesSpecificChildExist()`: returns a Boolean if it's true if the instance owns a child classified as such.

  ```py
  print(workspace.doesFirstChildExits('HighScore', 'IntStore'))
  print(workspace.doesFirstChildExits('Score', 'IntStore'))
  print(workspace.doesFirstChildExits('Name', 'StringStore'))
  ```
  ```
  False
  True
  False
  ```
  
- `findNamePairs()`: returns the first child in an instance that matches the name of another object. Returns ***None*** if no child exists named as such.

  ```py
  altScore = Instance('Score', 'NumberStore', [['Value', 0.0, 0.0]])
  print(workspace.findNamePairs(altScore).Sub(),
        workspace.findNamePairs(altScore).Class(),
        workspace.findNamePairs(altScore).Props())
  ```
  ```
  Score IntStore [['Value', 0, 0]]
  ```
  
  Using `getNamePairs()` would return a list of children that matches the name of the object.
  
- `findClassPairs()`: returns the first child in an instance that matches the class of another object. Returns ***None*** if no child exists classified as such.

  ```py
  highScore = Instance('HighScore', 'IntStore', [['Value', 0, 0]])
  print(workspace.findClassPairs(highScore).Sub(),
        workspace.findClassPairs(highScore).Class(),
        workspace.findClassPairs(highScore).Props())
  ```
  ```
  Score IntStore [['Value', 0, 0]]
  ```
  
  Using `getClassPairs()` would return a list of children that matches the clas of the object.

- `findPairs()`: returns the first child in an instance that matches both the name & class of another object. Returns ***None*** if no matching child exists.

  ```py
  outsider = Instance('Score', 'IntStore', [['Value', 0, 0]])
  print(workspace.findPairs(outsider).Sub(),
        workspace.findPairs(outsider).Class(),
        workspace.findPairs(outsider).Props())
  ```
  ```
  Score IntStore [['Value', 0, 0]]
  ```
  
  Using `getPairs()` would return a list of matching children.

#### Instance Variables
Instance Variables are variables stored instance an object.

- `NEW()`: creates a new variable named as _first_.

    ```py
    workspace.newChild(Instance('PlayerChar', 'humanoid', []))
    workspace.findChild('PlayerChar').NEW('direction', 90)
    ```

- `GET()`: returns the value of a variable. Returns ***None*** if the variable doesn't exist.

    ```py
    print(workspace.findChild('PlayerChar').GET('direction'))
    ```
    ```
    90
    ```
    
    The `INDEX()` function returns the name of a variable based on index.

- `SET()`: sets the value of a variable.

    ```py
    workspace.findChild('PlayerChar').SET('direction', 180)
    ```

- `DEL()`: removes a variable.

    ```py
    workspace.findChild('PlayerChar').DEL('direction')
    ```
