from PIL import Image, ImageDraw
from operator import attrgetter


#############################
# EDIT THESE FOR PERSONAL USE (
PATH_LOAD = 'orig/barn.jpg'
ITERATIONS = 400
PATH_SAVE = 'mod/barn.png'
#############################

# Background color, forms color of section padding
FILL = (256, 256, 256)

# Will save all images created, each frame, NOT RECOMMENDED
SAVEALL = False

# Creates Ellipses instead, doesn't look great without a square image
ELLIPSE = False

def weighted_average(hist):
    total = sum(hist)
    value = sum(i * x for i, x in enumerate(hist)) / total
    error = sum(x * (value - i) ** 2 for i, x in enumerate(hist)) / total
    error = error
    return value, error


def color_from_histogram(hist):
    r, re = weighted_average(hist[:256])
    g, ge = weighted_average(hist[256:512])
    b, be = weighted_average(hist[512:768])
    e = re * 0.2989 + ge * 0.5870 + be * 0.1140
    return (int(r), int(g), int(b)), e


class Section(object):
    def __init__(self, original, border):
        self.original = original
        self.border = border

        # Get the color and error of the section
        histogram = self.original.image.crop(self.border).histogram()
        self.color, self.error = color_from_histogram(histogram)

        self.area = self.area()

        self.priority = (self.area**.5) * (int(self.error))
        # Add the new section to the list
        self.original.list.append(self)

    def area(self):
        x0, y0, x1, y1 = self.border
        return (x1 - x0) * (y1 - y0)

    def split(self):
        # used to calculate borders for splits
        x0, y0, x1, y1 = self.border

        x0 = int(x0)
        y0 = int(y0)
        x1 = int(x1)
        y1 = int(y1)

        # width-middle, height-middle
        wm = int(x0 + (x1 - x0)/2)
        hm = int(y0 + (y1 - y0)/2)

        # Create the new sections
        #top_left
        Section(self.original, (x0, y0, wm, hm))
        #top_right
        Section(self.original, (wm, y0, x1, hm))
        #bottom_left
        Section(self.original, (x0, hm, wm, y1))
        #bottom_right
        Section(self.original, (wm, hm, x1, y1))

    def create(self):
        draw = ImageDraw.Draw(self.original.image)
        draw.rectangle(self.border, self.color)


class Original(object):
    def __init__(self, image):
        self.image = image
        self.width, self.height = self.image.size
        self.list = []
        self.orig = Section(self, (0, 0, self.width, self.height))

    def split(self):
        max_error_obj = max(self.list, key=attrgetter('priority'))
        self.list.remove(max(self.list, key=attrgetter('priority')))
        max_error_obj.split()

    def drawSections(self):
        new_im = Image.new('RGB', (self.width, self.height))
        draw = ImageDraw.Draw(new_im)
        draw.rectangle((0, 0, self.width, self.height), FILL)
        frame = 1
        for sect in self.list:
            x0, y0, x1, y1 = sect.border
            if (ELLIPSE):
                draw.ellipse((x0+1, y0+1, x1-1, y1-1), sect.color)
            else:
                draw.rectangle((x0+1, y0+1, x1-1, y1-1), sect.color)
                if (SAVEALL == True):
                    new_im.save('eyes_gif/eyes_' + str(frame) + '.png')
                    frame += 1

        new_im.save(PATH_SAVE)


def main():
    orig = Image.open(PATH_LOAD).convert('RGB')

    original = Original(orig)

    for x in range (ITERATIONS):
        original.split()


    original.drawSections()


if __name__ == "__main__":
    main()
