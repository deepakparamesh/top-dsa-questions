This can be solved with Buckt sort.
​
With Bucket sort, we have to Count the value and store in their index.
​
index --
count --
​
But we are going to alter here
​
count --
values -- as array
​
Some Tricks to remember
​
Use prefilled Array, don't use Array.fill() -> this will return an shall copy of array.
​
use Array.from
​
```
let frequency = Array.from({ length: nums.length + 1 }, () => []);
```
​
​