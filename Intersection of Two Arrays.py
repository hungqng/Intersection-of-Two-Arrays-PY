# 349. Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2)) # Python set operation

        # Solution 2 brute force
        # res = []
        # for i in nums1:
        #     if i not in res and i in nums2:
        #         res.append(i)

        # return res