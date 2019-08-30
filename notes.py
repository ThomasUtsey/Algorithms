# training kit short video

'''
given an image represented by an NxN matrix, where each pixel in the image is an integer from 0 to 9, write a function
rotateimage that rotates the image by 90 degrees in the counter-clockwise direction.

for example:

rotateImage ([
    [1,2],
    [3,4]
])

 should return

 [
     [1.2],
     [3,4]
 ]

questions to consider:
How is the matrix represented?

How do I move matrix elements around?

how do I rotate a matrix in any direction?

'''


# The Fibonacci sequence (in Math)
'''
mathmatical formula for fibonacci sequence

Fn = Fn-1 + Fn-2
F0 = 0,F1 = 1
'''


# def nth_fib(n):
#     if n < 2:
#         return n
#     return nth_fib(n-1) + nth_fib(n - 2)


# print(nth_fib(10))


# def Fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a+b
#     return a


# print(Fib(10))


# lecture with Artem Litchman


# practical understanding of a problem
'''
Ask questions on whats expected what is not what needs to be checked for for example a problem that is not set of an empty
array and - number. 

Planning such as psuedocode or plane englesh

put something to together to get a first pass

add fail safe cases 

optimize for performance and readeability
including variables and redundencies
'''

# factorials
# 5! = 5 * 4 * 3 * 2 * 1 is an example of factorials
''' itrative vs recurssion 

base case n = 0
          n = 1

recursive case n - 1

in solving this code recursion would be less efficient due to memory useage
'''


# def factorials(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorials(n-1)

''' can be [] will return 0
[0,0,0,0] should equal 2 not 3
length < 1000
no num > 1000'''

''' 
plan first pass
got through array
count # of appearance of each num
do math.
'''
# def pairs(arr):
#     if len(arr)<= 1:
#         return 0

#     counter_arr = [0] * [max(arr)+1]

#     for num in arr:
#         counter_arr[num] += 1
#     duplicate_count = 0
#     for num in counter_arr:
#         duplicate_count += num // 2
#     return duplicate_count

# Definition for a binary tree node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution(object):
# def preorderTraversal(self, root):

#     if not root:
#         return []
#     stack = [root]
#     res = []

#     while stack:
#         node = stack.pop()
#         res.append(node.val)

#         if node.right:
#             stack.append(node.right)

#         if node.left:
#             stack.append(node.left)
#     return res
