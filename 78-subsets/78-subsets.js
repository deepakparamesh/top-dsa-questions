/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    let result  = [];
    let subset  = [];
    
    function dfs(index){
        if(index >= nums.length) {
            result.push(subset.slice());
            return;
        }
        
        subset.push(nums[index]);
        dfs(index + 1);
        
        subset.pop();
        // subset.push(nums[index]);
        dfs(index + 1);
        
    }
    dfs(0);
    
    return result;
};