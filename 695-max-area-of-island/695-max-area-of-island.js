/**
 * @param {number[][]} grid
 * @return {number}
 */

// function findArea(grid, row, column) {
//     let area = 0;
//     if(row < 0 || row >= grid.length ||
//        column < 0 || column >= grid[row].length ||
//        grid[row][column] === 0)
//     {
//         return;
//     } else {
//         area += 1;
//     }
    
//     grid[row][column] = 0;
//     findArea(grid, row+1, column);
//     findArea(grid, row-1, column);
//     findArea(grid, row, column-1);
//     findArea(grid, row, column+1);
//     return area;
// }


// var maxAreaOfIsland = function(grid) {
//     if(!grid.length) return 0;
//     let maxArea = 0;
    
//     for(let i=0; i<grid.length; i++){
//         for(let j=0; j<grid[i].length;j++){
//             if(grid[i][j] === 1) {
//                let area = findArea(grid, i, j);
//                Math.max(area, maxArea);
//             }
//         }
//     }
    
//     return maxArea;
// };

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
    function find(x, y) {
        if (grid[y] === undefined || grid[y][x] === undefined) {
            return 0;
        }

        if (grid[y][x] === 0) {
            return 0;
        }

        grid[y][x] = 0;

        let square = 1;

        square += find(x + 1, y);
        square += find(x - 1, y);
        square += find(x, y + 1);
        square += find(x, y - 1);

        return square;
    }

    let max = 0;

    for (let y = 0; y < grid.length; y++) {
        for (let x = 0; x < grid[0].length; x++) {
            max = Math.max(max, find(x, y));
        }
    }

    return max;
};