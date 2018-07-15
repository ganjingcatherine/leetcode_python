
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
一开始的思路是逆向推，目的坐标(tx, ty)肯定是由(tx-ty, ty)或(tx, ty-tx)，但是坐标限定不为负数，因此比较tx、ty的大小可以唯一确定上一步的步骤
类似搜索的题，从终点往起点看，比较容易猜到正解。
这个题的关键点是，如果 ty > tx，那么必然是从 (tx, ty-tx)到达(tx, ty)这个状态的。
想明白上面，还需要知道一个优化的思路：取模不要一次一次相减

题目大意：
从点(x, y)出发经过一次移动可以到达(x + y, y)或者(x, x + y)

给定点(sx, sy)与(tx, ty)，判断(sx, sy)是否可以经过若干次上述移动到达(tx, ty)
解题思路：
循环取余数
类似于辗转相除法（欧几里得算法）

当 tx > ty  时，找父母的操作就是 tx - ty, 直到 tx = tx % ty 为止。当 tx > ty 和 ty > sy 都满足时，我们可以使用 tx %= ty 来代替 while tx > ty: tx -= ty ，会更快。

当 tx > ty 且 ty = sy  时，我们知道 ty 不能再减了，所以只有 tx 会改变，并且只会通过 一步步地减去ty  来改变。所以,使用 (tx - sx) % ty == 0 会更高效。

ty > tx  的情形同理。可以一直这样做，直到 tx == ty, 此时不需要再做 move 了
"""

 while sx < tx and sy < ty:
            if tx > ty: tx %= ty
            else: ty %= tx
        if sx == tx: return (ty - sy) % sx == 0
        if sy == ty: return (tx - sx) % sy == 0
        return False
