import numpy as np
from Bissection import Bissection
from pointfixe import pointfixe


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



# Question j)
def g1(Q):
    return np.log(-Q/2 + 5)

def g2(Q):
    return 10 - 2*np.exp(Q)

def print_table(iterations, titre, max_n=None):
    N = len(iterations) - 1
    if max_n is None or max_n > N:
        max_n = N
    print("\n" + titre)
    print("n\tQn\t\t\t|en|≈|Qn-Qn-1|\t|e(n+1)/en|\t|e(n+1)/en^2|\t|e(n+1)/en^3|")

    for n in range(0, max_n + 1):
        Qn = iterations[n]
        if n == 0:
            print(f"{n}\t{Qn:.16f}\t-\t\t-\t\t-\t\t-")
            continue
        en = abs(iterations[n] - iterations[n-1])
        if n < max_n:
            en1 = abs(iterations[n+1] - iterations[n])
            r1 = en1/en if en != 0 else np.nan
            r2 = en1/(en**2) if en != 0 else np.nan
            r3 = en1/(en**3) if en != 0 else np.nan
            print(f"{n}\t{Qn:.16f}\t{en:.10e}\t{r1:.10e}\t{r2:.10e}\t{r3:.10e}")
        else:
            print(f"{n}\t{Qn:.16f}\t{en:.10e}\t-\t\t-\t\t-")

Q0 = 1.0
tolr = 1e-8
nmax = 150

# Tableau g1
its_g1 = pointfixe(g1, Q0, tolr, nmax)
print_table(its_g1, "Tableau (g1) : g1(Q)=ln(-Q/2+5)")

# Tableau g2
its_g2 = pointfixe(g2, Q0, tolr, nmax)
print_table(its_g2, "Tableau (g2) : g2(Q)=10-2e^Q (Q0 à Q5)", max_n=5)

# Question l)
def g3(Q):
    return Q - (np.exp(Q) + Q/2 - 5) / (np.exp(Q) + 1/2)

#Tableau g3
its_g3 =pointfixe(g3, Q0, tolr, nmax)
print_table(its_g3, "Tableau (g3) : g3(Q)=Q + (e^Q + Q/2 - 5)/(e^Q + 1/2)", max_n=10)

#Question m)
def g1_stef(Q):
    gQ = g1(Q)
    ggQ = g1(gQ)
    return Q - (gQ - Q)**2 / (ggQ - 2*gQ + Q)

def g2_stef(Q):
    gQ = g2(Q)
    ggQ = g2(gQ)
    return Q - (gQ - Q)**2 / (ggQ - 2*gQ + Q)

def gN_stef(Q):
    gQ = g3(Q)
    ggQ = g3(gQ)
    return Q - (gQ - Q)**2 / (ggQ - 2*gQ + Q)

its_g1Steff = pointfixe(g1_stef, Q0, tolr, nmax)
print_table(its_g1Steff, "Tableau (g1_stef) : g1_stef(Q)=Q - (g1(Q) - Q)^2 / (g1(g1(Q)) - 2*g1(Q) + Q)", max_n=10)
its_g2Steff = pointfixe(g2_stef, Q0, tolr, nmax)
print_table(its_g2Steff, "Tableau (g2_stef) : g2_stef(Q)=Q - (g2(Q) - Q)^2 / (g2(g2(Q)) - 2*g2(Q) + Q)", max_n=10)
its_g3Steff = pointfixe(gN_stef, Q0, tolr, nmax)
print_table(its_g3Steff, "Tableau (g3_stef) : g3_stef(Q)=Q - (g3(Q) - Q)^2 / (g3(g3(Q)) - 2*g3(Q) + Q)", max_n=10)

