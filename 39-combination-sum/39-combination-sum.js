function combinationSum(candidates, target) {
    
    let result = [];
    
    function dfs(index, current, total){
        if(total == target){
            result.push(current.slice())
            return;
        }
        if(total > target || index >= candidates.length) return;
        
        current.push(candidates[index]);
        dfs(index, current, total+candidates[index]);
        current.pop();
        dfs(index+1, current, total);
    }
    dfs(0,[],0);
    return result;
}