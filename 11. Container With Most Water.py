class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        recArea = 0
        while(left<right):
            h = 0
            l = right - left
            if height[left] < height[right] :
                h = height[left]
                left+=1
            else:
                h = height[right]
                right-=1

            area = h*l
            if(area>recArea):
                recArea = area

        return recArea