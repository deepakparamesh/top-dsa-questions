Sort the Array to avoid pushing the duplicate triplets and take advantage of the sorted array.
​
The for loop should run till **** i < nums.length-1****
​
**sanity test 1**, the first element in the array should not be > 0 because there is no point in adding the numbers which will not give 0.
​
**Sanity Test 2**, the **current element should not be the same as prev elemen**t, this is to avoid the duplication, **Hence skip.**
​
**Run a Two sum under the for loop with two pointer method**.
​