/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let [left, right] = [0, height.length-1];
    let max = 0;
    while(left < right){
        let area = (right - left) * Math.min(height[left], height[right]);
        max = (area > max) ? area : max;
        if(height[left] <= height[right]) left++;
        else if(height[right] < height[left]) right--;
    }
    return max;
};