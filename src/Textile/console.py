from rich.console import Console
from rich.style import Style
from rich.color_triplet import ColorTriplet
from rich.color import Color, ColorType

RICH_CONSOLE = Console()


def interpolate(a, b, t):
    return (1 - t) * a + t * b


class Color3:

    @staticmethod
    def RgbToStyle(color : tuple[int, int, int]):
        ntriplet = ColorTriplet(color[0], color[1], color[2])
        NewColor = Color('newColor', ColorType.TRUECOLOR, triplet=ntriplet)
        NewStyle = Style(color=NewColor)
        return NewStyle
    
    @staticmethod
    def lerp(Color1 : Color3 , Color2 : Color3, alpha : float) -> Color3:
        return Color3.from_rgb(
            (
                interpolate(Color1.r, Color2.r, t),
                interpolate(Color1.g, Color2.g, t),
                interpolate(Color1.b, Color2.b, t),
            )
        )

    def __init__(self, color : tuple[int, int, int]):
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
    
    def __mul__(self, other):
        if isinstance(other, Color3):
            return Color3.from_rgb(
                (
                    self.r * other.r,
                    self.g * other.g,
                    self.b * other.b
                )
            )
        elif isinstance(other, (int, float)):
            return Color3(
                (
                    self.r * other,
                    self.g * other,
                    self.b * other,
                )
            )
    def __call__(self):
        return self.RgbToStyle((self.r, self.g, self.b))

class GradientKeyframe:
    Color : Color3
    Time : float
    def __init__(self, _Color : Color3 | (int, int, int), _Time : int | float):
        self.Color = _Color
        self.Time = _Time

class GradientColor3:
    ColorSequence : List[GradientKeyframe]

    def __init__(self, Colors : list[GradientKeyframe]):
        self.ColorSequence = sorted(Colors, key=lambda Color: Color.Time)
        self.MaxTime = 0
        for color in Colors:
            if color.Time > self.MaxTime:
                self.MaxTime = color.Time
        

    def addKeyframe(self, _Color : GradientKeyframe):
        self.ColorSequence.append(_Color)
        if _Color.Time > self.MaxTime:
            self.MaxTime = _Color.Time
        self.ColorSequence = sorted(self.ColorSequence, key=lambda Color: Color.Time)

    def getColor(self, _Time : int | float) -> Color3:
        self.ColorSequence = sorted(self.ColorSequence, key=lambda Color: Color.Time)
        for i in range(len(self.ColorSequence) - 1):
            if self.ColorSequence[i].Time <= _Time < self.ColorSequence[i + 1].Time:
                Color1 = self.ColorSequence[i].Color
                Color2 = self.ColorSequence[i + 1].Color
                
                Alpha = (_Time - self.ColorSequence[i].Time) / (self.ColorSequence[i + 1].Time - self.ColorSequence[i].Time)
                return Color3.lerp(Color1, Color2, Alpha)
                
        if _Time <= self.ColorSequence[0].Time:
            raise IndexError('Time Given is outside Index')
