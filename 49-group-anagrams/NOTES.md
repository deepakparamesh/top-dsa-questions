```
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
```
So this Approach is costing us. O(n2logn) since there is sorting.
​
​
**But in order to reduce it to O(n2)**
​
They say that strs[i] consists of lowercase English letters only.
​
So let's take advantage of this.
​
Let's create a hashKey as 26 character number as string. and the value as array of strings given.
​
We will have to use  "c".charCodeAt(index) to find the character code and use it as string.
​
```
let hashKey = new Array(26).fill(0);
for(let char of strs[i]) {
hashKey[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
hashKey.toString();
}
```
​
​
This is going to be life saver here.
​
This will cost us
Time: O(m*n*26)
Space: O(26)