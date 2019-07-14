class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        sorted_intervals = sorted(intervals, key=lambda interval:interval[0])
        start,end = sorted_intervals[0]
        result = list()

        for interval in sorted_intervals:
            if interval[0] > end:
                
                result.append([start,end])
                start,end = interval
                print(result)
            else:
                end = max(end,interval[1]) if interval[1]>end else end
                      
        # add last interval or the only interval
        result.append([start,end])
        return result
            
