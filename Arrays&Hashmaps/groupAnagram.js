//////////////////////////////////////////////////////////////////////////////
// Hash Each Word
// Time: O(n*max(w))
// Space: O(n*max(w))
// This solution is faster than sorting each word.
//////////////////////////////////////////////////////////////////////////////

/** @const {!Object<string, number>} */
const CODES = {
    a: 0, b: 1, c: 2, d: 3, e: 4, f: 5, g: 6, h: 7, i: 8, j: 9,
    k: 10, l: 11, m: 12, n: 13, o: 14, p: 15, q: 16, r: 17,
    s: 18, t: 19, u: 20, v: 21, w: 22, x: 23, y: 24, z: 25
};

/**
 * @param {string[]} words
 * @return {string[][]}
 */
function groupAnagrams(words) {
    
    const map = Object.create(null);
    for (const word of words) {
        const hashKey = createHashKey(word);
        if (!(hashKey in map)) {
            map[hashKey] = [];
        }
        map[hashKey].push(word);
    }
    
    const groups = [];
    for (const key in map) {
        groups.push(map[key]);
    }
    return groups;
}

/**
 * @param {string} word
 * @return {string}
 */
function createHashKey(word) {
    const hashKey = new Array(26).fill(0);
    for (const ch of word) {
        ++hashKey[CODES[ch]];
    }
    return hashKey.toString();
}



// With out helper function and using the constants
function groupAnagramsTwo(words){
    let hashMap = {};
    for(let word of words){
        
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
}



groupAnagramsTwo(["eat","tea","tan","ate","nat","bat"]);

// hashMap = {
//     "1,0,0,0,0,1,0,0,1"  : ["eat", "tea"],
//     ""
// }

// O(n * m);

// [1,0,0,0,1,0,0,0,0,0,0,0,1] => "1,0,0,0,0,1,0,0,"
