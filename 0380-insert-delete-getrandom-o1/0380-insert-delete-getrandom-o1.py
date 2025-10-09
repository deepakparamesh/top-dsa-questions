class RandomizedSet:

    def __init__(self):
        self.values = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        
        if val in self.val_to_index:
            return False
        
        self.values.append(val)

        self.val_to_index[val] = len(self.values)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        
        index_to_remove = self.val_to_index[val]
        last_element= self.values[-1]

        self.values[index_to_remove] = last_element
        self.val_to_index[last_element] = index_to_remove

        self.values.pop()

        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:

        return random.choice(self.values)
# Array:O(1) getRandom()
# HashMap: O(1) lookup insert/remove

# [Val1, Val2, Val3]
# {val1:0,val2:1, val3:2}

# []        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()