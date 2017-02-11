from PIL import Image, ImageDraw
from operator import attrgetter

FILL = (0, 0, 0)


def weighted_average(hist):
    total = sum(hist)
    value = sum(i * x for i, x in enumerate(hist)) / total
    error = sum(x * (value - i) ** 2 for i, x in enumerate(hist)) / total
    error = error ** 0.5
    return value, error


def color_from_histogram(hist):
    r, re = weighted_average(hist[:256])
    g, ge = weighted_average(hist[256:512])
    b, be = weighted_average(hist[512:768])
    e = re * 0.2989 + ge * 0.5870 + be * 0.1140
    return (r, g, b), e


class Section(object):

    def __init__(self, original, border):
        self.original = original
        self.border = border

        histogram = self.original.image.crop(self.border).histogram()
        self.color, self.error = color_from_histogram(histogram)

        self.original.list.append(self)

    def split(self):
        print('some')
        # Something

class Original(object):

    def __init__(self, image):
        self.image = image
        self.width, self.height = self.image.size
        self.list = []
        self.orig = Section(self, (0, 0, self.width, self.height))

    def split(self):
        print('some')
        #max_error = max(list, key=attrgetter('error'))


def main():
    orig = Image.open('orig/image_1.jpg').convert('RGB')

    original = Original(orig)

    original.split()
    # orig.show()
    #width, height = orig.size

    #draw = ImageDraw.Draw(orig)
    #draw.rectangle((0,0,width/2,height/2), FILL)
    #draw.rectangle((width/2,height/2,width,height), FILL)
    #box = (origin, origin, width, height)

    orig.save('mod/image_1.png')


if __name__ == "__main__":
    main()
