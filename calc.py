class Calculator:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, char):
        self.expression += char

    def remove_last_character(self):
        self.expression = self.expression[:-1]

    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        try:
            result = round(eval(self.expression), 3)
            self.expression = str(result)
            return result
        except ZeroDivisionError as e:
            return "You can't divide by zero!"
        except Exception as e:
            return "Invalid syntax!"

    def get_expression(self):
        return self.expression