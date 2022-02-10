import cv2
from FingerMetrics import FingerMetrics
from Feature import Feature


class HandMetrics:
    def __init__(self, image):
        self.image = image
        self.index: FingerMetrics = None
        self.middle: FingerMetrics = None
        self.ring: FingerMetrics = None
        self.pinky: FingerMetrics = None
        self.thumb_orthogonal: Feature = None
        self.knuckle_orthogonal: Feature = None
        self.backhand_orthogonal: Feature = None

    def draw_lines(self):
        if self.index is not None:
            self.index.draw_line(self.image)
        if self.middle is not None:
            self.middle.draw_line(self.image)
        if self.ring is not None:
            self.ring.draw_line(self.image)
        if self.pinky is not None:
            self.pinky.draw_line(self.image)
        if self.thumb_orthogonal is not None:
            self.thumb_orthogonal.draw_line(self.image)
        if self.knuckle_orthogonal is not None:
            self.knuckle_orthogonal.draw_line(self.image)
        if self.backhand_orthogonal is not None:
            self.backhand_orthogonal.draw_line(self.image)