import cv2
import os
from HandMetrics import HandMetrics


# returns a list of all files in a specified directory
def get_files(dir_path) -> list:
    image_list = os.listdir(dir_path)
    return [f'{dir_path}/{file_name}' for file_name in image_list]


# returns a resized image and maintains aspect ratio
def aspect_ratio_resize(image, scale_percent):
    (h, w) = image.shape
    width = int(w * scale_percent / 100)
    height = int(h * scale_percent / 100)
    dimensions = (width, height)
    return cv2.resize(image, dimensions, cv2.INTER_AREA)


# reads and resizes a list of image file paths into a list of images ready for processing
def image_preprocessing(image_paths, scale_percent) -> dict:
    image_dict = {}
    for file_path in image_paths:
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        image = aspect_ratio_resize(image, scale_percent)
        image_dict[file_path] = HandMetrics(image)
    return image_dict
