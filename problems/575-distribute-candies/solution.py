class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        hash_set = set()
        for i in candies:
            hash_set.add(i)
        return min(len(candies)/2, len(hash_set))