import cv2
import numpy as np
import Utility as Util
from HandMetrics import HandMetrics
from FingerMetrics import FingerMetrics
from Feature import Feature

point_collection = list()


def main():
    image_paths = Util.get_files('Resources')
    image_dict = Util.image_preprocessing(image_paths, 12)
    for image_path in image_paths:
        while len(point_collection) < 15:
            cv2.namedWindow(image_path)
            params = [image_path]
            cv2.setMouseCallback(image_path, left_click_callback, params)
            cv2.imshow(image_path, image_dict[image_path].image)
            cv2.waitKey(1)
            if len(point_collection) == 2:
                image_dict[image_path].index = FingerMetrics(point_collection[0], point_collection[1])
            if len(point_collection) == 4:
                image_dict[image_path].middle = FingerMetrics(point_collection[2], point_collection[3])
            if len(point_collection) == 6:
                image_dict[image_path].ring = FingerMetrics(point_collection[4], point_collection[5])
            if len(point_collection) == 8:
                image_dict[image_path].pinky = FingerMetrics(point_collection[6], point_collection[7])
            if len(point_collection) == 10:
                image_dict[image_path].thumb_orthogonal = Feature(point_collection[8], point_collection[9])
            if len(point_collection) == 12:
                image_dict[image_path].knuckle_orthogonal = Feature(point_collection[10], point_collection[11])
            if len(point_collection) == 14:
                image_dict[image_path].backhand_orthogonal = Feature(point_collection[12], point_collection[13])
            image_dict[image_path].draw_lines()
        cv2.destroyWindow(image_path)
        point_collection.clear()

    for image_path in image_paths:
        cv2.namedWindow(image_path)
        cv2.imshow(image_path, image_dict[image_path].image)
        cv2.waitKey(0)
        cv2.destroyWindow(image_path)


def left_click_callback(event, x, y, flags, params):
    global point_collection
    image_path = params[0]
    if event == cv2.EVENT_LBUTTONDOWN:
        point_collection.append((x, y))
        print(point_collection)


if __name__ == '__main__':
    main()
