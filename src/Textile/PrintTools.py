from __future__ import annotations

#--------------------------------------------------

from PIL import Image

from console import RICH_CONSOLE, Color3

def printIMG(ImagePath : str) -> None:
    IMG = Image.open(ImagePath)

    for y in range(IMG.size[1]):
        for x in range(IMG.size[0]):
            r, g, b = IMG.getpixel((x, y))
            NewClr = Color3.from_rgb((r, g, b))
            RICH_CONSOLE.print('██', Style=NewClr, end='')