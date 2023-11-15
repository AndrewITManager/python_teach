def alg_evklida(a, b):
    while b:
        a, b = b, a % b#остаток от деления
    return a

print(alg_evklida(98, 56))


def gcd_recursive(a, b):

    if b == 0:

        return a

    return gcd_recursive(b, a % b)

print(gcd_recursive(98, 56))