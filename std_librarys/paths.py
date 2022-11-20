# The path class

from pathlib import Path

path = Path('modules/ecommerce/__init__.py')
print(path.exists())
print(path.name)
print(path.parent)

path = path.with_suffix(".txt")
print(path.absolute())