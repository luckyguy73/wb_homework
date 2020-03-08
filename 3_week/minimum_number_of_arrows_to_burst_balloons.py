class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points: return 0
        points.sort(key=lambda x: x[1])
        arrowPos = points[0][1]
        arrowCnt = 1
        for i in range(1, len(points)):
            if arrowPos >= points[i][0]:
                continue;
            arrowCnt += 1
            arrowPos = points[i][1]
        return arrowCnt
