You can do by sorting the number and finding the longest sequence.
​
Now, the question is how do we do it with sorting.
​
1. Find if the previous number of the given number is there.
2. Continue only if it is there.
3. have the currentMax as 1 and then add that with the current number until a consecutive number is not found.
4. check if the currentMax > max if so then replace.
5. return max