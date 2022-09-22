/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a,b) => a[0] - b[0]);
    const result = [intervals[0]];
    
    for(let current of intervals){
        let previous = result[result.length -1];
        if(previous[1] >= current[0]) {
            previous[1] = Math.max(current[1], previous[1]);
        } else {
            result.push(current);
        }
    }
    return result;
};