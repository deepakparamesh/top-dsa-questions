https://leetcode.com/problems/product-of-array-except-self/

// var productExceptSelf = function(nums) {
//     for(let [index, value] of nums.entries()) {
//         let copyOfArray = [...nums];
//         nums[index] = multipliedValue(copyOfArray.splice(index, 1));
//     };
//     return nums;
// };

// function multipliedValue(nums){
//     return nums.reduce((accumulator, currentValue) => accumulator * currentValue, 1);
// }

var productExceptSelf = function(nums) {
    let result = [];
    
    // iterating for prefix;
    let prefix = 1;
    for(let [index, value] of nums.entries()) {
        result[index] = prefix;
        prefix = prefix * nums[index];
    }
    
    // iterating for postFix
    let postFix =1;
    for(let i=nums.length-1; i>=0; i--){
        result[i] *= postFix;
        postFix *= nums[i]
    }
    return result;
}