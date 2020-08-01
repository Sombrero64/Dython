An instance is an object that uses the `Instance()` class, which can carries a name, a class, properties, children, and its own variables.

```py
from PythonSHARP import *

playerInfoStuff = [
    Instance('Health', 'IntStore', [['Value', 0, 0]]),
    Instance('Level', 'IntStore', [['Value', 1, 0]]),
    Instance('XP', 'FloatStore', [['Value', 0.0, 0.0]]),
    Instance('XP Max', 'FloatStore', [['Value', 10.0, 0.0]]),
    Instance('Health', 'IntStore', [['Value', 100, 0]]),
    Instance('Name', 'StringStore', [['Name', '', '']]),
    Instance('Character', 'ObjectStore', [['Value', None, None]])
    ]

objects = Instance('ObjectStorage', 'service', [])

objects.newChild(Instance('PlayerInfo', 'folder', []))
playerInfo = objects.findSpecificChild('PlayerInfo', 'folder')

for s in playerInfoStuff: playerInfo.newChild(s)
```

___1___ is name; ___2___ is class; ___3___ is properties.

To create a master instance, assign it to a variable.

```py
objects = Instance('ObjectStorage', 'service', [])
```

[Functions for the Properties]()

[Functions for managing Children]()

[Functions for finding Children]()

[Functions for finding Pairs]()

[Instance Variables]()
