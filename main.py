import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)

from plus import plus
from minus import minus
from multiple import multiple
from divide import divide


def calculate(operation, first_input, second_input, result_label):
    try:
        a = float(first_input.text())
        b = float(second_input.text())

        result = operation(a, b)
        result_label.setText(f"Result: {result}")

    except ValueError:
        result_label.setText("Error: enter valid numbers!")
    except ZeroDivisionError:
        result_label.setText("Error: division by zero!")


def visual_box():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Calculator - DayDreamingg-g")
    window.resize(400, 350)

    layout = QVBoxLayout()

    title = QLabel("Python Calculator")
    layout.addWidget(title)

    first_label = QLabel("Enter the first number:")
    layout.addWidget(first_label)

    first_number = QLineEdit()
    first_number.setPlaceholderText("First number")
    layout.addWidget(first_number)

    second_label = QLabel("Enter the second number:")
    layout.addWidget(second_label)

    second_number = QLineEdit()
    second_number.setPlaceholderText("Second number")
    layout.addWidget(second_number)

    buttons = QHBoxLayout()

    operations = [
        ("+", plus),
        ("-", minus),
        ("×", multiple),
        ("÷", divide),
    ]

    result_label = QLabel("Result: ")

    for symbol, operation in operations:
        button = QPushButton(symbol)
        button.clicked.connect(
            lambda checked=False, op=operation: calculate(
                op, first_number, second_number, result_label
            )
        )
        buttons.addWidget(button)

    layout.addLayout(buttons)
    layout.addWidget(result_label)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())


def main():
    visual_box()


if __name__ == "__main__":
    main()
