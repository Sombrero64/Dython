# Python#
__Python#__ is a free open-source Python module that allows the braching, convenient creation of objects.

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

Copyright (©) 2020 Daniel Lawson
