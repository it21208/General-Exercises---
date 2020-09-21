class Circle:

    def __init__(self, centre, R):
        self.centre = centre
        self.R = R
    
    def contains(self, simio):
        if (simio.getX > self.centre.getX - self.R) and (simio.getX < self.centre.getX + self.R) and (simio.getY > self.centre.getY - self.R) and (simio.getY < self.centre.getY + self.R):
            return(True)
        else:
            return(False)


    def __str__(self):
        return('Circle has R=', self.R, ' and center point=', self.centre)

    def intersects(self, other):
        x1 = self.centre.getX
        y1 = self.centre.getY
        x2 = other.centre.getX
        y2 = other.centre.getY
        R1 = self.R
        R2 = other.R

        distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        radSumSq = (r1 + r2) * (r1 + r2)

        if distSq > radSumSq:
            return(False)
        else:
            return(True)        