import json


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        l = 0
        while l <= n // 2:
            for i in range(l, n - 1-l):
                t = matrix[l][l + i]
                matrix[l][l + i] = matrix[n - 1 - i][l]
                matrix[n - 1 - i][l] = matrix[n - 1 - l][n - l - 1 - i]
                matrix[n - 1 - l][n - l - 1 - i] = matrix[i][n - 1 - l]
                matrix[i][n - 1 - l] = t
            l += 1


def stringToInt2dArray(input):
    return json.loads(input)


def int2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            matrix = stringToInt2dArray(line)

            ret = Solution().rotate(matrix)

            out = int2dArrayToString(matrix)
            if ret is not None:
                print("Do not return anything, modify matrix in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()