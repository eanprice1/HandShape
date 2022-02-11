import copy
import cv2
import skimage.draw as draw


class Feature:
    def __init__(self, point1: tuple, point2: tuple):
        self.point1 = point1
        self.point2 = point2
        self.line = self.find_points_in_line()
        self.edge1 = tuple()
        self.edge2 = tuple()

    def draw_line(self, image):
        cv2.line(image, self.point1, self.point2, 0, 1)

    def draw_circles(self, image):
        cv2.drawMarker(image, self.edge1, 0, cv2.MARKER_SQUARE, 10, 2)
        cv2.drawMarker(image, self.edge2, 0, cv2.MARKER_SQUARE, 10, 2)

    def find_points_in_line(self) -> list:
        xy_arrays = draw.line(self.point1[1], self.point1[0], self.point2[1], self.point2[0])
        return list(zip(xy_arrays[1], xy_arrays[0]))

    def find_edges(self, image):
        length = len(self.line)
        edge1 = self.line[0]
        edge2 = self.line[length - 1]
        max_increase = 0
        max_decrease = 0
        prev_pixel = ()
        for pixel in self.line:
            if len(prev_pixel) == 0:
                prev_pixel = copy.deepcopy(pixel)
                continue
            row = int(pixel[1]) - 1
            col = int(pixel[0]) - 1
            current_intensity = int(image[row, col])
            prev_row = int(prev_pixel[1]) - 1
            prev_col = int(prev_pixel[0]) - 1
            prev_intensity = int(image[prev_row, prev_col])
            diff_intensity = current_intensity - prev_intensity
            if diff_intensity > 0 and abs(diff_intensity) > max_increase:
                edge1 = (int(pixel[0]), int(pixel[1]))
                max_increase = abs(diff_intensity)
            elif diff_intensity < 0 and abs(diff_intensity) > max_decrease:
                edge2 = (int(pixel[0]), int(pixel[1]))
                max_decrease = abs(diff_intensity)
            prev_pixel = copy.deepcopy(pixel)
        self.edge1 = edge1
        self.edge2 = edge2
        self.draw_circles(image)
