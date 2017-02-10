from PIL import Image, ImageDraw
from operator import attrgetter

FILL = (0, 0, 0)

class Section(object):

	def __init__(self, size):
		self.origin_1, self.origin_2, self.width, self.height = size
		self.error
	def split(self):
		print ('some')
	
class Original(object):
	def __init__(self, image):
		self.image = image
		self.list = []
	def split(self):
		max_error = max(list, key=attrgetter('error'))
		
def main():
	orig = Image.open('orig/image_1.jpg').convert('RGB')
	
	original = Original(orig)
	
	original.split()
	#orig.show()
	#width, height = orig.size
	
	
	#draw = ImageDraw.Draw(orig)
	#draw.rectangle((0,0,width/2,height/2), FILL)
	#draw.rectangle((width/2,height/2,width,height), FILL)
	#box = (origin, origin, width, height)
	
	
	orig.save('mod/image_1.png')
	
	
if __name__ == "__main__":
	main()