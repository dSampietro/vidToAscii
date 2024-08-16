from dataclasses import dataclass
from ascii_magic import AsciiArt #type: ignore
from PIL import Image, ImageFont, ImageDraw #type: ignore

@dataclass
class Info:
    textCols: int
    textRows: int
    

def img_to_text(inputPath: str, outputPath: str, cols=120) -> None:
    img = AsciiArt.from_image(inputPath)
    img.to_file(path=outputPath, columns=cols, monochrome=True) #TODO: remove monochrome


def save_img_to_file(inputPath: str, outputPath: str, fontsize: int, info: Info) -> None:
    with open(inputPath, "r") as f:
        ascii_text: str = f.read()

    img_width = 1920
    img_heigth = fontsize * info.textRows
    img = Image.new('RGB', (img_width, img_heigth), color = (255,255,255))
    fnt = ImageFont.truetype("fonts/Consolas.ttf", fontsize)
    draw = ImageDraw.Draw(img)
    
    draw.text((0,0), ascii_text, font=fnt, fill=(0,0,0))

    img.save(outputPath)