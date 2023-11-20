def fast_pow_recursive(a, n):

    if n == 0:

        return 1

    elif n % 2 == 1:

        return a * fast_pow_recursive(a, n - 1)

    else:

        temp = fast_pow_recursive(a, n // 2)

        return temp * temp

print(fast_pow_recursive(3, 5))

def fast_pow_iterative(a, n):

    result = 1

    while n > 0:

        if n % 2 == 1:

            result *= a

        a *= a

        n //= 2

    return result

print(fast_pow_iterative(3, 5))
