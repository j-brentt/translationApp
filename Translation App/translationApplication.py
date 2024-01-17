import sys
import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QComboBox
from PyQt6.QtGui import QFont
from translationAPI import Translate

class TranslationApp(QMainWindow):
    def __init__(self):
        # Create a seperate method that initalizs a dark UI based on time of day
        super().__init__()
        self.init_ui()

    def init_ui(self):
        '''
        Initializes the UI
        '''
        # Window setup
        self.setWindowTitle('Translation App')
        self.setGeometry(100, 100, 400, 300)

        self.source_label = QLabel('Source Text:')
        self.source_text = QTextEdit()

        self.translated_label = QLabel('Translated Text:')
        self.translated_text = QTextEdit()
        self.translated_text.setReadOnly(True)

        self.language_label = QLabel('Select Language:')
        self.language_dropdown = QComboBox()
        self.language_dropdown.addItems(['English', 'Spanish', 'French', 'German', 'Greek', 'Tagalog'])  # Add your language options here

        self.translate_button = QPushButton('Translate')
        self.translate_button.clicked.connect(self.translate_text)

        # Change the font of the QLabel widgets
        self.label_font = QFont()
        self.label_font.setFamily("Arial")  # Set the font family (e.g., Arial)
        self.label_font.setPointSize(12)  # Set the font size
        self.label_font.setBold(True)  # Set the font to bold (optional)

        self.source_label.setFont(self.label_font)
        self.translated_label.setFont(self.label_font)
        self.language_label.setFont(self.label_font)

        # Change the font of the QPushButton
        self.button_font = QFont()
        self.button_font.setFamily("Times New Roman")  # Set the font family
        self.button_font.setPointSize(14)  # Set the font size
        self.button_font.setBold(True)  # Set the font to bold (optional)

        self.translate_button.setFont(self.button_font)

        # Layout setup
        vbox = QVBoxLayout()
        vbox.addWidget(self.source_label)
        vbox.addWidget(self.source_text)
        vbox.addWidget(self.language_label)
        vbox.addWidget(self.language_dropdown)
        vbox.addWidget(self.translate_button)
        vbox.addWidget(self.translated_label)
        vbox.addWidget(self.translated_text)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Set the UI to dark mode if it's after 7:00 PM
        self.set_dark_mode()

    def set_dark_mode(self):
        '''
        Sets the UI to dark mode after 7:00 PM
        '''
        current_time = datetime.datetime.now().time()
        if current_time >= datetime.time(19, 00): # 7:00 PM
            dark_grey = "#444444"  # Dark grey background
            light_grey = "#222222"  # Light grey background
            text_color = "#FFFFFF"  # White text on grey background

            # Apply dark grey color scheme to UI elements
            self.setStyleSheet(
                f"background-color: {dark_grey}; color: {text_color};"
                f"QTextEdit {{ background-color: {light_grey}; color: {text_color}; }}"  # Light grey for text editors
                f"QPushButton {{ background-color: {light_grey}; color: {text_color}; }}"  # Light grey for buttons
                f"QComboBox {{ background-color: #004368; color: #FFFFFF; }}"  # Dark blue for combo box
            )

    def translate_text(self):
        '''
        Translates the text in the source_text QTextEdit widget to the language 
        selected in the language_dropdown QComboBox widget
        '''
        translate = Translate()
        translate.set_language(self.language_dropdown.currentText())
        self.translated_text.setText(translate.translate_text(self.source_text.toPlainText()))

def main():
    app = QApplication(sys.argv)
    window = TranslationApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()