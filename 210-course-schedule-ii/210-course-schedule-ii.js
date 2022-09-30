/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function (numCourses, prerequisites) {
    let graph = {};
    for(let i=0; i < numCourses; i++) {
        graph[i] = [];
    }
    for(let [course, prerequisite] of prerequisites) {
        graph[course].push(prerequisite);   
    }

    // we are having 2 sets here because the output is expected as an array, If it was set then we could have used the same used the same set as the evaluation element
    const order = [];
    const canComplete = new Set();
    const cycle = new Set();
    function dfs(course) {
        // these are the base conditions
        if(canComplete.has(course)) return true;
        if(cycle.has(course)) return false;
        cycle.add(course);
        
        for(let neighbor of graph[course]){
            if(!dfs(neighbor)) return false;
        }
        canComplete.add(course);
        // we are removing it from cycle because this should be cleared for all the iteration.
        cycle.delete(course);
        order.push(course);
        return true;
    }
    
    // we need to iterate through each element in the given array because there can be multiple distint graphs / which may not be interconnected
    for(let i=0; i<numCourses; i++){
        if(!dfs(i)) {
           return []; 
        }
    }
    return order;
    
};