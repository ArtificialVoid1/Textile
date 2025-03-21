from __future__ import annotations

#--------------------------------------------------

from PIL import Image

from console import RICH_CONSOLE, Color3, GradientColor3, GradientKeyframe

def printIMG(ImagePath : str) -> None:
    IMG = Image.open(ImagePath)

    for y in range(IMG.size[1]):
        for x in range(IMG.size[0]):
            r, g, b = IMG.getpixel((x, y))
            NewClr = Color3.RgbToStyle((r, g, b))
            RICH_CONSOLE.print('██', Style=NewClr, end='')

def printGradient(text : str, Gradient : GradientColor3, end='\n'):
    textLen = len(text)
    for index, Char in enumerate(text):
        _Time = index / (textLen - 1)
        Color = Gradient.getColor(_Time)
        RICH_CONSOLE.print(Char, Style=Color(), end='')
    RICH_CONSOLE.print(end, end='')
