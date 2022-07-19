/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let hashMap = {};
    for(let word of strs){
        
        let hashKey = new Array(26).fill(0);
        for(let char of word){
            hashKey[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
            hashKey.toString();
        }

        if(!hashMap[hashKey]) hashMap[hashKey] = [];

        hashMap[hashKey].push(word);
    }
    
    let groupAnagrams = [];
    for(let key in hashMap) {
        groupAnagrams.push(hashMap[key]);
    }
    return groupAnagrams;
};