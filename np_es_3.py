import numpy as np 


a = np.array([[1,2], [3,4]])

print(f"Matrice: {a}")

inv_a = np.linalg.inv(a)
print(f"Inversa: {inv_a}")

p = a @ inv_a

print(f"Prodotto: {p}")