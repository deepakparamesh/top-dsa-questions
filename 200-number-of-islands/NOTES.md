This problem has two approach of solving.
1. By making the visited element as "0"
2. By adding the visited element in the visited set.
​
Here I have used visited element
​
Made  a mistake in the condition. I had not put grid[0]
if(row < 0 || row >= grid.length ||
col < 0 || col >= grid[0].length ||
grid[row][col] === "0") {
return ;
}