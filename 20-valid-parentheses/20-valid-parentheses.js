/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const hashMap = {
     "}" : "{",
     ")" : "(",
     "]" : "["
    }
    let stack = [];
    
    for(let char of s){
        if(!hashMap[char]) stack.push(char);
        else
            if(stack.pop() !== hashMap[char]) return false;
    }
    
    return !stack.length;
};