This question is a pretty easy one to solve. You just have to know all the edge cases clearly.
​
Given a tree and two nodes, we need to find lowest common ancestors.
​
### Program logic
Initate current = root.
​
Traverse to the left, if both the p and q nodes are smaller than the current
​
Traverse to the right, if both the p and q nodes are bigger than the current
​
otherwise, return the current node.