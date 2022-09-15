import cv2

from src.cameras.detection.cam_detection import DetectPossibleCameras


dpc = DetectPossibleCameras()

dpc.find_available_cameras()