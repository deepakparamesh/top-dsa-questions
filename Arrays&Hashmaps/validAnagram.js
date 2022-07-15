https://leetcode.com/problems/valid-anagram/submissions/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isAnagram = function(s, t) {
    if(s.length !== t.length) return false;
    
    let sHashMap = {};
    let tHashMap = {};
    for(let i=0; i<s.length; i++){
        sHashMap[s[i]] = sHashMap[s[i]] ? ++sHashMap[s[i]] : 1;
        tHashMap[t[i]] = tHashMap[t[i]] ? ++tHashMap[t[i]] : 1;
    };
    
    for(let char in sHashMap){
        if(sHashMap[char] !== tHashMap[char])
            return false;
    }
    
    return true;
};

isAnagram("aacc","ccac");

// Mistakes done
// added "sHashMap++" instead of "++sHashMap"
// made a wrong validation by sHashMap[s[i]] = sHashMap[s[i]] > 1 ? ++sHashMap[s[i]] : 1; initially