"""
special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
Given a special string S, a move consists of choosing two consecutive, non-empty, special substrings of S, and swapping them. (Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)

At the end of any number of moves, what is the lexicographically largest resulting string possible?

Example 1:
Input: S = "11011000"
Output: "11100100"
Explanation:
The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
Note:

S has length at most 50.
S is guaranteed to be a special binary string as defined above.
"""

"""

According to the description , there are 2 requirement for Special-String

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
The 2nd definition is essentially saying that at any point of the string, you cannot have more 0's than 1's.

If we map '1' to '(', '0's to ')', a Special-String is essentially Valid-Parentheses, therefore share all the properties of a Valid-Parentheses
A VP (Valid-Parentheses) have 2 form:

single nested VP like "(())", or "1100";
a number of consecutive sub-VPs like "()(())", or "101100", which contains "()" + "(())" or "10" + "1100"
And this problem is essentially ask you to reorder the sub-VPs in a VP to make it bigger. If we look at this example : "()(())" or "101100", how would you make it bigger?
Answer is, by moving the 2nd sub-string to the front. Because deeply nested VP contains more consecutive '('s or '1's in the front. That will make reordered string bigger.

The above example is straitforward, and no recursion is needed. But, what if the groups of sub-VPs are not in the root level?
Like if we put another "()(())" inside "()(())", like "()(( ()(()) ))", in this case we will need to recursively reorder the children, make them MVP(Max-Valid-Parentheses), then reorder in root.

To summarize, we just need to reorder all groups of VPs or SS's at each level to make them MVP, then reorder higher level VPs;



题目复述

special binary string的定义如下：

0的数量和1的数量相等

串的任意前缀的1的数量大于等于0的数量

给定一个special string S，一个move操作定义如下，选择两个连续、非空的S串的子串，并且交换他们。
（两个串是连续的当且仅当第一个串的最后一个字符后面是第二个串的第一个字符。）现在给定一个special string，
经过任意步move操作之后，能得到的最大的串是什么？

题目解析

首先我们考虑解决此问题的简化版，给一些串的数组，现在需要将这些串拼成一个大串，每次只能交换相邻的串，求一个大串，此串的字典序最大。

例如S = ["abc", "def", "dee"]，最后的结果为"defdeeabc"。

解决此问题需要将串从大到小排列并拼接即得到答案。比较的规则如下，例如a = "def"， b =  "dee"，我们将两个串拼接为ab和ba，
因为ab（defdee） > ba（deedef），所以a > b，即结果串里面a的位置在b的前面会增大字典序。
原因解释：因为每次可以比较相邻的串，因此我们可以通过三趟来找出最大，次大以及最小的串。是不是有点类似冒泡排序。

解决了上面的问题，考虑解决本问题，

对于S = “10 1100”来说，其由两个special string s1="10"和s2="1100"组成，为了让结果最大，只需要将他们排序组合即可。

对于S = “1 10 1100 0 1100”来说，其由两个special string s1="1 10 1100 0"和s2="1100"组成，其中s1还有其子special string，此时需要我们递归处理。

这道题给了我们一个特殊的二进制字符串，说是需要满足两个要求，一是0和1的个数要相等，二是任何一个前缀中的1的个数都要大于等于0的个数。
根据压力山大大神的帖子，其实就是一个括号字符串啊。这里的1表示左括号，0表示右括号，那么题目中的两个限制条件其实就是限定这个括号字符串必须合法，
即左右括号的个数必须相同，且左括号的个数随时都要大
于等于右括号的个数，可以参见类似的题目Valid Parenthesis String。那么这道题让我们通过交换子字符串，生成字母顺序最大的特殊字符串，
注意这里交换的子字符串也必须是特殊字符串，满足题目中给定的两个条件，换作括号来说就是交换的子括号字符串也必须是合法的。那么我们来想什么样的字符串是
字母顺序最大的呢，根据题目中的例子可以分析得出，应该是1靠前的越多越好，那么换作括号来说就是括号嵌套多的应该放在前面。比如我们分析题目中的例子:

11011000    ->    (()(()))

11100100    ->    ((())())

我们发现，题目中的例子中的交换操作其实是将上面的红色部分和蓝色部分交换了，因为蓝色的部分嵌套的括号多，那么左括号就多，在前面的1就多，所以字母顺序大。
所以我们要做的就是将中间的子串分别提取出来，然后排序，再放回即可。上面的这个例子相对简单一些，实际上上面的红色和蓝色部分完全可以更复杂，
所以再给它们排序之前，其自身的顺序应该已经按字母顺序排好了才行，这种特点天然适合递归的思路，先递归到最里层，然后一层一层向外扩展，直至完成所有的排序。

好，下面我们来看递归函数的具体写法，由于我们移动的子字符串也必须是合法的，那么我们利用检测括号字符串合法性的一个最常用的方法，就是遇到左括号加1，
遇到右括号-1，这样得到0的时候，就是一个合法的子字符串了。我们用变量i来统计这个合法子字符串的起始位置，字符串数组v来保存这些合法的子字符串。
好了，我们开始遍历字符串S，遇到1，cnt自增1，否则自减1。当cnt为0时，我们将这个字串加入v，注意前面说过，我们需要给这个字串自身也排序，
所以我们要对自身调用递归函数，我们不用对整个子串调用递归，因为字串的起始位置和结束位置是确定的，一定是1和0，我们只需对中间的调用递归即可，
然后更新i为j+1。当我们将所有排序后的合法字串存入v中后，我们对v进行排序，将字母顺序大的放前面，最后将其连为一个字符串即可，参见代码如下：。
"""
/*
     * 1、找到满足要求的特殊二进制串，该二进制串肯定是以1开始，以0结束,
     * 所以除去最前面的1和最后面的0，中间部分也是特殊二进制串，继续对中间部分进行递归处理。
     * 2、将找到的满足要求的特殊二进制串放入list中，然后按照字典序进行排序。
     * 3、返回进行字典序排序的结果
     * @param S
     * @return
     */
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """

        # a list of substrings
        l = []
        cnt = 0  # count for 1, make a stack 1 push, 0 pull
        i = 0  # S 's pointer, ancher?
        for j, v in enumerate(S):

            import pdb; pdb.set_trace()

            if v == '1':
                cnt = cnt + 1
            else:
                cnt=cnt - 1
            if cnt == 0:  # to make Special as small as possible smallest substrings
                l.append('1' + self.makeLargestSpecial(S[i + 1:j]) + '0')  # first must be 1, last must be 0
                i = j + 1

        return ''.join(sorted(l)[::-1])


s = Solution()
print s.makeLargestSpecial('1011001100')


