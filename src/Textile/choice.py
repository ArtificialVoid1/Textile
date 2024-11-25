from typing import Any
from console import Color3, RICH_CONSOLE
from enum import Enum

class DisplayType(Enum):
    NO_DISPLAY = ''
    NUMBERED = '# '
    BULLET_POINT = '* '
    ARROW = '> '
    LONG_ARROW = '-> '
    DASH = '- '
    FANCY_NUMBERED = '#.) '
    EQUAL_ARROW = '=> '
    NUMBERED_ARROW = '#> '


class choice:

    def __init__(self,
        *choices, 
        display_type : DisplayType = DisplayType.NUMBERED,
        show_wrong : bool = True,
        
        ):
        self.choices = choices
        self.display_type = display_type
        self.show_wrong = show_wrong
    
    def __call__(self) -> str:
        
        def printChoices(iswrong = False):
            for i, choice in enumerate(self.choices):
                num = self.display_type.value.replace('#', str(i))
                RICH_CONSOLE.print( num + choice )
            if iswrong == True:
                RICH_CONSOLE.print(self.choices, 'red')

            inp = RICH_CONSOLE.input()
            if inp.lower() in self.choices:
                return inp.lower
            else:
                if self.show_wrong == True:
                    printChoices(iswrong=True)
                else:
                    printChoices(iswrong=False)
        
        return printChoices(iswrong=False)

