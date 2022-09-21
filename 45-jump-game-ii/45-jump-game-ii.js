/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let [left, right] = [0,0];
    let jumps = 0;
        
    while(right < nums.length-1) {
        let farthest = 0;
        for(let i=left; i<right+1; i++){
            farthest = Math.max(farthest, nums[i] + i);
        }
        left = right+1;
        right = farthest;
        jumps +=1;
    }
    return jumps;
};