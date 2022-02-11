from FingerMetrics import FingerMetrics
from Feature import Feature


class HandMetrics:
    def __init__(self, image):
        self.image = image
        self.finger1: FingerMetrics = None
        self.finger2: FingerMetrics = None
        self.finger3: FingerMetrics = None
        self.finger4: FingerMetrics = None
        self.measurement1: Feature = None
        self.measurement2: Feature = None
        self.measurement3: Feature = None

    def draw_lines(self):
        if self.finger1 is not None:
            self.finger1.draw_line(self.image)
        if self.finger2 is not None:
            self.finger2.draw_line(self.image)
        if self.finger3 is not None:
            self.finger3.draw_line(self.image)
        if self.finger4 is not None:
            self.finger4.draw_line(self.image)
        if self.measurement1 is not None:
            self.measurement1.draw_line(self.image)
        if self.measurement2 is not None:
            self.measurement2.draw_line(self.image)
        if self.measurement3 is not None:
            self.measurement3.draw_line(self.image)

    def find_edges(self):
        if self.finger1 is not None:
            self.finger1.find_edges(self.image)
        if self.finger2 is not None:
            self.finger2.find_edges(self.image)
        if self.finger3 is not None:
            self.finger3.find_edges(self.image)
        if self.finger4 is not None:
            self.finger4.find_edges(self.image)
        if self.measurement1 is not None:
            self.measurement1.find_edges(self.image)
        if self.measurement2 is not None:
            self.measurement2.find_edges(self.image)
        if self.measurement3 is not None:
            self.measurement3.find_edges(self.image)
