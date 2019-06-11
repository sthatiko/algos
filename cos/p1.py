# Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data
# structures


def main(s):
    count = [0]*26
    for c in s:
        count[ord(c) - 97] += 1
    for n in count:
        if n > 1:
            return True
    return False


if __name__ == '__main__':
    s = 'bloke'
    print(main(s))
