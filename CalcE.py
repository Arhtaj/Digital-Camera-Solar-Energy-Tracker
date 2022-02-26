#Thomas Mikhail, 2021
import numpy as np
import math
from numpy import ndarray


# Inputs: Array, number of "resolution" points, minimum accepted value,
# Weight given to pure white, weight given to color designations

def calcE(array, distrib, mintot, whiteweight, colorweight, rw, gw, bw, pw, cw, yw):
    # Range of values to use
    rangergb = 764 - mintot;
    d = -math.floor(rangergb / distrib);
    size = array.shape
    # Energy Matrix
    Emat: ndarray = np.empty([size[0], size[1]])
    t = 0
    for j in array:
        s = 0
        lastknowncolor = yw
        for i in j:
            # Deriving a representation of intensity
            I0 = sum(i)
            if (I0 == 765):
                Emat[t, s] = whiteweight*lastknowncolor
                # print("white")
            else:
                x = distrib
                # Intensity Quotient
                Iq = 0;
                for k in range(764, mintot, d):
                    if (I0 < k) & (I0 > k + d):
                        Iq = distrib * x
                        break
                    else:
                        x = x - 1
                        print(x)
                # "Normalizes" the colors. Allows for an elegant and cost
                # effective way to increase color resolution
                color = i
                minim = min(color)
                color[:] = [c - minim for c in color]
                # Checks for red
                if color[1] == 0 & color[2] == 0:
                    temp = rw * colorweight
                    # print("red")
                # Green
                elif color[0] == 0 & color[2] == 0:
                    temp = gw * colorweight
                    # print("green")
                # Blue
                elif color[0] == 0 & color[1] == 0:
                    temp = bw * colorweight
                    # print("blue")
                # Violet/Purple
                elif color[0] != 0 & color[2] != 0:
                    temp = pw * colorweight
                    # print("violet")
                # cyan
                elif color[1] != 0 & color[2] != 0:
                    temp = cw * colorweight
                # Yellow/grey-white
                else:
                    temp = yw * colorweight
                lastknowncolor = temp / colorweight
                temp = temp * Iq
                Emat[t, s] = temp
                # print(t,s,Emat[t,s])
            s = s + 1
            # dir()
        t = t + 1
    return Emat
