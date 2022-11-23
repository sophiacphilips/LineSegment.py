#Author: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 11/21/22
#This code is designed to find the distance between two points, their slope, and determine if two line segments are parallel.

class Point: #defines class Point
    def __init__(self, x_coord, y_coord):
        """Initializes objects for x and y coordinates while accepting parameters"""
        self._x_coord= x_coord
        self._y_coord= y_coord

    def get_x_coord(self):
        """Returns the x coordinate"""
        return self._x_coord

    def get_y_coord(self):
        """Returns the y coordinate"""
        return self._y_coord

    def distance_to(self, point_dist):
        """Returns distance between two points"""
        return abs((((point_dist._x_coord-self._x_coord)**2)+(point_dist._y_coord-self._y_coord)**2)**0.5)

class LineSegment: #defines class LineSegment
    def __init__(self, endpoint_1, endpoint_2):
        """Initializes objects for endpoints 1 and 2 while accepting parameters"""
        self._endpoint_1= endpoint_1
        self._endpoint_2= endpoint_2

    def get_endpoint_1(self):
        """Returns endpoint 1"""
        return self._endpoint_1

    def get_endpoint_2(self):
        """Returns endpoint 2"""
        return self._endpoint_2

    def length(self):
        """Returns length between endpoints"""
        return self._endpoint_1.distance_to(self._endpoint_2)

    def is_parallel_to(self, line_seg): #checks lines for parallel
        """checks if line segments are parallel returns true if they are and false if not"""
        if self.slope()==line_seg.slope():
            return True
        else:
            return False

    def slope(self):
        """Returns slope of lines"""
        return abs((self._endpoint_2.get_y_coord()-self._endpoint_1.get_y_coord())/(self._endpoint_2.get_x_coord()-self._endpoint_1.get_x_coord()))

#testing
#point_1 = Point(7,4)
#point_2 = Point(-6,18)
#print(point_1.distance_to(point_2))
#line_seg_1 = LineSegment(point_1,point_2)
#print(line_seg_1.length())
#print(line_seg_1.slope())

#point_3 = Point(-2,2)
#point_4 = Point(24, 12)
#line_seg_2 = LineSegment(point_3,point_4)
#print(line_seg_1.is_parallel_to(line_seg_2))