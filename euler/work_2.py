def main():
    f1, f2, limit, s = 1, 2, 4000000, 2
    while True:
        f = f1 + f2
        if f > limit:
            break
        if not f & 1:
            s += f
        f1 = f2
        f2 = f
    return s


if __name__ == '__main__':
    print(main())
