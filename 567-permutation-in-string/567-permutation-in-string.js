/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = (s1, s2) => {
    if (s2.length < s1.length) return false;
    
    let [ left, right ] = [ 0, 0 ];
    const [ s1FrequencyMap, s2FrequencyMap ] = getFrequencyMaps(s1);
    
    while (right < s2.length) {
        addRightFrequency(s2, right, s2FrequencyMap);

        const window = (right - left) + 1;
        const isPermutation = (window === s1.length) && isSame(s1FrequencyMap, s2FrequencyMap);
        if (isPermutation) return true;

        const canSlide = s1.length <= window;
        if (canSlide) {
            subtractLeftFrequency(s2, left, s2FrequencyMap);
            left++;
        }
        
        right++;
    }
    
    return false;
}

const getFrequencyMaps = (s1) => {
    const [ s1FrequencyMap, s2FrequencyMap ] = new Array(2)
        .fill().map(() => new Array(26).fill(0))

    for (const char of s1) s1FrequencyMap[getCode(char)]++;

    return [ s1FrequencyMap, s2FrequencyMap ]
}


const getCode = (char) => char.charCodeAt(0) - 'a'.charCodeAt(0);

const addRightFrequency = (s, right, frequencyMap) => {
    const char = s[right];
    const index = getCode(char);

    frequencyMap[index]++;
    
    return frequencyMap[index];
}

const subtractLeftFrequency = (s, left, frequencyMap) => {
    const char = s[left];
    const index = getCode(char);

    frequencyMap[index]--;
    
    return frequencyMap[index];
}

const isSame = (a, b) => {
    for (let i = 0; i < 26; i++) {
        const isMatch = a[i] === b[i];
        if (!isMatch) return false
    }
    
    return true;
}