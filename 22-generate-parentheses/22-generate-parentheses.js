/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    // Add the open bracket only if open < n
    // Add the closed bracked only if closed < open
    // valid: open == closed == n
    let stack = [];
    let result = [];
    
    function backtrack(openCount, closedCount) {
        if(openCount === n && closedCount === n) {
            result.push(stack.join(""));
            return;
        }
        
        if(openCount < n){
            stack.push("(");
            backtrack(openCount+1, closedCount);
            stack.pop();
        }
        
        if(closedCount < openCount) {
            stack.push(")");
            backtrack(openCount, closedCount + 1);
            stack.pop();
        }
    }
    backtrack(0, 0);
    return result;
    
};