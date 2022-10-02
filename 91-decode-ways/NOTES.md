Clarifications / doubts :
​
Edge cases :  string starting with "0" is an invalid string
empty string should
Brute force approach :   If the given string passes all the edge cases then it means that we have Two decisions to take.
​
Example :
​
​
​
​
​
​
Conditions we have to consider :
If we are taking single digit that should be within the range 1-9
If we are taking double digit then,
we should take the first number should be either (1 || 2) and
the second digit should be within (0 - 6)
If the starts with "0" then the whole string is invalid
​
Time Complexity : 2^n
​
​
​
​
Optimal approach :     we can use an DP hashMap to memoize the value of each index and run a dfs. This will cost us only
TimeComplexity : O(n)
SpaceComplexity : O(n)
There is an approach to use two variables and make the space complexity as O(1)