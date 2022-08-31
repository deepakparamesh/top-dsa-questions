/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
//     let count = {};
//     let result = [];
//     // let frequency = new Array(nums.length).fill([]);
//     let frequency = Array.from({ length: nums.length + 1 }, () => []);
    
    
//     for(let num of nums){
//         if(!count[num]) count[num] = 0;
//         count[num] += 1;
//     }
    
//     for(let key in count) {
//         // if(!frequency[count[key]]) frequency[count[key]] = [];
//         frequency[count[key]].push(key);
//     }
    
//     for(let i=nums.length-1; i>=0; i--) {
//         if(frequency[i].length > 0){
//             frequency[i].forEach((elem) => result.push[elem]);
//             if(k == result.length){
//                 return res;
//             }
//         }
//     }
    
    let map = {};
    let res = [];
    let bucket = Array.from({ length: nums.length + 1 }, () => []); // to create unique arrays

    // storing frequency of numbers in a map
    for (const n of nums) {
        map[n] = (n in map) ? 1 + map[n] : 1;
    }

    // Populate the bucket with numbers in frequency
    // as the index of the bucket
    for(const c in map){
        bucket[map[c]].push(c);
    }
    
    for (let i = bucket.length - 1; i >= 0; i--) {
        if (bucket[i].length > 0) {
            bucket[i].forEach((elem)=> res.push(elem));
            if(k == res.length){
                return res;
            }
        }
    }
    
};