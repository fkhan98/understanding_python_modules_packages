import helper_scripts
import numpy as np
x = np.array([2.3, 4.5, -9.3, 1.11])

y = np.array([4.9, 1.72, 1, -2.771])


euc_dis = helper_scripts.euclidean_distance(x,y)
print('euclidean distance is', euc_dis)

cos_dis = helper_scripts.cosine_distance(x,y)
print('cosine distance is', cos_dis)
