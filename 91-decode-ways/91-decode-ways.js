/**
 * @param {string} s
 * @return {number}
 */

// this is bottom up approach
var numDecodings = (str, index = 0, memo = new Map()) => {
    
    const helper = (data, k, memo) => {
        const idx = data.length - k
        if (data[idx] === '0') return 0
        if (k === 0) return 1
        

        if (memo.has(k)) return memo.get(k)
        
        let result = helper(data, k - 1, memo)
        
        const isAlphabetical = Number(data.substring(idx, idx + 2)) <= 26
        if (k >= 2 && isAlphabetical) result += helper(data, k - 2, memo)
        
        memo.set(k, result)
        return result
    }
    
    // this is bottom up approach, we are passing the length and decreasing the length
    return helper(str, str.length, new Map());
}