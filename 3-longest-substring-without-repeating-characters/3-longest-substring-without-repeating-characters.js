// var lengthOfLongestSubstring = function (str) {
//     const hash = {};
//     let start = 0;
//     let max = 0;

//     for (let i = 0; i < str.length; i++) {
//         let rightChar = str[i];

//         if (!(rightChar in hash)) hash[rightChar] = 0;
//         hash[rightChar] += 1;

//         while (hash[rightChar] > 1) {
//             let leftChar = str[start];
//             start += 1;

//             if (leftChar in hash) hash[leftChar] -= 1;
//         }
//         max = Math.max(max, i - start + 1);
//     }
//     return max;
// };

var lengthOfLongestSubstring = function(s) {
    map = new Map()
    l = 0
    res = 0
    
    for (let r=0; r < s.length; r++) {
        
        while (map.has(s[r])) {
            map.delete(s[l])
            l++
        }
    
        map.set(s[r], s[r])
        res = Math.max(res, r-l + 1)
        
    }
    return res
    
};