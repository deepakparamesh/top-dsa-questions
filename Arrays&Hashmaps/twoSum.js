https://leetcode.com/problems/two-sum/

var twoSum = function(nums, target) {
    let hashMap = {};
    for(let [index, value] of nums.entries()){
        let difference = target - value;
        if(difference in hashMap) {
            return [hashMap[difference], index]
        };
        hashMap[value] = index; 
    }
};