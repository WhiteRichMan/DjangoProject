import os
from pathlib import Path


print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(os.path.abspath(os.path.join(os.path.dirname(__file__))))
print(Path(__file__).resolve().parent.parent)
