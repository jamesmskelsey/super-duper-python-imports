# super-duper-python-imports
In this repository we are playing with python imports and inducing those pesky ImportErrors.

## File Organization

```
project
│   README.md
│   main.py   
│
└───animals
│   │   __init.py__
│   │   animal.py
│   │   test_animal.py
│   │   mammal.py
│   │   test_mammal.py
│   │
│   └───canines
│       │   __init__.py
│       │   dog.py
│       │   test_dog.py
```


Dog is in the canine folder, and inherits from Mammal in the previous folder, which inherits
from Animal in that same folder.

If you try to run `py dog.py` file directly from `.\animals\canines`, you will get an **ImportError**. If you run `py main.py` from the top level folder, it will _happily_ allow these imports to work.

Lastly, if you run:
```
> py -m unittest
```
from the top level folder, with these naming conventions (NOTE: the test files are called `test_class_name.py`, which allows unittest to discover them)
you'll get the results that you really, really want. :partying_face:
