/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  // 0 unvisited
  // 1 processing
  // 2 processed || canComplete
  const graph = new Map();
  const status = new Array(numCourses).fill(0);
  for (let [course, dependency] of prerequisites)
    graph.set(course, (graph.get(course) || new Set()).add(dependency));
    
    // the reason why we are traversing in this way is we can have distinct courses.
    for(let i=0; i<numCourses; i++){
        if(status[i] == 0) {
            if(isCyclic(graph, status, i)) {
                return false;
            }
        }
    }
    
    return true;
    
    function isCyclic(graph, status, index) {
        if(status[index] == 1) return true;
        status[index] = 1;
        let neighbors = graph.get(index) || [];
        for(let neighbor of neighbors) {
            if(status[neighbor] != 2) {
                if(isCyclic(graph, status, neighbor)) return true;
            }
        }
        status[index] = 2;
        return false;   
    }
};


// function canFinish(numCourses, prerequisites) {
//   const seen = new Set();
//   const seeing = new Set();
//   const adj = [...Array(numCourses)].map(r => []);
  
//   for (let [u, v] of prerequisites) {
//     adj[v].push(u);
//   }
  
//   for (let c = 0; c < numCourses; c++) {
//     if (!dfs(c)) {
//       return false;
//     }
//   }
//   return true;
  
//   function dfs(v) {
//     if (seen.has(v)) return true;
//     if (seeing.has(v)) return false;
    
//     seeing.add(v);
//     for (let nv of adj[v]) {
//       if (!dfs(nv)) {
//         return false;
//       }
//     }
//     seeing.delete(v);
//     seen.add(v);
//     return true;
//   }
// }