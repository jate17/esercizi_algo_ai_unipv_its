import numpy as np 


def creare_array(rows = 1, cols = 1, val_min = 0, val_max = 100) -> np.ndarray:
    return np.random.randint(val_min,val_max, size=(rows,cols))   


def rettifica(arr) -> np.array:
    arr[arr < 0] = 0
    return arr



f = creare_array(5,6,10,100)

print(f)


g = np.array([5, -2, 8, -1, 0, 15, -4])

rettifica(g)

print(g)
