import numpy as np

scores = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [95, 88, 92],
    [50, 65, 55]
])

print(scores.shape)
print(scores.ndim)
print(scores.size)
print(scores[1])
print(scores[:, 2])
print(scores[2, 1])
print(scores[:2, 1:])
print(scores[scores > 80])
print(scores[(scores >= 70) & (scores <= 90)])