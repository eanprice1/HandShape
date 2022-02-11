import math
import cv2
import os
from HandMetrics import HandMetrics
from FingerMetrics import FingerMetrics
from Feature import Feature


# returns a list of all files in a specified directory
def get_files(dir_path) -> list:
    image_list = os.listdir(dir_path)
    return [f'{dir_path}/{file_name}' for file_name in image_list]


# returns a resized image and maintains aspect ratio
def aspect_ratio_resize(image, scale_percent: int):
    (h, w) = image.shape
    width = int(w * scale_percent / 100)
    height = int(h * scale_percent / 100)
    dimensions = (width, height)
    return cv2.resize(image, dimensions, cv2.INTER_AREA)


# reads and resizes a list of image file paths into a list of images ready for processing
def image_preprocessing(image_paths: list, scale_percent: int) -> dict:
    image_dict = {}
    for file_path in image_paths:
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        image = aspect_ratio_resize(image, scale_percent)
        image_dict[file_path] = HandMetrics(image)
    return image_dict


def point_selection(image_paths: list, image_dict: dict):
    point_collection = list()
    for image_path in image_paths:
        metrics: HandMetrics = image_dict[image_path]
        while len(point_collection) < 15:
            cv2.namedWindow(image_path)
            params = [point_collection]
            cv2.setMouseCallback(image_path, left_click_callback, params)
            cv2.imshow(image_path, metrics.image)
            cv2.waitKey(1)
            if len(point_collection) == 2:
                metrics.index = FingerMetrics(point_collection[0], point_collection[1])
            if len(point_collection) == 4:
                metrics.middle = FingerMetrics(point_collection[2], point_collection[3])
            if len(point_collection) == 6:
                metrics.ring = FingerMetrics(point_collection[4], point_collection[5])
            if len(point_collection) == 8:
                metrics.pinky = FingerMetrics(point_collection[6], point_collection[7])
            if len(point_collection) == 10:
                metrics.thumb_orthogonal = Feature(point_collection[8], point_collection[9])
            if len(point_collection) == 12:
                metrics.knuckle_orthogonal = Feature(point_collection[10], point_collection[11])
            if len(point_collection) == 14:
                metrics.backhand_orthogonal = Feature(point_collection[12], point_collection[13])
            metrics.draw_lines()
        cv2.destroyWindow(image_path)
        point_collection.clear()
        metrics.find_edges()


def left_click_callback(event, x, y, flags, params):
    point_collection: list = params[0]
    if event == cv2.EVENT_LBUTTONDOWN and (x, y) not in point_collection:
        point_collection.append((x, y))
        print((x, y))


def calculate_norm(vector_v: tuple) -> float:
    v1 = vector_v[0] ** 2
    v2 = vector_v[1] ** 2
    sum_squares = v1 + v2
    return math.sqrt(sum_squares)


def calculate_point_on_orthogonal(initial_point_p: tuple, distance: float, unit_vector_z: tuple) -> list:
    q1 = unit_vector_z[0] * distance
    q2 = unit_vector_z[1] * distance
    vector_q = (q1, q2)
    point1 = tuple(map(lambda p1, p2: int(p1 - p2), initial_point_p, vector_q))
    point2 = tuple(map(lambda p1, p2: int(p1 + p2), initial_point_p, vector_q))
    return [point1, point2]
