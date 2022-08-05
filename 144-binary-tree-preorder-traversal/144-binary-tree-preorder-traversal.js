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
var preorderTraversal = function(root) {
    var stack =[];
    function traverse(node){
        if(node){
            stack.push(node.val);
            traverse(node.left);
            traverse(node.right);   
        }
    }
    traverse(root);
    return stack;
};