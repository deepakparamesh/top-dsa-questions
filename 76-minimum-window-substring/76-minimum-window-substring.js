/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    let map1 = new Map(), map2 = new Map(), left = 0, maxMatchedString = '', matches = 0, maxLen = Number.MAX_SAFE_INTEGER;
    
    if (t.length > s.length || t == "") { return ""; }
    
    for (let i = 0; i < t.length; i++) {
        map1.has(t[i]) ? map1.set(t[i], map1.get(t[i])+1) : map1.set(t[i], 0);
    }
    
    for(let right = 0; right < s.length; right++) {
        let end = s[right]
        if(map1.has(end)) {
            map2.has(end) ? map2.set(end, map2.get(end)+1) : map2.set(end, 0);
            if (map1.get(end) == map2.get(end)) { matches++ }
        }
                
        while(matches == map1.size) {
            if(maxLen > (right - left + 1)) {
                maxLen = (right - left + 1); 
                maxMatchedString = s.substring(left, right+1);
            } 
            if(map1.has(s[left])) {
                map2.set(s[left], map2.get(s[left])-1); 
                if (map2.get(s[left]) < map1.get(s[left])) { matches-- }
            }
            left++;
        }
    }
    return maxMatchedString;
};