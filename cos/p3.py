# Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer.
# NOTE: One or two additional variables are fine. An extra copy of the array is not.


def get_bit(bits, bit_index):
    mask = 1 << bit_index
    res = bits & mask
    return True if res > 0 else False


def set_bit(bits, bit_index):
    mask = 1 << bit_index
    bits = bits | mask
    return bits


def main(s):
    bits = 0
    result = []
    for c in s:
        val = ord(c) - 97
        if not get_bit(bits, val):
            bits = set_bit(bits, val)
            result.append(c)
    return ''.join(result)


if __name__ == '__main__':
    print(main('characters'))
