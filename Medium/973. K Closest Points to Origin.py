"""
https://leetcode.com/problems/k-closest-points-to-origin/

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
"""

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
      
        pointsDict = defaultdict(list)
        distanceHeap = []
        heapify(distanceHeap)
        
        for x,y in points:
            distance = x**2 + y**2
            heappush(distanceHeap, distance)
            pointsDict[distance].append([x,y])
            
        result = []
        for i in range(K):
            key = heappop(distanceHeap)
            result += pointsDict[key]
        
        return result[:K]