class Solution:
    def maxArea(self, height: List[int]) -> int:
        best, left, right = 0, 0, len(height)-1
        while left<right:
            temp = min(height[left], height[right])*(right-left)
            best = temp if temp>best else best
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return best
