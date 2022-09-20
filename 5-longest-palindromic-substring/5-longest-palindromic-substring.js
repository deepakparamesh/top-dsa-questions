/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let result = "";
    let resultLength = 0;
    
    for(let i=0; i < s.length; i++) {
        let [left, right] = [i, i];
        
        while(left >= 0 && right < s.length && s[left] === s[right]) {
            if(right - left + 1 > resultLength) {
                result = s.slice(left, right+1);
                resultLength = result.length;
            }
            left -= 1;
            right += 1;
        }
        
        [left, right] = [i, i+1]
        while(left >= 0 && right < s.length && s[left] === s[right]) {
            if(right - left + 1 > resultLength) {
                result = s.slice(left, right+1);
                resultLength = result.length;
            }
            left -= 1;
            right += 1;
        }
    }
    
    return result;
};