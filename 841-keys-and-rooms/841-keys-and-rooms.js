/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function(rooms) {
    let visited = {0:"true"};
    let stack =[0];
    while(stack.length){
        let keys = rooms[stack.pop()];
        for(let key of keys){
            if(!(key in visited)) {
                visited[key] = true;
                stack.push(key);
            }
        }
    }

    return Object.keys(visited).length === rooms.length;
};