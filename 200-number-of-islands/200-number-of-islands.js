/**
 * @param {character[][]} grid
 * @return {number}
 */

function dfs(grid, row, col) {
    if(row < 0 || row >= grid.length ||
       col < 0 || col >= grid[row].length ||
       grid[row][col] === "0") {
        return ;
    }    
    
    grid[row][col] = "0";
    dfs(grid, row-1, col);
    dfs(grid, row+1, col);
    dfs(grid, row, col-1);
    dfs(grid, row, col+1);
}

var numIslands = function (grid) {
    if(!grid.length) return 0;
    
    let islands = 0;
    
    for(let i=0; i< grid.length ; i++) {
        for(let j=0; j< grid[i].length; j++){
            if(grid[i][j] === "1"){
                islands += 1;
                dfs(grid, i, j);
            }
        }
    }
    return islands;
    
    
};