/**
 * @param {string} s
 * @return {boolean}
 */
const ALPHA_NUM = /^[a-zA-Z0-9]$/;

var isPalindrome = function(s) {
    // todo
    // remove all non AlphaNumericCharacters
    // By using two pointers check if they are equal
    let left = 0, right= s.length-1;

     while(left < right){
        while(left < right && !ALPHA_NUM.test(s[left]))  left++;

        while(left < right && !ALPHA_NUM.test(s[right]))  right--;
        
        if(s[left].toLowerCase() != s[right].toLowerCase()) return false;

        left++;
        right--;
    }
    return true;
};

function isValidAlphaNumeric(char){  
    if(char.toLowerCase().charCodeAt(0) > 97 && char.toLowerCase().charCodeAt(0) < 122) return true;

    return false;
}