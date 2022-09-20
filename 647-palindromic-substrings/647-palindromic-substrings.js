/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    let result =0;
    for(let i =0; i <s.length; i++){
        let [left, right] = [i,i];
        while(left >= 0 && right < s.length && s[left] === s[right]) {
            result +=1;
            left -= 1;
            right +=1;
        }
        
        [left, right] = [i, i+1];
        while(left >= 0 && right < s.length && s[left] === s[right]) {
            result +=1;
            left -= 1;
            right +=1;
        }
    }
    return result;
};
