from enum import Enum


class OperationTypes(Enum):
    add = "+"
    subtract = "-"
    multiply = "*"
    divide = "/"


class Operand:
    def __init__(self, amount):
        self.amount = amount

    def is_number(self):
        try:
            float(self.amount)
            return True
        except ValueError:
            return False

    def is_empty(self):
        if self.amount == '':
            return True
        return False

    def get_amount(self):
        if self.is_empty():
           return False, self.amount
        if not self.is_number():
           return False, self.amount
        return True, float(self.amount)

    def check_validity(self):
        is_validity, _ = self.get_amount()
        if is_validity:
            return True
        return False


class Operation:
    def __init__(self, first_operand, second_operand, operation):
        self.first_operand = first_operand
        self.second_operand = second_operand
        self.operation = operation

    def get_result(self):
        _, first_operand = self.first_operand.get_amount()
        _, second_operand = self.second_operand.get_amount()
        match self.operation:
            case OperationTypes.add:
                return first_operand + second_operand
            case OperationTypes.subtract:
                return first_operand - second_operand
            case OperationTypes.multiply:
                return first_operand * second_operand
            case OperationTypes.divide:
                if second_operand != 0:
                    return first_operand / second_operand
                else:
                    return "Division by zero!"
