/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */

// This problem can be solved by using stack and in-order traversal.

var kthSmallest = function(root, k) {
    let stack=[]
    while(k--){
        root = moveLeft(root, stack);
        
        if(k===0) return root.val;
        
        root = root.right;
    }
};

function moveLeft (root, stack) {
    while(root !== null) {
        stack.push(root);
        root = root.left;
    }
    
    return stack.pop();
}