For this problem, we need to use a special datastructure called *"Deque"*
​
So, **Deque store the values in decreasing order.**
​
When you want to store a value in the deque, and if that value is greater than the right most value in the deque, then you have to pop the value in the deque and then insert the value.
​
So the value of deque should always be in the decreasing order.
​
Pseudocode: Monotonically Decreasing Queue
​
Input=[8,7,6,9] k=2
​
Deque [8,7]    Output [8]
Deque [7,6]    Output
​
​
​
​
​
​