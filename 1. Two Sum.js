/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let i,j,r1,r2,solved=0
    for(i=0;i<nums.length;i++){
        for(j=0;j<nums.length;j++){
            if(nums[i]+nums[j] == target && i!==j){
                r1=i
                r2=j
                solved=1
                break
            }
        }
        if(solved)
            break
    }
    return [r1,r2]
};