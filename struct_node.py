from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    data: int
    next: Optional['Node'] = None
