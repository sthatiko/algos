def find_sum(n):
    sum, count = 0, 1
    while n * count < 1000:
        sum += n * count
        count += 1
    return sum


def lcm(a, b):
    return a*b//gcd(a, b)


def gcd(a, b):
    if 0 in [a, b]:
        return max(a, b)
    if a == b:
        return a
    if a > b:
        return gcd(a-b, b)
    return gcd(b-a, a)


def main():
    sum = 0
    for n in [3, 5]:
        sum += find_sum(n)
    sum -= find_sum(lcm(3,5))
    return sum


if __name__ == '__main__':
    print(main())
