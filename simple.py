from PIL import Image, ImageDraw

FILL = (0, 0, 0)

def main():
	orig = Image.open('orig/image_1.jpg')
	
	#orig.show()
	
	width, height = orig.size
	
	
	draw = ImageDraw.Draw(orig)
	draw.rectangle((0,0,width/2,height/2), FILL)
	draw.rectangle((width/2,height/2,width,height), FILL)
	
	orig.save('mod/image_1.png')
if __name__ == "__main__":
	main()