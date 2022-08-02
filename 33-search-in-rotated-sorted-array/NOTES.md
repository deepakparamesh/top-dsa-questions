check if we are in the left sorted portion or in the right sorted portion.
if(left<middle) it is left sorted
else it is right sorted
​
check if middle == target
if yes return target.
check if the middle <= left .
If yes, then we are in the left sorted portion.
Then check if the target <= to the left .
If yes, then shift the left to current middle+1 and re-calculate the middle.
If no, then shift the right to current middle-1 and re-calculate the middle.
If no, then we are in the right sorted portion.
Then check if the target value is >= to the right most value.
asdflkj;l