import sys
from PIL import Image, ImageDraw, ImageFont


images = []
myFont = ImageFont.truetype('arial_bold.ttf', 65)

for arg in sys.argv[1:]:
    image = Image.open(arg)
    I1 = ImageDraw.Draw(image)
    I1.text((5,0 ), "No teacher i am not autistic", font=myFont, fill =(0, 0, 0))
    images.append(image)


images[0].save(
    'output.gif',
    save_all=True,
    append_images=images[1:],
    duration=30,    
    loop=0
)