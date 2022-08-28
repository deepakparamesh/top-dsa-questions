/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let hashMap = {};
    let result = [];   
    for(let i=0; i< strs.length; i++){
        let sortedString = strs[i].split('').sort().join('');
        if(!(sortedString in hashMap)){
            hashMap[sortedString] = [];
        }
        hashMap[sortedString].push(strs[i]);
    }
    for(let key in hashMap) {
        result.push(hashMap[key]);
    }  
    return result;
};