https://leetcode.com/problems/longest-repeating-character-replacement/submissions/

// Lessons learnt

// Lesson 1: did not add +1 while calculating windowLength;

// Lesson 2: gave the condition r<= in the while condition.
var characterReplacement = function(s, k) {
    let maxLength = 1;
    let left=0; let right=0;
    let charHashMap = {};

    while(right < s.length){    
        let windowLength = right - left + 1;
        
        if(!charHashMap[s[right]]) {
            charHashMap[s[right]] = 1;
        } else {
            charHashMap[s[right]] += 1;
        }
        
        let condition = windowLength - findMostCharacter(charHashMap) <= k;
        
        if(condition){
            right += 1;
            if(windowLength > maxLength) {
                maxLength = windowLength; 
            }
        } else {
            charHashMap[s[left]] -= 1;
            left +=1;
        }
    };
    
    return maxLength;
};

function findMostCharacter(charHashMap){
    let maxCount = 0;
    for(char in charHashMap) {
        if(charHashMap[char] > maxCount){
            maxCount = charHashMap[char];
        }
    }
    return maxCount;
}

characterReplacement("AABABBA",1);


// Copied Answer
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
 var characterReplacement = function(s, k) {
    let sCharacterSet = {};
    let result = 0;
    let l = 0;
    let maxLength = 0;
    for(let r = 0; r < s.length; r++){
        if(sCharacterSet[s[r]]) sCharacterSet[s[r]]+=1;
        else sCharacterSet[s[r]] = 1;
        maxLength = Math.max(maxLength, sCharacterSet[s[r]])
        if ((r - l + 1) - maxLength > k){
            sCharacterSet[s[l]] -= 1;
            l += 1;
        }
        result = Math.max(result, r - l + 1);
    }
    return result
};