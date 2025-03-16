class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.connect_signals()

    def connect_signals(self):
        """Connect button signals to controller methods."""
        for button in self.view.buttons:
            button.clicked.connect(lambda _, b=button: self.handle_button_click(b.text()))

    def handle_button_click(self, text):
        """Handle button clicks and call the appropriate model methods."""
        if text == "C":
            self.model.clear_expression()  # Clear the expression
            self.view.update_display("")  # Clear the display in the view
        elif text == "=":
            result = self.model.calculate()  # Calculate the result
            self.view.update_display(str(result))  # Update the display with the result
        else:
            self.model.add_to_expression(text)  # Add the button text to the expression
            self.view.update_display(self.model.get_expression())  # Update the display