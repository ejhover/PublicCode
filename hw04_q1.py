# Emmet Hoversten
# hover114
# CSCI 1133 Section 050
# Assignment 4
from PIL import Image

import os
# brown = (209, 133, 24)
# change the color in a picture of Jerry
def color_jerry():
    img = Image.open("data/berry.png")
    rgb_vals = list(img.getdata()) # a list of rgb values
    # loop through the rgb values and if the color is blue, change to brown
    for pos, i in enumerate(rgb_vals):
        if list(i)[:-1] == [0, 0, 255]:
            rgb_vals[pos] = (209, 133, 24, 255)
    img.putdata(rgb_vals)
    img.show()

def main():
    color_jerry()
if __name__ == "__main__":
    main()