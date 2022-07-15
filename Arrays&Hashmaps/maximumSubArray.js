https://leetcode.com/problems/maximum-subarray/

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