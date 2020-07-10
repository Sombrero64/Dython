!["Python#'s logo."](https://raw.githubusercontent.com/Sombrero64/PythonSharp/master/docs/logo/PythonSharpLogo.png)

**Python#** is a free open-source Python module that allows the braching, convenient creation of objects.

```py
from PythonSHARP import *

playerInfoStuff = [
    Instance('Health', 'IntStore', [prop('Value', 0)]),
    Instance('Level', 'IntStore', [prop('Value', 1)]),
    Instance('XP', 'FloatStore', [prop('Value', 0.0)]),
    Instance('XP Max', 'FloatStore', [prop('Value', 10.0)]),
    Instance('Health', 'IntStore', [prop('Value', 100)]),
    Instance('Name', 'StringStore', [prop('Name', '')]),
    Instance('Character', 'ObjectStore', [prop('Value', None)])
    ]

objects = Instance('ObjectStorage', 'service', [])

objects.newChild(Instance('PlayerInfo', 'folder', []))
playerInfo = objects.locateForChild('PlayerInfo', 'folder')

for s in list(playerInfoStuff): playerInfo.newChild(s)
```

### **[Documentation](https://sombrero64.github.io/PythonSharp/doc)**

### [License](https://github.com/Sombrero64/PythonSharp/blob/master/LICENSE)

#### [Logos/Icons](https://sombrero64.github.io/PythonSharp/logo/logos)

## Credits

[Daniel Lawson](https://github.com/Sombrero64); creator

[18001767679](https://github.com/18001767679)

Dan's Papa

Copyright (©) 2020 Daniel Lawson
