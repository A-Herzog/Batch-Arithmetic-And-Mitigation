from math import prod, exp


def PowerFactorial(x: float, n: int) -> float:
    """Calculates x^n/n!"""
    if n == 0:
        return 1
    return prod([x / i for i in range(1, n + 1)])


def P2(lmbda: float, mu: float, CVI: float, CVS: float, c: int, bI: int, bS: int) -> float:
    a = (lmbda * bI) / mu
    rho = a / (bS * c)

    part1 = PowerFactorial(a / bS, c) / (1 - rho)
    part2 = sum([PowerFactorial(a / bS, k) for k in range(c)])
    return part1 / (part1 + part2)


def ENQ_approx(lmbda: float, mu: float, CVI: float, CVS: float, c: int, bI: int, bS: int, useKLB : bool = False) -> float:
    a = (lmbda * bI) / mu
    rho = a / (bS * c)

    P2_val = P2(lmbda, mu, CVI, CVS, c, bI, bS)

    if useKLB:
        SCVIStar = bI / bS * CVI**2
        if SCVIStar <= 1:
            KLB = exp(-2 / 3 * (1 - rho) / P2_val * (1 - SCVIStar)**2 / (SCVIStar + CVS**2))
        else:
            KLB = exp(-(1 - rho) * (SCVIStar - 1) / (SCVIStar + 4 * CVS**2))
    else:
        KLB = 1

    return rho / (1 - rho) * P2_val * (bI * CVI**2 + bS * CVS**2) / 2 * KLB + (bI - 1) / 2 + (bS - 1) / 2


def EN_approx(lmbda: float, mu: float, CVI: float, CVS: float, c: int, bI: int, bS: int, useKLB : bool = False) -> float:
    a = (lmbda * bI) / mu
    rho = a / (bS * c)

    P2_val = P2(lmbda, mu, CVI, CVS, c, bI, bS)

    if useKLB:
        SCVIStar = bI / bS * CVI**2
        if SCVIStar <= 1:
            KLB = exp(-2 / 3 * (1 - rho) / P2_val * (1 - SCVIStar)**2 / (SCVIStar + CVS**2))
        else:
            KLB = exp(-(1 - rho) * (SCVIStar - 1) / (SCVIStar + 4 * CVS**2))
    else:
        KLB = 1

    return rho / (1 - rho) * P2_val * (bI * CVI**2 + bS * CVS**2) / 2 * KLB + (bI - 1) / 2 + (bS - 1) / 2 + a


def EW_approx(lmbda: float, mu: float, CVI: float, CVS: float, c: int, bI: int, bS: int, useKLB : bool = False) -> float:
    a = (lmbda * bI) / mu
    rho = a / (bS * c)

    P2_val = P2(lmbda, mu, CVI, CVS, c, bI, bS)

    if useKLB:
        SCVIStar = bI / bS * CVI**2
        if SCVIStar <= 1:
            KLB = exp(-2 / 3 * (1 - rho) / P2_val * (1 - SCVIStar)**2 / (SCVIStar + CVS**2))
        else:
            KLB = exp(-(1 - rho) * (SCVIStar - 1) / (SCVIStar + 4 * CVS**2))
    else:
        KLB = 1

    return (rho / (1 - rho) * P2_val * (bI * CVI**2 + bS * CVS**2) / 2 * KLB + (bI - 1) / 2 + (bS - 1) / 2) * 1 / (lmbda * bI)