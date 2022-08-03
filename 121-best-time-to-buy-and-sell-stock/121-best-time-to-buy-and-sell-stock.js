/**
 * @param {number[]} prices
 * @return {number}
 */
// var maxProfit = function(prices) {
//     let max = 0;
//     for(let i=0; i<=prices.length-2; i++){
//         let profit = prices[i+1] - prices[i];
//         if(profit > max) max = profit;
//     }
//     return max;
// };

var maxProfit = function(prices){
    let max =0;
    
    let i=0; let j=1;
    let profit = prices[j] - prices[i];
    while(i <= prices.length-2){
        if(profit > max) max = profit;    
        if(profit < 0){
            profit = 0;
            i++;
        }
        j++;
    }
}

// var maxProfit = function(prices) {
//     let max = 0;
//     let left = 0; 
//     let right = 1;

//     while(right <= prices.length-1){
//         if(prices[left] > prices[right]) left++; right++;
        
//         let latestProfit = prices[right] - prices[left];
//         if(latestProfit > max) {
//             max = latestProfit;
//             right++;
//         }
//     }
//     return max;
// }

var maxProfit = function(prices) {
    let max = 0;
    let left = 0; 
    let right = 1;

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