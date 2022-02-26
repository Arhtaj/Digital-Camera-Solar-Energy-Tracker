#Thomas Mikhail, 2021
import numpy
import sys
import numpy as np
from numpy import asarray
from PIL import Image, ImageDraw
import CalcE
from Check import Check
from CheckY import CheckY
import math

# Load image, get details
image = Image.open("")
width, height = image.size
# print(width, height)
image = image.resize((int(width / 4), int(height / 4)), Image.ANTIALIAS)
width, height = image.size
width = int(width)
height = int(height)
# print(width, height)
# Get data, convert to numpy array
array = asarray(image)
# Debug
img = Image.fromarray(array, 'RGB')
####################

# Generate light array
# Values obtained from a combination of various curve fits. Will be updated later to allow for more "resolution" of wavelengths
rw = 0.24
gw = 0.6666
bw = 0.5375
pw = 0.01
ow = 0.99975
yw = 0.55346
cw = 0.4
ww = 127
minlight = 127
Uncollapsed = CalcE.calcE(array, 6, minlight, ww, 1, rw, gw, bw, pw, ow, yw)

# Find max
Iter = 4
print('y')
Liney = Check(Uncollapsed, 0, height, Iter)
print('x')
drawx = int(width / (2 ** (Iter + 1)))
# miny = int(Liney - drawx)
# maxy = int(Liney + drawx)#[miny:maxy,:]
Linex = CheckY(Uncollapsed, 0, width, Iter)
print(Linex, Liney)

# Draw on image (for presentation purposes, not necessary)
drawy = int(height / (2 ** (Iter + 2)))
draw = ImageDraw.Draw(image)
print(drawx, drawy, 2 ** (Iter + 2))
s = [((Linex - drawy), (Liney - drawx)), (Linex + drawy, Liney + drawx)]
draw.rectangle(s, fill="Green", outline="green")
image.show()
