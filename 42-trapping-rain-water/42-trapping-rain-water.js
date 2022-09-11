/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let [left, right] = [0, height.length-1];
    let [maxLeft, maxRight] = [height[left], height[right]];
    let area = 0;

    while(left < right){
        [maxLeft, maxRight] = calculateMax(height, left, right, maxLeft, maxRight);
        let tempArea = 0;
        if(maxLeft <= maxRight) {
             left += 1;
             tempArea = Math.min(maxLeft, maxRight) - height[left];
             tempArea = (tempArea < 0) ? 0 : tempArea;
             area += tempArea;
        } else if(maxRight < maxLeft) {
            right -= 1;
            tempArea = Math.min(maxLeft, maxRight) - height[right];
            tempArea = (tempArea < 0) ? 0 : tempArea;
            area += tempArea;
        }
    }
    
    return area;
    
};

function calculateMax(height, left, right, maxLeft, maxRight) {
    maxLeft = (height[left] > maxLeft) ? height[left] : maxLeft;
    maxRight = (height[right] > maxRight) ? height[right] : maxRight;
    return [maxLeft, maxRight];
}