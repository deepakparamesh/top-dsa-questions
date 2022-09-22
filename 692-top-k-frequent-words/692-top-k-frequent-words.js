/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
var topKFrequent = function(words, k) {
    const mappings = {}
    for (let i = 0; i < words.length; i++) {
        mappings[words[i]] = mappings[words[i]] + 1 || 1
    }
    const sorted = Object.keys(mappings).sort((a, b) => {
        if(mappings[b] === mappings[a]) {
            return a > b ? 1 : -1
        }
        return mappings[b] - mappings[a];
    })
    return sorted.slice(0, k)
};