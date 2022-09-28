/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice1 = Infinity;
    let profit1 = 0;
    let minPrice2 = Infinity;
    let profit2 = 0;
    for(let i=0; i<prices.length; i++) {
        minPrice1 =  Math.min(prices[i], minPrice1);
        profit1 = Math.max(profit1, prices[i] - minPrice1);
        minPrice2 = Math.min(minPrice2, prices[i]-profit1);
        profit2 = Math.max(profit2, prices[i]-minPrice2);
    }
    return profit2;
};