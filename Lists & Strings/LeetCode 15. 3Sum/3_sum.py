class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        triples = set()
        
        for i in range(len(nums) - 2):
            # Assume elemtnt i is inside our triple
            curr = nums[i]
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                sec = nums[j]
                third = nums[k]
                
                if (curr + sec + third == 0):
                    triples.add((curr, sec, third))
                    j += 1
                    k -= 1
                elif curr + sec + third < 0:
                    j += 1
                else:
                    k -= 1
        
        return [list(el) for el in triples]


solution = Solution()

assert [[-1, -1, 2], [-1, 0, 1]] == solution.threeSum([-1, 0, 1, 2, -1, -4])
