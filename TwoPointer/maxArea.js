/**
 * @param {number[]} height
 * @return {number}
 */

// Lesson learnt

// Lesson 1: Always be clear whether we should go with index or indices.
// Initially you went with indices and that messed up the whole problem.

// Lesson 2: Carelessness with the left pointer and right pointer movement condition validation.
// used if(left < height) instead of if(height[left] < height[right])
var maxArea = function(height) {
    let left=0, right=height.length-1;
    let maxArea = 0;
    while(left < right){
        let tempArea = Math.min(height[left], height[right]) * (right - left);
        if(tempArea > maxArea) maxArea = tempArea;
        if(height[left] < height[right]) left++;
        else if(height[right] < height[left]) right--;
        else left++;
    }
    return maxArea;
};