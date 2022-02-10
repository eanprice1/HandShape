import cv2


class Feature:
    def __init__(self, point1: tuple, point2: tuple):
        self.point1 = point1
        self.point2 = point2
        self.line = list()
        self.left_edge = tuple()
        self.right_edge = tuple()

    def draw_line(self, image):
        cv2.line(image, self.point1, self.point2, (0, 255, 0), 1)
