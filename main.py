"""
Simple Image Converter - Version française 1.0

Copyright © Gaëtan Sencie 2025
Tous droits réservés.
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox, QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QFrame, QGroupBox, QSplashScreen
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QTimer
from PIL import Image
import cairosvg
import sys
import os
import tempfile
import fitz  # PyMuPDF

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # Répertoire temporaire utilisé par PyInstaller
    except Exception:
        base_path = os.path.abspath(".")  
    return os.path.join(base_path, relative_path)

class ImageConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()




# Code sous licence propriétaire


if __name__ == "__main__":
    app = QApplication(sys.argv)


