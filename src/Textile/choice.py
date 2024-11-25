from typing import Any
from console import Color3, RICH_CONSOLE
from enum import Enum

class DisplayType(Enum):
    NO_DISPLAY = 0
    NUMBERED = 1
    BULLET_POINT = 2
    ARROW = 3
    LONG_ARROW = 4
    DASH = 5
    FANCY_NUMBERED = 6


class choice:

    def __init__(
        *choices, 
        display_type : DisplayType = DisplayType.NUMBERED,
        show_wrong : bool = True,
        
        ):
        self.choices = choices
        self.display_type = display_type
        self.show_wrong = show_wrong
    
    def __call__(self) -> str:
        return 'ye'
