/**
 * @param {number[]} nums
 * @return {number}
 */
// var pivotIndex = function(nums) {
//     let leftSum =0;
    
//     let sum = nums.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    
//     for(let i=0; i < nums.length; i++) {
//         // if(i >= nums.length) return -1;

//         rightSum = sum - nums[i];
        
//         if(leftSum == rightSum) return i;
        
//         leftSum += nums[i];
//     }
//     return -1;
// };

// var pivotIndex = function(arr){
//     const sum = arr.reduce((r, n) => r + n, 0);
//     let left = 0;
//     for (let i = 0; i < arr.length; i++) {
//         const right = sum - left - arr[i];
//         if (left === right)return i;
//         left += arr[i];
//     }
//     return -1;
// }

// var pivotIndex = function(nums) {
//     let sum = 0;
//     let sumsFromLeft = nums.map(x =>{
//     	sum+=x;
//     	return x;
//     });
//     for(let i=1, len = nums.length; i<len; i++){
//     	if(2*sumsFromLeft[i]===sum-nums[i]) return i;
//     }
//     return -1;
// };

// var pivotIndex = function(nums) {
//     let sum = nums.reduce((a,b)=>a+b, 0);
//     let sumL = 0;
//     for(let i=0, len=nums.length; i<len; i++){
//     	if(sumL === (sum-nums[i])/2) return i;
//     	sumL += nums[i];
//     }
//     return -1;
// };

var pivotIndex = function(nums) {
    let sum = nums.reduce((a,b)=>a+b, 0);
    let sumL = 0, sumR = sum;
    for(let i=0, len=nums.length; i<len; i++){
        sumR -= nums[i];
    	if(sumL === sumR) return i;
    	sumL += nums[i];
    }
    return -1;
};

// [1,7,3,6,5,6]

// Declare Two variable as leftSum and RightSum
// Start the pivot index from the middle of the array.
// Check if the sum of the values to the left of the array equals right of the array
// If yes, return the index of the array.
// If left value is higher, move the pivot towards left.
// If right value is higher, move the pivot towards right.
// repeat the same process until left and right value is equal,
// If the pivot goes out of bound, return -1.