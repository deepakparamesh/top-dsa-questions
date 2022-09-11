/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let max = 0;
    let [left, right] = [0,1]; 

    while(right <= prices.length-1){
        if(prices[left] < prices[right]){
            let latestProfit = prices[right] - prices[left];
            max = Math.max(max, latestProfit);
        } else {
            left = right;
        }
        right++
    }
    return max;
}