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
 * @return {number[]}
 */
var postorderTraversal = function(root) {
    var stack =[];
    function traverse(node){
        if(node){
            traverse(node.left);
            traverse(node.right);
            stack.push(node.val);
        }
    }
    traverse(root);
    return stack;
};