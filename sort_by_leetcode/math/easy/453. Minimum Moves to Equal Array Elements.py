"""

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

"""
"""n-1个数加1，相当于所有的数都加1，然后其中一个数减去了1，所以按照这个思路，也就是求将所有数都变成最小的那个数所需要的步骤"""
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)
    
让我们定义 sum 为移动前数组中所有元素的和； minNum 为数组中最小的元素值； n 是数组的长度 
那么，在 m 次移动操作后，我们得到了数组的元素为 x （此时数组中的元素已经全部相等），于是我们可以得到这么一个关系： 
sum + m * (n - 1) = x * n 
实际上： 
x = minNum + m 
最后，我们能够得到这么一个关系式： 
sum - minNum * n = m 
所以现在这个问题非常简单了

    
首先，我们需要明白，数组的最后状态肯定是所有元素相等，我们拿着这个相等的元素值 x，就可以得到这么一个关系式：

sum + m * (n - 1) = x * n

这个式子是什么意思呢？sum 也就是所有元素的和，x * n 也就是移动操作后所有元素的和；m 是我们的移动次数，
因为我们每次操作都是将 n - 1 个元素的值加 1，因此每次移动操作都实际上给所有元素的和增加了 n - 1 的增量值；因此我们得到了上述这个等式

然后，我们还找到了这么一个式子：

x = minNum + m

这个式子又是什么意思呢？x 是移动后的元素值，minNum 是移动前数组中最小的值，那么我们通过了移动操作使得 minNum 变成了 x，
你说 x 等不等于 minNum + m 呢 ^_^

最后，我们将这两个式子结合起来，得到了这么一个式子：

sum - minNum * n = m

这个式子中，sum 可得，minNum 可得，n 已知，m （也就是移动此时）就可以求出来了
