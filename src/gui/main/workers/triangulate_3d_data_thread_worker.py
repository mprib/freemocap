from pathlib import Path
from typing import Union

import numpy as np
from PyQt6.QtCore import QThread, pyqtSignal

import logging

from src.core_processes.capture_volume_calibration.triangulate_3d_data import (
    triangulate_3d_data,
)

logger = logging.getLogger(__name__)


class Triangulate3dDataThreadWorker(QThread):
    finished = pyqtSignal()

    def __init__(
        self,
        anipose_calibration_object,
        mediapipe_2d_data: np.ndarray,
        output_data_folder_path: Union[str, Path],
        mediapipe_confidence_cutoff_threshold: float,
        save_data_as_csv: bool,
    ):
        super().__init__()
        self._anipose_calibration_object = anipose_calibration_object
        self._mediapipe_2d_data = mediapipe_2d_data
        self._output_data_folder_path = output_data_folder_path
        self._mediapipe_confidence_cutoff_threshold = (
            mediapipe_confidence_cutoff_threshold
        )
        self._save_data_as_csv = save_data_as_csv

    def run(self):
        logger.info(
            f"Triangulating 3d data (i.e. combining 2d skeleton data with camera calibration data to estimate 3d positions of tracked points"
        )

        triangulate_3d_data(
            anipose_calibration_object=self._anipose_calibration_object,
            mediapipe_2d_data=self._mediapipe_2d_data,
            output_data_folder_path=self._output_data_folder_path,
            mediapipe_confidence_cutoff_threshold=self._mediapipe_confidence_cutoff_threshold,
            save_data_as_csv=self._save_data_as_csv,
        )

        self.finished.emit()
