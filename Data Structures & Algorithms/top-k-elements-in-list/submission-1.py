class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        nums.sort()

        for i in range(len(nums)):
            if nums[i] in freq.keys():
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1


        sortedFreq = dict(sorted(freq.items(), key=lambda x: x[1], reverse = True))
        return list(sortedFreq)[:k]
