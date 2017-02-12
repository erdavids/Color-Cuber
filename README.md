# Color Cuber

This is a simple Python program that utilizes the PILLOW library to iteratively break down an original image into sections that slowly become more detailed. A section is colored as the average color from that section of the image. The program calculates a priority for the sections based on the area and error, making it so that more detailed portions of the original image will have receive greater amounts of attention.

This gif shows a summary of the process of the Color Cuber from 1 to 2048 iterations.
![Frog Gif](http://i.giphy.com/A1iIGZFCiZcQ0.gif)

To use the program to create your own images, follow the process below (you will need to edit the file, indicated by #):

    git clone https://github.com/erdavids/Python-Art
    cd Color Cuber
    
Place the original image in the orig folder and edit the fields at the top to indicate iteration and saving path
    
    Python color_cuber.py
    


I drew heavy inspiration from Quads by Michael Fogleman. It is an open source project that can be found ![here](https://github.com/fogleman/Quads). The only code that I used of his is the calculation of the average color and average error, although I edited the error function slightly. I borrowed the `color_from_histogram` function because I am unfamiliar with traversing histograms
