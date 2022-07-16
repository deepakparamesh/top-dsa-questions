https://leetcode.com/problems/valid-palindrome/

// Lessons learnt

// Lesson 1: No need to new string, we can implement in O(1) space complexity
// Initially I thought of creating a new string with non-alphanumeric characters
// after watching neetcode video, I realized that it could be done with creating a new string.
// with the help of pointer we can decide 

// Lesson 2: I learnt when to stop the process of comparing the characters. we need to do while(Left <= right)

function validPalindrome(s) {
    let left = 0, right= s.length-1;

    while(left < right){
        while(left < right && !isValidAlphaNumeric(s[left]))  left++;

        while(left < right && !isValidAlphaNumeric(s[right]))  right--;
        
        if(s[left].toLowerCase() != s[right].toLowerCase()) return false;

        left++;
        right--;
    }
    return true;
}

function isValidAlphaNumeric(char){  
    if(char.toLowerCase().charCodeAt(0) > 97 && char.toLowerCase().charCodeAt(0) < 122) return true;

    return false;
}

// validPalindrome("ada");
// validPalindrome("deed");
// validPalindrome("deed deed");
// validPalindrome("ada ada ada");

