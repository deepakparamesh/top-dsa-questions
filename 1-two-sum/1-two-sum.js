/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hashMap={};
    for(let i=0;i<nums.length;i++){
        let difference = target - nums[i];
        if(difference in hashMap) {
            return [hashMap[difference], i];
        }
        hashMap[nums[i]] = i;
    }
};