Multiplying with the postfix is the important catch here.
​
You will have to multiply with the output[i]
and then multiply with postfix
​
```
let postFix = 1;
for(let i=nums.length-1; i>=0 ; i--){
output[i] *= postFix;
postFix *= nums[i];
}
```