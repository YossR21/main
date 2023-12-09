import random
from PyQt6.QtWidgets import *
from gui import *
from math import *
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Initializing Logic() class, setting up private instances
        """
        super().__init__()
        self.setupUi(self)
        self.__formula_cbox: QComboBox = self.formula_box
        self.__numbers_texbox: QTextEdit = self.numbers_texbox
        self.error_label.setWordWrap(True)
        self.done_button.clicked.connect(lambda: self.done())

    def done(self) -> None:
        """
        :return:
        Based on their preferred mathematical operation,
        solve and provide the result, or display the error message
        """
        num_input = self.__numbers_texbox.toPlainText().split()
        numbers = []
        try:
            for i in num_input:
                i = float(i)
                numbers.append(i)
        except ValueError:
            return self.error_label.pyqtConfigure(text='Enter space separated numbers only, no strings')
        # print(numbers, len(numbers))
        formula = self.__formula_cbox.currentText()
        if formula == 'Random':
            options = ['Add', 'Subtract', 'Multiply', 'Divide']
            formula = random.choice(options)
            # self.error_label.setText(f'Random formula given: {formula}\n')

        match formula:
            case "Add":
                if len(numbers) <= 1:
                    return self.error_label.pyqtConfigure(text='Enter at least two numbers for Addition')
                else:
                    addition = 0
                    for i in numbers:
                        if i > 0:
                            addition += i
                    return (self.error_label.pyqtConfigure(text=f'Addition Answer = {addition:.2f}'),
                            self.__numbers_texbox.setPlainText(""))
            case "Subtract":
                if len(numbers) <= 1:
                    return self.error_label.pyqtConfigure(text='Enter at least two numbers for Subtraction')
                else:
                    subtraction = 0
                    for i in numbers:
                        if i < 0:
                            subtraction += i
                    return (self.error_label.pyqtConfigure(text=f'Subtraction Answer = {subtraction:.2f}'),
                            self.__numbers_texbox.setPlainText(""))

            case "Divide":
                if len(numbers) <= 1:
                    return self.error_label.pyqtConfigure(text='Enter at least two numbers for division, 0 is not an acceptable number')
                else:
                    if numbers[0] != 0:
                        division = numbers[0]
                        for i in numbers[1:]:
                            if i == 0:
                                return (self.error_label.pyqtConfigure(text= f'Cannot divide by 0'),
                                        self.__numbers_texbox.setPlainText(""))
                            else:
                                division /= i
                    else:
                        return (self.error_label.pyqtConfigure(text=f'0'),
                                self.__numbers_texbox.setPlainText(""))

                    return (self.error_label.pyqtConfigure(text= f'Division Answer = {division:.2f}'),
                            self.__numbers_texbox.setPlainText(""))

            case "Multiply":
                if len(numbers) <= 1:
                    return self.error_label.pyqtConfigure(text='Enter at least two numbers for Multiplication,  0 is not an acceptable number')
                else:
                    if numbers[0] != 0:
                        mult = numbers[0]
                        for i in numbers[1:]:
                            if i > 0:
                                mult *= i
                            elif i == 0:
                                return self.error_label.pyqtConfigure(text=f'0'), self.__numbers_texbox.setPlainText("")
                    else:
                        return self.error_label.pyqtConfigure(text=f'0'), self.__numbers_texbox.setPlainText("")
                    return (self.error_label.pyqtConfigure(text=f'Multiplication Answer = {mult:.2f}'),
                            self.__numbers_texbox.setPlainText(""))
            case "Square Root":
                if len(numbers) != 1:
                    return self.error_label.pyqtConfigure(text='Enter one number for Square Root')
                else:
                    if numbers[0] > 1:
                        return (self.error_label.pyqtConfigure(text = f'Square Root Answer = {sqrt(numbers[0]):.2f}'),
                                self.__numbers_texbox.setPlainText(""))
                    else:
                        return (self.error_label.pyqtConfigure(text = f'Square Root of a negative number is not possible'),
                                           self.__numbers_texbox.setPlainText(""))
                #cannot take negative numbers
