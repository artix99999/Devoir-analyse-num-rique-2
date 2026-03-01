def pointfixe(fonction_pointfixe, Q0, tolr, nmax):

    iterations = [Q0]
    for _ in range(nmax):
        Qn = fonction_pointfixe(iterations[-1])
        iterations.append(Qn)
        erreur_relative = abs(Qn - iterations[-2]) / abs(Qn)
        if erreur_relative < tolr:
            break
    return iterations