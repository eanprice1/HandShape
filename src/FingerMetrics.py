import cv2
import Utility as Util
from Feature import Feature


class FingerMetrics:
    def __init__(self, point1: tuple, point2: tuple):
        self.point1 = point1
        self.point2 = point2
        orthogonal_features = self.calculate_orthogonal_features()
        self.orthogonal1: Feature = orthogonal_features[0]
        self.orthogonal2: Feature = orthogonal_features[1]

    def draw_line(self, image):
        cv2.line(image, self.point1, self.point2, 0, 1)
        self.orthogonal1.draw_line(image)
        self.orthogonal2.draw_line(image)

    def find_edges(self, image):
        self.orthogonal1.find_edges(image)
        self.orthogonal2.find_edges(image)

    def calculate_orthogonal_features(self) -> list:
        vector_v = tuple(map(lambda p1, p2: p1 - p2, self.point1, self.point2))
        vector_v_norm = Util.calculate_norm(vector_v)
        half_vector_v_norm = vector_v_norm / 2
        if vector_v[0] == 0:
            orthogonal_vector_u = (vector_v[1], vector_v[0])
        else:
            y = 1
            x = ((-1) * vector_v[1] * y) / vector_v[0]
            orthogonal_vector_u = (x, y)
        orthogonal_vector_u_norm = Util.calculate_norm(orthogonal_vector_u)
        z1 = orthogonal_vector_u[0] / orthogonal_vector_u_norm
        z2 = orthogonal_vector_u[1] / orthogonal_vector_u_norm
        unit_vector_z = (z1, z2)
        orthogonal1_point1, orthogonal1_point2 = Util.calculate_point_on_orthogonal(self.point1,
                                                                                    half_vector_v_norm,
                                                                                    unit_vector_z)
        orthogonal2_point1, orthogonal2_point2 = Util.calculate_point_on_orthogonal(self.point2,
                                                                                    half_vector_v_norm,
                                                                                    unit_vector_z)
        return [Feature(orthogonal1_point1, orthogonal1_point2),
                Feature(orthogonal2_point1, orthogonal2_point2)]
