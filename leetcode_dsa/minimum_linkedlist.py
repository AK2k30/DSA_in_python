class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
      if not points:
          return 0

      # Sort the balloons by their end coordinates
      points.sort(key=lambda x: x[1])

      arrows = 1
      arrowPos = points[0][1]  # Position of the first arrow

      for xStart, xEnd in points:
          if xStart > arrowPos:
              arrows += 1
              arrowPos = xEnd

      return arrows
