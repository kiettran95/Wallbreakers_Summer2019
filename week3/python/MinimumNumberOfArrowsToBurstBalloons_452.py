class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        sorted_points = sorted(points, key=lambda x:x[1])
        count = 1
        last_end = sorted_points[0][1]
        for point in sorted_points:
            if point[0] > last_end:
                last_end = point[1]
                count += 1
                
        return count
