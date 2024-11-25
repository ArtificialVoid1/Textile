from rich.console import Console
from rich.style import Style
from rich.color_triplet import ColorTriplet
from rich.color import Color, ColorType

RICH_CONSOLE = Console()


class Color3:

    @staticmethod
    def RgbToStyle(color : tuple[int, int, int]):
        ntriplet = ColorTriplet(color[0], color[1], color[2])
        NewColor = Color('newColor', ColorType.TRUECOLOR, triplet=ntriplet)
        NewStyle = Style(color=NewColor)
        return NewStyle

    def __init__(self, color : str):
        self.color = color

    @classmethod
    def from_rgb(cls, Color : tuple[int, int, int]):
        cls.__init__(cls.RgbToStyle(Color))
    
    def __call__(self):
        return self.color
    
