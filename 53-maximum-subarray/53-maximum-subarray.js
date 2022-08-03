/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    maxSub = nums[0];
    curSum = 0;
    
    for(num of nums){
        if(curSum < 0) curSum = 0;
        curSum += num;
        maxSub = Math.max(maxSub, curSum);
    }
    return maxSub;
};