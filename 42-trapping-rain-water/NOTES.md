The whole problem can be solved by this formulat
​
** area = Math.min(maxLeft, maxRight) - height[left/right] **
​
### The pseudocode is
​
preset the maxLeft, maxRight with the initial value of height[left], height[right]
​
```
while(left < right) {
calculateMax
if left is min or same move left else move right
calculate the area, if area is > 0 keep as it is or assign 0
}
```