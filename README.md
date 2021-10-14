# super-duper-python-imports
In this repository we are playing with python imports and inducing those pesky ImportErrors.



## Heirarchy of Classes

* Animal 
* -> Mammal 
* ---> Dog

## File Organization

```
project
│   README.md
│   main.py   
│
└───animals
│   │   __init.py__
│   │   animal.py
│   │   mammal.py
│   │
│   └───canines
│       │   __init__.py
│       │   dog.py
```


Dog is in the canine folder, and inherits from Mammal in the previous folder, which inherits
from Animal in that same folder.

If you try to run the `dog.py` file directly from .\animals\canines, you will get an ImportError. If you run 'py main.py' from the top level folder, it will happily allow these imports to work.
