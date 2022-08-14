/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
// var canFinish = function(numCourses, prerequisites) {
    
//     // prepare the adjacency list
//     let preMap = {};
//     for(let i=0; i<numCourses; i++){
//         preMap[i] = [];
//     }
//     for(let pair of prerequisites){
//         let [course, prerequisite] = pair;
//         preMap[course].push(prerequisite);
//     }
    
//     let visitedSet = new Set();
    
//     let dfs = (course) =>{
//         if(visitedSet.has(course)) return false;
//         if(preMap[course] == []) return true;
        
//         visitedSet.add(course);
        
//         for(let pre of preMap[course]){
//             if(!dfs(pre)) return false;
//             visitedSet.remove(course);
//             preMap[course] = [];
//             return true;
//         }
//     }
    
//     for(let course=0; course < numCourses.length; course++){
//         if(!dfs(course)){
//             return false;
//         }
//         return true;
//     }
// };


function createGraph(numCourses, edges) {
    const graph = Array.from({ length: numCourses }, () => []);

    for (let edge of edges) {
        let [a, b] = edge;

        if (!(a in graph)) graph[a] = [];
        if (!(b in graph)) graph[b] = [];

        graph[a].push(b);
    }
    return graph;
}

function canFinish(numCourses, preq) {
    const graph = createGraph(numCourses, preq);
    let seen = new Set();
    let seeing = new Set();

    function explore(course) {
        if (seen.has(course)) return true;
        if (seeing.has(course)) return false;

        seeing.add(course);
        for (let neighbor of graph[course]) {
            if (!explore(neighbor)) return false;
        }

        seen.add(course);
        seeing.delete(course);
        return true;
    }

    for (let i = 0; i < numCourses; i++) {
        if (!explore(i)) return false;
    }
    return true;
}