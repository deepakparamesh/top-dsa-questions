class AllOne:

    # HashMap<String, Integer> counts


    class Bucket:

        def __init__(self, count):
            self.count = count
            self.strings = set()
            self.prev =None
            self.next = None
        

    def __init__(self):
        self.string_count = {}
        self.count_bucket = {}
        self.head = self.Bucket(float('-inf'))
        self.tail = self.Bucket(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head


    def inc(self, key: str) -> None:
        # counts[key] = counts.get(key,0)+1
        if key in self.string_count:
            self._change_count(key,1)
        else:
            self.string_count[key]=1

            if 1 not in self.count_bucket:
                new_bucket = self.Bucket(1)
                self._insert_bucket_after(new_bucket, self.head)
                self.count_bucket[1] = new_bucket
            
            self.count_bucket[1].strings.add(key)



    def dec(self, key: str) -> None:
        # counts[key] -= 1
        # if counts[key] ==0:
            # remove key
        self._change_count(key, -1)

    def getMaxKey(self) -> str:
        # iterate all entries, find max count -> O(n)
        if self.tail.prev == self.head:
            return ""
        
        return next(iter(self.tail.prev.strings))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""

        return next(iter(self.head.next.strings))
    
    def _change_count(self, key: str, delta: int) -> None:
        old_count = self.string_count[key]
        new_count = old_count + delta

        if new_count == 0:
            del self.string_count[key]
        else:
            self.string_count[key] = new_count
        
        old_bucket = self.count_bucket[old_count]

        if new_count > 0:
            if new_count not in self.count_bucket:
                new_bucket = self.Bucket(new_count)
                if delta == 1:
                    self._insert_bucket_after(new_bucket, old_bucket)
                else:
                    self._insert_bucket_after(new_bucket, old_bucket.prev)
                
                self.count_bucket[new_count] = new_bucket
            
            self.count_bucket[new_count].strings.add(key)
        
        old_bucket.strings.remove(key)

        if not old_bucket.strings:
            self._remove_bucket(old_bucket)
            del self.count_bucket[old_count]
    
    def _insert_bucket_after(self, new_bucket, prev_bucket):
        new_bucket.prev = prev_bucket
        new_bucket.next = prev_bucket.next
        prev_bucket.next.prev = new_bucket
        prev_bucket.next = new_bucket
    
    def _remove_bucket(self, bucket):
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# [head] <> [Count:1, Strings:{...}] <> [Count:2, Strings]

# Hashmaps:
# stringCount: {hello:2}
# countBucket: {1: BucketNode1, 2: BucketNode2}



