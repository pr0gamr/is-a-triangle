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

    def valuechangeda(self, a):
        self.sidea = a
    def valuechangedb(self, b):
        self.sideb = b
    def valuechangedc(self, c):
        self.sidec = c

    def calculatetri(self):
        self.canBe = ""
        self.typeOfTri = ""
        if self.sidea != 0 and self.sideb != 0 and self.sidec != 0:
            if self.sidea + self.sideb > self.sidec and self.sidea + self.sidec > self.sideb and self.sideb + self.sidec > self.sidea:
                self.canBe = "This can be a triangle,"
                
                #below to determine what type of triangle
                if self.sidea != self.sideb and self.sideb != self.sidec and self.sidec != self.sidea:
                    self.typeOfTri = "it would be a scalene triangle"
                elif self.sidea == self.sideb and self.sideb == self.sidec:
                    self.typeOfTri = "it would be an equalateral triangle"
                else:
                    self.typeOfTri = "it would be an isosceles triangle"
                    
            else:
                self.canBe = "This can not be a triangle"
        else:
            self.canBe = "Please enter non-zero values"
        self.output.setText(f"{self.canBe} {self.typeOfTri}")

    def __init__(self):
        super().__init__()

        self.canBe = ""
        self.typeOfTri = ""
        self.sidea = 0.0
        self.sideb = 0.0
        self.sidec = 0.0

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
        widget.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout0.addWidget(widget)
        layout0.setContentsMargins(0,20,0,0)
        layout0.setSpacing(10)
        
        a = QDoubleSpinBox()
        title_a = QLabel("Side A")
        a.setMinimum(0)
        a.setMaximum(99999.99)
        a.valueChanged.connect(self.valuechangeda)
        layout1.addWidget(title_a)
        layout1.addWidget(a)
        layout1.setContentsMargins(0,20,0,0)
        layout1.setSpacing(10)

        b = QDoubleSpinBox()
        title_b = QLabel("Side B")
        b.setMinimum(0)
        b.setMaximum(99999.99)
        b.valueChanged.connect(self.valuechangedb)
        layout2.addWidget(title_b)
        layout2.addWidget(b)
        layout2.setContentsMargins(0,20,0,0)
        layout2.setSpacing(10)

        c = QDoubleSpinBox()
        title_c = QLabel("Side C")
        c.setMinimum(0)
        c.setMaximum(99999.99)
        c.valueChanged.connect(self.valuechangedc)
        layout3.addWidget(title_c)
        layout3.addWidget(c)
        layout3.setContentsMargins(0,20,0,0)
        layout3.setSpacing(10)

        calculate = QPushButton("Calculate")
        self.output = QLabel(self.canBe + self.typeOfTri)
        calculate.clicked.connect(self.calculatetri)
        layout4.addWidget(calculate)
        layout4.addWidget(self.output)

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
