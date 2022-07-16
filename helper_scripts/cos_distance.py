import numpy as np
from numpy.linalg import norm

def cosine_distance(x, y):
    return 1 -(np.dot(x,y)/(norm(x)*norm(y)))