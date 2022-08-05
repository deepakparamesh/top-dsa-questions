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
 * @return {number}
 */
var maxPathSum = function(root) {
    let globalMax = -Infinity
    let connectedPathsMax = dfs(root)

    return Math.max(globalMax, connectedPathsMax)
    
    function dfs(node) {
        if (!node) return 0
        
        let left = dfs(node.left)
        let right = dfs(node.right)
	
        globalMax = Math.max(globalMax, node.val, left+node.val, right+node.val, left + right + node.val)
        
		// there might be a bigger solution as we bubble up. 
		// there's only 3 possible paths to return: 
		// the current node val only, node val + the left path or the node val + right path. 
		// you cannot return node + left + right, b/c that would create a split in the path for the recursion.
        return Math.max(node.val, left + node.val, right + node.val)
    }  
};