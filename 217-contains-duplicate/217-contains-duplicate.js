/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let hashMap = {};
    for(let [index, value] of nums.entries()) {
        if(value in hashMap) return true;
        hashMap[value] = index;
    }
    return false;
};

// Time Complexity is : O(n)
// Space Complexity is : O(n)