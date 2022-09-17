/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
function dfs(board, i, j, remain) {
    if (remain === '') return true;
    // i < 0 and i >= board.length is for find the row out of bound
    // j < 0 and j >= board[0].length is to find the column out of bound
    if (i < 0 || i >= board.length || j < 0 || j >= board[0].length)
        return false;
    if (board[i][j] !== remain[0]) return false;

    let temp = board[i][j];
    board[i][j] = '-';

    let result =
        dfs(board, i - 1, j, remain.slice(1)) || // top
        dfs(board, i + 1, j, remain.slice(1)) || // bottom
        dfs(board, i, j - 1, remain.slice(1)) || // left
        dfs(board, i, j + 1, remain.slice(1));   // right

    board[i][j] = temp;
    return result;
}

var exist = function (board, word) {
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (dfs(board, i, j, word)) {
                return true;
            }
        }
    }
    return false;
};