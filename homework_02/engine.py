"""
create dataclass `Engine`
"""

import dataclasses


@dataclasses
class Engine:
    volume: float
    pistons: int