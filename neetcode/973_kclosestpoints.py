class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # formula 
        # list of points and their score
        # sort in order
        # choose kth items in the hash map

        def scoreCalc(x,y):
            return (x * x) + (y * y)

        pointsWithScore = []

        for point in points:
            score = scoreCalc(point[0], point[1])
            pointsWithScore.append((score, point))

        pointsWithScore.sort()

        closestPoints = []

        for i in range(k):
            closestPoints.append(pointsWithScore[i][1])
        
        return closestPoints
