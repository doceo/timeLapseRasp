from pathlib import Path
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

data_folder = Path("image/")

print (data_folder)

file_to_open = data_folder / "stills.txt"

with open(file_to_open) as f:
	
	print(f.read())
	
	img = Image.open(read_data)
	
	draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
	font = ImageFont.truetype("sans-serif.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
	draw.text((0, 0),"Sample Text",(255,255,255),font=font)
	img.save(data_folder + 'out' + read_data)
