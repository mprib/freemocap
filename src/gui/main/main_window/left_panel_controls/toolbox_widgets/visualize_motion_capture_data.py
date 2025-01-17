from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
)


class VisualizeMotionCaptureDataPanel(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout()

        self._load_session_data_button = QPushButton(
            "Load Session Data",
        )
        self._load_session_data_button.setEnabled(True)
        self._layout.addWidget(self._load_session_data_button)

        self._play_button = QPushButton("Play")
        self._play_button.setEnabled(False)
        self._layout.addWidget(self._play_button)

        self._pause_button = QPushButton("Pause")
        self._pause_button.setEnabled(False)
        self._layout.addWidget(self._pause_button)

        self._layout.addStretch()

        self.setLayout(self._layout)

    @property
    def load_session_data_button(self):
        return self._load_session_data_button
