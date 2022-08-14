class Drains {
    constructor(west = false, east = false) {
        this.west = west;
        this.east = east;
    }
}

/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
function pacificAtlantic(heights) {
    const rowLen = heights.length;
    const colLen = heights[0].length;
    const lastRow = rowLen - 1;
    const lastCol = colLen - 1;
    const drainage = new Array(rowLen);
    const drainsBoth = [];

    for (let r = 0; r < rowLen; ++r) {
        drainage[r] = new Array(colLen);
        for (let c = 0; c < colLen; ++c) {
            drainage[r][c] = new Drains();
        }
    }

    for (let r = 0; r < rowLen; ++r) {
        markDrainage(r, 0, true);
        markDrainage(r, lastCol);
    }
    for (let c = 0; c < colLen; ++c) {
        markDrainage(0, c, true);
        markDrainage(lastRow, c);
    }

    return drainsBoth;

    /**
     * @param {number} r
     * @param {number} c
     * @param {boolean=} west = `false`
     * @param {number=} prev = `-Infinity`
     * @return {void}
     */
    function markDrainage(r, c, west = false, prev = -Infinity) {
        if (
            !inBounds(r, c) ||
            heights[r][c] < prev ||
            (west && drainage[r][c].west) ||
            (!west && drainage[r][c].east)
        ) {
            return;
        }

        const drains = drainage[r][c];
        const height = heights[r][c];

        if (west) {
            drains.west = true;
        } else {
            drains.east = true;
        }

        if (drains.west && drains.east) {
            drainsBoth.push([r, c]);
        }

        markDrainage(r - 1, c, west, height);
        markDrainage(r + 1, c, west, height);
        markDrainage(r, c - 1, west, height);
        markDrainage(r, c + 1, west, height);
    }

    /**
     * @param {number} r
     * @param {number} c
     * @return {boolean}
     */
    function inBounds(r, c) {
        return r >= 0 && c >= 0 && r < rowLen && c < colLen;
    }
}