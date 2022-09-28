/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
     // We define our two pointers which will indicate a buying and a selling.
    let left = 0;
    let right = 1;
    let profit = 0;
    
    // We run while the right pointer didn't reach the end of the prices array.
    while(right < prices.length) {
        
        // If the right price is bigger than the left, we need to add it to the profit, because we want to calculate the profit whenever our selling is bigger than the buying.
        if(prices[right] > prices[left]) {
            profit += prices[right] - prices[left];
        }
        
        // We of course increment the two pointers and move forward with our checking and calculation. 
        left++;
        right++;
    }
    
    return profit;
};