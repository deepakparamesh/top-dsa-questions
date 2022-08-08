/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if(nums.length === 0) return 0;
    
    let hashSet = new Set(nums);
    let max = 0;
    
    for(let num of nums){
        
        if(hashSet.has(num-1)) {
            continue;
        }
        
        let currentMax = 1;
        while(hashSet.has(num+currentMax)) {
            currentMax += 1;
        }
        
        if(currentMax > max) max = currentMax;
    }
    return max;
};