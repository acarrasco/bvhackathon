import sys
from PIL import Image
import numpy
import itertools

def get_statisticals(array):
    n, m = array.shape
    return numpy.histogram(array, 8, range=(0, 256))[0] / (1.0*n*m)

def reduce_array(arr, rows, cols):
    n, m = arr.shape
    result = numpy.zeros((rows, cols))
    for i in xrange(rows):
        for j in xrange(cols):
            result[i, j] = numpy.mean(arr[i*n//rows:(i+1)*n//rows, j*m//cols:(j+1)*m//cols])
    return result

def get_multi_levels(arr, levels):
    base_side = 16
    min_side = min(arr.shape)
    for i in xrange(levels, -1, -1):
        side = (min_side - base_side) * i // levels + base_side
        yield reduce_array(arr, side, side)

def extract_features(filename):
    arr = numpy.array(Image.open(filename).convert('L'))
    return numpy.concatenate([get_statisticals(x) for x in get_multi_levels(arr, 3)])

for fname in map(str.strip, sys.stdin):
    ft = extract_features(fname)
    score = fname.split('_')[-2]
    print fname, " ".join(map(str, ft)), score