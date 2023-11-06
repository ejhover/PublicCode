class Solution:
    def maxProfit(self, prices) -> int:
        # loop through and add value to dictionary/variable if it is smallest value and then for each value that's not, check the diffference between the two and update the answer variable
        smallest, ans = 9999, 0
        for val in prices:
            if val < smallest:
                smallest = val
            elif val-smallest > ans:
                ans = val-smallest
        return ans