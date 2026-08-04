# def guess(num: int) -> int:
#     ...

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n

        while l <= h:
            mid = (l + h) // 2

            res = guess(mid)   # <-- API call

            if res == 0:
                return mid
            elif res == -1:
                h = mid - 1
            else:
                l = mid + 1