# import counter class from collections module
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        counter = dict(sorted(counter.items(), key=lambda item: item[1]))

        top_keys = list(counter.keys())

        return top_keys[::-1][:k]

