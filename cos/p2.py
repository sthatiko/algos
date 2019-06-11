# Write code to reverse a C-Style String. (C-String means that “abcd” is represented as five characters,
# including the null character.)


def main(s):
    start, end, result = 0, len(s)-1, [0]*len(s)
    while start <= end:
        result[start] = s[end]
        result[end] = s[start]
        start += 1
        end -= 1
    return ''.join(result)


if __name__ == '__main__':
    a = 'shravanthatikonda'
    print(main(a))
