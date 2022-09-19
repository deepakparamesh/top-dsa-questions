/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    let maxArea = 0;
    let stack = [];

    for(let i=0; i<heights.length; i++){
        let start = i;
        while(stack.length > 0 && stack[stack.length-1][1] > heights[i]) {
            let [lastI, lastH] = stack.pop();
            maxArea = Math.max(maxArea, lastH * (i - lastI));
            start = lastI;
        }
        
        stack.push([start, heights[i]]);
    }
    
    for(let j=0; j< stack.length; j++) {
        let currArea = (heights.length - stack[j][0]) * stack[j][1];
        maxArea = Math.max(maxArea, currArea);
    }
    
    return maxArea;
};