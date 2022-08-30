/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let output = [];
    
    let prefix=1;
    for(let i=0; i<nums.length; i++){
        output[i] = prefix;
        prefix *= nums[i];
    }
    
    let postFix = 1;
    for(let i=nums.length-1; i>=0 ; i--){
        output[i] *= postFix;
        postFix *= nums[i];
    }
    
    return output;
};