# %%
import PIL
import random
from PIL import Image,ImageFont,ImageDraw

def add_number (num,pic,color='red'):
    width,heighth=pic.size
    draw=ImageDraw.Draw(pic)
    add_font=ImageFont.truetype('C:\Windows\Fonts\AGENCYR.ttf',50)
    draw.text((width-40,30),'%d'%num,fill=(255,0,0),font=add_font)
    pic.show()
    return pic

if __name__ == "__main__":
    pic=Image.open('draw.jpg')
    num=random.randint(1,10)
    add_number (num,pic,color='red')
# %%
