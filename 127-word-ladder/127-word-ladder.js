/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    if (!wordList.includes(endWord)) return 0;
    wordList.push(beginWord);
    let patternMap = {};
    
    for(let word of wordList){
        for(let j=0; j<word.length; j++){
            let pattern = word.slice(0,j) + '*' +word.slice(j+1);
            if(!(pattern in patternMap)) patternMap[pattern] = [];
            patternMap[pattern].push(word);
        }
    }
    
    let wordCount = 1,
        queue = [beginWord],
        visited = [beginWord];
    while (queue.length) {
        const levelSize = queue.length;
        for (let x = 0; x < levelSize; x++) {
            const word = queue.shift();
            if (word === endWord) return wordCount;
            for (let x = 0; x < word.length; x++) {
                const pattern = word.slice(0, x) + '*' + word.slice(x + 1);
                for (let nei of patternMap[pattern]) {
                    if (nei in visited) continue;
                    visited[nei] = true;
                    queue.push(nei);
                }
            }
        }
        wordCount += 1;
    }
    return 0;
};

// hit *it,h*t,hi*
// hot *ot,h*t,ho*
    
// h*t: [hit, hot]

// hit: [hot]
// hot: [hit]




// (5000^2 * 10)
// (5000 * 10^2)