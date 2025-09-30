import numpy as np 


#2.1.5
def calcola_determinate(arr):
    if arr.shape != (2,2):
        return "Shape diverso"

    try: 
        inv = np.linalg.inv(arr)
        return inv
    except np.linalg.LinAlgError as e:
        return f"Errore: {e}"


#Non avvevo voglia di farla -> 2.1.6
def inverti_se_invertibile(mat):
     if isinstance(mat, np.ndarray) and mat.ndim == 2 and mat.shape[0] == mat.shape[1] and np.linalg.det(mat) != 0:
        return np.linalg.inv(mat)
    else:
        return None


f = np.array([[1,2], [2,4]])
print(calcola_determinate(f))


