/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let current=0;
    let max=0;
    let temp;
    // [curr, max, n, n+1, ..... nums.length - 1]
    for(let n of nums) {
        temp = Math.max(n+current, max);
        current = max;
        max = temp;
    }
    return max;
};