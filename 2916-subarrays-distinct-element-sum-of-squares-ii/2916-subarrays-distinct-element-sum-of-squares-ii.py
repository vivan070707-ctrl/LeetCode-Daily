import sys

sys.seturllib = None  
sys.setrecursionlimit(200000)


class Solution:

    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum_sq = [0] * (4 * n)
        tree_sum = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, l, r):
            v = lazy[node]
            if v != 0:
                mid = (l + r) // 2
                # Left child
                left_child = 2 * node
                l_len = mid - l + 1
                tree_sum_sq[left_child] = (
                    tree_sum_sq[left_child]
                    + 2 * v * tree_sum[left_child]
                    + v * v * l_len
                ) % MOD
                tree_sum[left_child] = (
                    tree_sum[left_child] + v * l_len
                ) % MOD
                lazy[left_child] = (lazy[left_child] + v) % MOD

                # Right child
                right_child = 2 * node + 1
                r_len = r - mid
                tree_sum_sq[right_child] = (
                    tree_sum_sq[right_child]
                    + 2 * v * tree_sum[right_child]
                    + v * v * r_len
                ) % MOD
                tree_sum[right_child] = (
                    tree_sum[right_child] + v * r_len
                ) % MOD
                lazy[right_child] = (lazy[right_child] + v) % MOD

                lazy[node] = 0

        def update(node, l, r, ql, qr, v):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                length = r - l + 1
                tree_sum_sq[node] = (
                    tree_sum_sq[node] + 2 * v * tree_sum[node] + v * v * length
                ) % MOD
                tree_sum[node] = (tree_sum[node] + v * length) % MOD
                lazy[node] = (lazy[node] + v) % MOD
                return

            push(node, l, r)
            mid = (l + r) // 2
            update(2 * node, l, mid, ql, qr, v)
            update(2 * node + 1, mid + 1, r, ql, qr, v)

            tree_sum_sq[node] = (
                tree_sum_sq[2 * node] + tree_sum_sq[2 * node + 1]
            ) % MOD
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD

        last = {}
        total_ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            last[x] = i

            update(1, 0, n - 1, prev + 1, i, 1)

            
            total_ans = (total_ans + tree_sum_sq[1]) % MOD

        return total_ans