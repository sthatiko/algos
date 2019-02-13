import math
import json


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n, l, r = len(nums1), len(nums2), 0, 0
        a = int(math.ceil((m + n) / 2) + 1)
        _a, _b, k = 0, 0, 0
        while l < m and r < n:
            if nums1[l] < nums2[r]:
                _a = _b
                _b = nums1[l]
                l += 1
            else:
                _a = _b
                _b = nums2[r]
                r += 1
            k += 1
            if k == a:
                break
        if k < a:  # i,e while condition failed
            if l == m:
                while r < n:
                    _a = _b
                    _b = nums2[r]
                    k += 1
                    if k == a:
                        break
                    r += 1
            else:
                while l < m:
                    _a = _b
                    _b = nums1[l]
                    k += 1
                    if k == a:
                        break
                    l += 1
        if (m + n) % 2 == 0:
            return (_a + _b) / 2
        else:
            if k < a:
                return _b
            return _a


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums1 = stringToIntegerList(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);

            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()