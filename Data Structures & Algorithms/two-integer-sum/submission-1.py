class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = []
        for i, num in enumerate(nums):
            sortedNums.append([num, i])

        sortedNums.sort()

        i,j = 0, len(sortedNums) - 1
        while i < j:
            currSum = sortedNums[i][0] + sortedNums[j][0]
            if currSum == target:
                return [min(sortedNums[i][1], sortedNums[j][1]),max(sortedNums[i][1], sortedNums[j][1])]
            elif currSum < target:
                i += 1;
            else:
                j -= 1;
        return []    
