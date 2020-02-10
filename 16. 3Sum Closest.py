import random
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        out = []
        nums.sort()
        nums_index = []
        add_index = 0
        while(add_index < len(nums)-2):
            nums_index.append(add_index)
            add_index += 20
        
        s1,s2,s3 = 0,0,0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if j == i:
                    continue
                s1, s2 = nums[i], nums[j]
                gap = target - (s1+s2)
                
                #
                key = 0
                for ni in nums_index:
                    if(gap > nums[ni]):
                        key = ni
                # print(key)
                #
                last_gap = ''
                for k in range(key,len(nums)):
                    if(k == i or k == j):
                        continue
                    
                    current_gap = abs(target - (s1+s2+nums[k]))
                    if(last_gap != '' and current_gap > last_gap):
                        break
                    else:
                        last_gap = current_gap
                        s3 = nums[k]
                
                #
                sum_s1_s2_s3 = s1+s2+s3                
                sum_gap = abs(target - sum_s1_s2_s3)
                out.append((sum_gap,sum_s1_s2_s3))
        out.sort(key=lambda tup: tup[0],reverse=False)
        return out[0][1]
