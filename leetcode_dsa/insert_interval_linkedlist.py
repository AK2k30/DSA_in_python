class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      result = []
      i = 0

      # Step 2: Add all intervals ending before newInterval starts
      while i < len(intervals) and intervals[i][1] < newInterval[0]:
          result.append(intervals[i])
          i += 1

      # Step 3: Merge overlapping intervals with newInterval
      while i < len(intervals) and intervals[i][0] <= newInterval[1]:
          newInterval[0] = min(newInterval[0], intervals[i][0])
          newInterval[1] = max(newInterval[1], intervals[i][1])
          i += 1

      # Step 4: Add the merged newInterval
      result.append(newInterval)

      # Step 5: Add remaining intervals
      while i < len(intervals):
          result.append(intervals[i])
          i += 1

      return result
