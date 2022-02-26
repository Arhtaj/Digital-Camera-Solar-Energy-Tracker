#Thomas Mikhail, 2021
import math as m
import numpy


def CheckY(array, start, end, steps):
    # print(steps)
    d = m.floor((end - start) / 2)
    half = d + start
    if steps == 0:
        return half
    else:
        steps = steps - 1
        d2 = m.floor((end - start) / 4)
        quarter = start + d2
        three_quarters = half + d2
        sum1 = int(numpy.sum(numpy.sum(array[:, start:half])))
        # print(sum1)
        sum2 = int(numpy.sum(numpy.sum(array[:, quarter:three_quarters])))
        sum3 = int(numpy.sum(numpy.sum(array[:, half:end])))
        if (sum1 * 0.9 > sum2) & (sum1 * 0.9 > sum3):
            print("left", sum1, sum2, sum3)
            return CheckY(array, start, half, steps)
        elif (sum3 * 0.9 > sum1) & (sum3 * 0.9 > sum2):
            print("right", sum1, sum2, sum3)
            return CheckY(array, half, end, steps)
        else:
            print("stay", sum1, sum2, sum3)
            return CheckY(array, quarter, three_quarters, steps)
