import numpy as np
arr = np.array([5, 12, 7, 18, 3])
result = np.where(arr > 10)
print("Indices where value > 10:", result)