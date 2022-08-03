/**
 * @param {number} n
 * @return {number}
 */
// var fib = function(n) {
//   let memo = {};
//   if(n in memo) return memo[n];
//   if(n < 2) return n;
//   let result = fib(n-1) + fib(n-2);
//   memo[n] = result;
//   return result;
// };

var fib = function(n) {
  if(n<2) return n;
  let fibNum = [0,1,1]
  for(let i=3; i<=n; i++){
      fibNum[i] = fibNum[i-1] + fibNum[i-2];
  }
  return fibNum[n];
};