import numpy as np 
import time

start = time.time()


a = np.array([[1,2], [3,4]])
b = np.array([[1,2], [3,4]])


if a.shape == b.shape:
    c = np.dot(a, b)
    print(c)
    end = time.time()
    t_es = end - start
    print(f"[*] Esecuzione: {t_es:.6f}")
else:
    print("Shape differente")