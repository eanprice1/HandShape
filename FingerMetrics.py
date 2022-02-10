import cv2
from Feature import Feature


class FingerMetrics:
    def __init__(self, point1: tuple, point2: tuple):
        self.point1 = point1
        self.point2 = point2
        self.upper_orthogonal: Feature
        self.lower_orthogonal: Feature

    def draw_line(self, image):
        cv2.line(image, self.point1, self.point2, (0, 255, 0), 1)