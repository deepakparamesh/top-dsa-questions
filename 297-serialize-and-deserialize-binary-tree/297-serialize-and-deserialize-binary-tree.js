/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    let data = []
    function dfs(node) {
        if(!node) {
            data.push("N")
            return;
        }
        
        data.push(JSON.stringify(node.val));
        
        dfs(node.left);
        dfs(node.right);
        
    }
    dfs(root);
    return data.toString();
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    vals = data.split(",");
    let i = 0;
    
    function dfs(){
        if(vals[i] == "N") {
            i +=1;
            return null;   
        }
        let node = new TreeNode(parseInt(vals[i]))
        i+=1;
        node.left = dfs();
        node.right = dfs();
        return node;
    }
    return dfs();
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */