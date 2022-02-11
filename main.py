import cv2
import Utility as Util
from HandMetrics import HandMetrics


def main():
    image_paths = Util.get_files('Resources')
    image_dict = Util.image_preprocessing(image_paths, 12)
    Util.point_selection(image_paths, image_dict)

    for image_path in image_paths:
        metrics: HandMetrics = image_dict[image_path]
        cv2.namedWindow(image_path)
        cv2.imshow(image_path, metrics.image)
        cv2.waitKey(0)
        cv2.destroyWindow(image_path)


if __name__ == '__main__':
    main()
