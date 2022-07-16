https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

// Code worked on the first attempt

function twoSumII(numbers, target){
    let left = 0, right = numbers.length -  1;
    while(left < right){
        let currentSum = numbers[left] + numbers[right];
        if(currentSum < target) left++;
        if(currentSum  > target) right--;  
        if(currentSum == target) return [left+1, right+1];
    }
}

