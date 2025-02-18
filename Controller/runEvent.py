from Controller.IEvent import IEvent  
# from GAN import gan
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class runEvent(IEvent):
    def handle(self, ui_instance):
        if ui_instance.image_path:
            ui_instance.drop_label.setText("Processing Image...")
            result_path = "G:/Hripsime/Education/UNI/4rd_kurs/Diploma project/Slide, word/Photos/result.png"  # Call logic function
            ui_instance.drop_label.setText("Processing Complete!")
            ui_instance.result_image_path = result_path
            pixmap = QPixmap(result_path)
            ui_instance.upload_icon.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            ui_instance.download_button.setVisible(True)
            ui_instance.image_path = None