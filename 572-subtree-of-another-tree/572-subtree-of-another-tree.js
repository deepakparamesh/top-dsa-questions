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
    return dfs(root);
};

function isSameTree(p, q){
    // check if both nodes are not null
    if(!p && !q) return true;
    // check the structure and value of the nodes.
    if(!p || !q || p.val !== q.val) return false;
    // do it for both left and right
    return (isSameTree(p.left, q.left) && isSameTree(p.right, q.right));
}