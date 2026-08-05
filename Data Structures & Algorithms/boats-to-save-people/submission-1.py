class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # 3 5 4 3
        # After sort
        # l     r 
        # 3 3 4 5  limit = 5
        people.sort()
        count = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[right] + people[left] <= limit:
                left += 1
            right -= 1
            count += 1
        return count
