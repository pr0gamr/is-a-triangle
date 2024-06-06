import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def calculatetri(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            print("This can be a triangle,")
            
            #below to determine what type of triangle
            if a != b and b != c and c != a:
                print("it would be a scalene triangle")
            elif a == b and b == c:
                print("it would be an equalateral triangle")
            else:
                print("it would be an isosceles triangle")
                
        else:
            print("This can NOT be a triangle")

    def __init__(self):
        super().__init__()

        canBe = ""
        typeOfTri = ""

        self.setWindowTitle("Is It a Triangle")

        layout = QVBoxLayout()
        layout0 = QVBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout4 = QVBoxLayout()

        widgets = [
            QDoubleSpinBox,
            QLabel,
            QPushButton,
            QSpinBox,
        ]

        widget = QLabel("Enter side lengths please.")
        widget.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        layout0.addWidget(widget)
        
        a = QDoubleSpinBox()
        title_a = QLabel("Side A")
        layout1.addWidget(title_a)
        layout1.addWidget(a)
        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(20)

        b = QDoubleSpinBox()
        title_b = QLabel("Side B")
        layout2.addWidget(title_b)
        layout2.addWidget(b)
        layout2.setContentsMargins(0,0,0,0)
        layout2.setSpacing(20)

        c = QDoubleSpinBox()
        title_c = QLabel("Side C")
        layout3.addWidget(title_c)
        layout3.addWidget(c)
        layout3.setContentsMargins(0,0,0,0)
        layout3.setSpacing(20)

        calculate = QPushButton("Calculate")
        output = QLabel(canBe + typeOfTri)
        calculate.clicked.connect(self.calculatetri(1,1,1))
        layout4.addWidget(calculate)
        layout4.addWidget(output)

        layout.addLayout(layout0)
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
