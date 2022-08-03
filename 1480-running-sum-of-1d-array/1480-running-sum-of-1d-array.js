/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let runningSum = 0;
    for(let i=0; i <= nums.length -1; i++){
        runningSum += nums[i];
        nums[i] = runningSum
    }
    return nums;
};