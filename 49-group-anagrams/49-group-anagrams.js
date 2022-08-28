/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    
    // Version 1 which will cost us O(m*nlogn)
    // let hashMap = {};
    // let result = [];   
    // for(let i=0; i< strs.length; i++){
    //     let sortedString = strs[i].split('').sort().join('');
    //     if(!(sortedString in hashMap)){
    //         hashMap[sortedString] = [];
    //     }
    //     hashMap[sortedString].push(strs[i]);
    // }
    // for(let key in hashMap) {
    //     result.push(hashMap[key]);
    // }  
    // return result;
    
    let hashMap = {};
    let result = [];   
    for(let i=0; i< strs.length; i++){
        let hashKey = new Array(26).fill(0);
        for(let char of strs[i]) {
            hashKey[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
            hashKey.toString();
        }
        if(!(hashKey in hashMap)) hashMap[hashKey] = [];
        hashMap[hashKey].push(strs[i]);
    }
    for(let key in hashMap) {
        result.push(hashMap[key]);
    }  
    return result;
};