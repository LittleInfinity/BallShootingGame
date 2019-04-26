#colors
import math
class Colors:
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)

class Maths:
    def isPointInsideCircle(pt_x, pt_y, cl_x, cl_y, radius):
        if(math.sqrt((pt_x-cl_x)**2 + (pt_y-cl_y)**2) > radius):
            return False
        else:
            return True
        
