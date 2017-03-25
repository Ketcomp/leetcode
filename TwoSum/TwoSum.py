# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    """
    Store all numbers in a hashmap with the number as the key and their index as the value.
    For each number 'i' in the list, check if 'i-target' exists in the hashmap and return their indices.
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i, num in enumerate(nums):
            if num in hmap:
                return [hmap[num], i]
            else:
                hmap[target - num] = i

if __name__ == '__main__':
    print(Solution.twoSum('',[2,3,44,2,3,4,56,78,21],58))