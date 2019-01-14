import os
import sys

int_size = 32


class TrieNode:
    def __init__(self, value=0, children=None):
        self.value = value
        if children is None:
            self.children = [None]*2


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,  element):
        current = self.root
        for cur_pos in range(int_size-1, 0, -1):
            cur_bit = 1 if (element & 1 << cur_pos) else 0
            if current.children[cur_bit] is None:
                current.children[cur_bit] = TrieNode()
            current = current.children[cur_bit]
        current.value = element

    def query(self, pre_xor):
        current = self.root
        for cur_pos in range(int_size-1, 0, -1):
            cur_bit = 1 if (pre_xor & 1 << cur_pos) else 0
            if current.children[1-cur_bit] is not None:
                current = current.children[1-cur_bit]
            elif current.children[cur_bit] is not None:
                current = current.children[cur_bit]
        return pre_xor ^ current.value


def problem_solver(int_arr):
    pre_xor = 0
    trie = Trie()
    trie.insert(0)
    result = 0
    for element in int_arr:
        pre_xor = pre_xor ^ element
        trie.insert(pre_xor)
        result = max(result, trie.query(pre_xor))
    print(result)


sys.stdin = open(os.path.abspath(__file__)[:-2] + 'in', 'r')  # TODO: for local testing only

n_tc = int(input())
for tc in range(n_tc):
    arr_length = int(input())
    arr = list()
    for i in range(arr_length):
        arr.append(int(input()))
    problem_solver(arr)


'''
XOR Sum
https://www.geeksforgeeks.org/find-the-maximum-subarray-xor-in-a-given-array/
https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=345&page=show_problem&problem=2683

Given an array of N numbers, we wish to choose a contiguous sub-sequence of the array, so that the
bitwise XOR of all chosen numbers is maximum. Bitwise XOR is defined as follows: every bit in the
answer is obtained by applying XOR logic on the corresponding bits of the set of numbers. For example
7, 8 and 5 are XORed as follows,
Numbers in binary: 0111 1000 0101 ----- 1010
So the answer is 10 (in decimal). The same answer can be obtained in C/C++/Java by using the
XOR operator as 7ˆ8ˆ5.
Input
The first line contains the number of test cases T. The first line of each test-case contains one integer,
N (size of the array). The next N lines of each test-case contain integers denoting the elements of the
array.
Output
For each test case, output a single line containing the maximum sum that can be obtained.
Constraints:
• 1 ≤ T ≤ 10
• 1 ≤ N ≤ 100, 000
• All input integers will be non-negative and fit into 32 bit signed integer.
Sample Input
2 5 3 7 7 7 0 5 3 8 2 6 4
Sample Output
7 15
'''