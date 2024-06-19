class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        fruit_count = {}
        
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            
            fruit = fruits[right]
            
            if fruit in fruit_count:
                fruit_count[fruit] +=1
            else:
                fruit_count[fruit] = 1
            
            while len(fruit_count) > 2:
                leftFruit = fruits[left]
                fruit_count[leftFruit] -=1
                if fruit_count[leftFruit] == 0:
                    del fruit_count[leftFruit]
                
                left +=1
            
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits