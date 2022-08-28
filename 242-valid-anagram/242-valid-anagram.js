/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length !== t.length) return false;
    let sHash = {};
    let tHash = {};
    for(let i=0; i<s.length; i++) {
        sHash[s[i]] = sHash[s[i]] ? sHash[s[i]] += 1 : 1;
        tHash[t[i]] = tHash[t[i]] ? tHash[t[i]] += 1 : 1;
    }
    for(let char in sHash) {
        if(sHash[char] !== tHash[char]) {
            return false;
        }
    }
    return true;
};