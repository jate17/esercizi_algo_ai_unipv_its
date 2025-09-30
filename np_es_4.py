import numpy as np 

def calcola_determinate(arr):
    if arr.shape != (2,2):
        return "Shape diverso"

    try: 
        inv = np.linalg.inv(arr)
        return inv
    except np.linalg.LinAlgError as e:
        return f"Errore: {e}"


f = np.array([[1,2], [2,4]])
print(calcola_determinate(f))