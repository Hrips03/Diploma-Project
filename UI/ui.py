import os
import shutil
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QFrame
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from Controller.IEvent import IEvent
from Controller.runEvent import runEvent
from Controller.uploadEvent import uploadEvent
from Controller.downloadEvent import downloadEvent

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.image_path = None
        self.result_image_path = None
        self.init_ui()

        self.event_map = {
            "upload": uploadEvent(),
            "run": runEvent(),
            "download": downloadEvent(),
        }


    def init_ui(self):
        self.setWindowTitle("Mask Optimization Algorithm")
        self.setGeometry(100, 100, 500, 450)
        self.setStyleSheet("background-color: #ADD8E6;")

        layout = QVBoxLayout(self)

        title_label = QLabel("Upload Layout", self)
        title_label.setFont(QFont("Arial", 14, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #003399;")
        layout.addWidget(title_label)

        self.drop_area = QFrame(self)
        self.drop_area.setStyleSheet(
            "background-color: #f7faff; border-radius: 12px; border: 2px dashed #a0c4ff; padding: 40px;")
        self.drop_area.setFrameShape(QFrame.StyledPanel)
        layout.addWidget(self.drop_area)

        drop_layout = QVBoxLayout(self.drop_area)

        self.upload_icon = QLabel(self.drop_area)
        self.upload_icon.setPixmap(QPixmap("upload_icon_new.png").scaled(
            100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.upload_icon.setAlignment(Qt.AlignCenter)
        drop_layout.addWidget(self.upload_icon)

        self.drop_label = QLabel("Drag & drop your layout image here", self.drop_area)
        self.drop_label.setFont(QFont("Arial", 10))
        self.drop_label.setAlignment(Qt.AlignCenter)
        drop_layout.addWidget(self.drop_label)

        self.attach_button = self.create_button("Choose Image", "#003399", lambda: self.sendEvent("upload"))
        layout.addWidget(self.attach_button)

        self.run_button = self.create_button("Run", "#003399", lambda: self.sendEvent("run"), visible=False)
        layout.addWidget(self.run_button)

        self.download_button = self.create_button("Download Result", "#28a745", lambda: self.sendEvent("download"), visible=False)
        layout.addWidget(self.download_button)

        self.setAcceptDrops(True)

    def create_button(self, text, color, callback, visible=True):
        button = QPushButton(text, self)
        button.setStyleSheet(
            f"background-color: white; border: 2px solid {color}; color: {color}; "
            "padding: 10px; border-radius: 8px;")
        button.clicked.connect(callback)
        button.setVisible(visible)
        return button


    def sendEvent(self, event_type):
        print(f"sendEvent called with event_type: {event_type}")  # Debugging
        event = self.event_map.get(event_type)
        if event:
            print(f"Calling handle method for {event_type}")  # Debugging
            event.handle(self)
        else:
            print(f"Unknown event type: {event_type}")



    # def attach_file(self):
    #     """Opens file dialog to select an image."""
    #     file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
    #     if file_path:
    #         self.load_file(file_path)

    # def load_file(self, file_path):
    #     """Loads and displays the selected image."""
    #     self.image_path = file_path
    #     self.drop_label.setText(f"Selected: {os.path.basename(file_path)}")
    #     pixmap = QPixmap(file_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    #     self.upload_icon.setPixmap(pixmap)
    #     self.run_button.setVisible(True)

    # def run_logic(self):
    #     """Placeholder for the processing function."""
    #     if self.image_path:
    #         self.drop_label.setText("Processing Image... (Logic not included)")
    #         self.result_image_path = "result.png"  # Dummy placeholder for processed image
    #         self.display_result_image(self.result_image_path)
    #         self.download_button.setVisible(True)

    # def display_result_image(self, result_path):
    #     """Displays the result image after processing."""
    #     pixmap = QPixmap(result_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    #     self.upload_icon.setPixmap(pixmap)

    # def download_result(self):
    #     """Allows the user to save the processed image."""
    #     save_path, _ = QFileDialog.getSaveFileName(self, "Save Result", "", "Images (*.png *.jpg *.bmp)")
    #     if save_path and self.result_image_path:
    #         shutil.copy(self.result_image_path, save_path)
    #         self.drop_label.setText(f"Saved at: {save_path}")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            if file_path.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                # self.load_file(file_path)
                self.image_path = file_path
                self.sendEvent("upload")
            else:
                self.drop_label.setText("Invalid file type! Please drop an image.")

