def split_number(number):
    str_num = str(number)
    middle = len(str_num)//2
    high = int(str_num[:middle])
    low = int(str_num[middle:])
    return high, low

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    m = max(len(str(x)), len(str(y)))
    m2 = m // 2
    high1, low1 = split_number(x)
    high2, low2 = split_number(y)
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)
    return (z2 * 10**(2 * m2)) + ((z1 - z2 - z0) * 10**m2) + z0


num1 = 1234567891
num2 = 987654321

result = karatsuba(num1, num2)
print(f"Karatsuba multiplication of {num1} and {num2} is: {result}")