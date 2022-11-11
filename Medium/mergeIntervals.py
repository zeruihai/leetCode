class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key=lambda x: x[0])
        print(intervals,"\n")
        length=len(intervals)
        i = 0
        while i!=length-1 and length != 1:

            
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i][1]<intervals[i+1][1]:
                    intervals[i] = [intervals[i][0],intervals[i+1][1]]
                    intervals.pop(i+1)
                    length = len(intervals)
                else:
                    intervals.pop(i+1)
                    length = len(intervals)
                    
                
            else:
                i+=1
        


        return intervals