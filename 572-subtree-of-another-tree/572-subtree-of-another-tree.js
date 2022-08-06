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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
    let dfs = (node) => {
        if(!node) return false;
        if(isSameTree(node, subRoot)) return true;
        return dfs(node.left) || dfs(node.right);
    }
    
    function isSameTree(p, q){
        if(!p && !q) return true;
        if(!p || !q || p.val !== q.val) return false;
        return (isSameTree(p.left, q.left) && isSameTree(p.right, q.right));
    }
    
    return dfs(root);
};