import numpy as np
from Bissection import Bissection


def f(Q):
    return np.exp(Q) + Q/2 - 5

tol = 1e-6
nmax = 100
X = Bissection(f, 1.0, 2.0, tol, nmax)
Q15 = X[14]
Q16 = X[15]

print("\n--- Résultats pour la question (c) ---")
print("Q15 =", Q15)
print("Q16 =", Q16)
print("|Q16 - Q15| =", abs(Q16 - Q15))
print("O(Q15) =", np.exp(Q15))
print("D(Q15) =", -Q15/2 + 5)

erreur = abs(Q16 - Q15)

Delta_O = np.exp(Q15) * erreur
Delta_D = 0.5 * erreur

print("\n--- Bornes par propagation d'erreur ---")
print("Delta_O <=", Delta_O)
print("Delta_D <=", Delta_D)