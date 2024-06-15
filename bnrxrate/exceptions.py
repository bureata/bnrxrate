
class DateRangeInvalid(Exception):
    def __init__(self, message, start_date, end_date):
        super().__init__(message)
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"{self.args[0]} | start_date: {self.start_date}, end_date: {self.end_date}"


class SymbolNotAvailable(Exception):
    def __init__(self, message, symbol, date):
        super().__init__(message)
        self.symbol = symbol
        self.date = date

    def __str__(self):
        return f'{self.args[0]} | Symbol "{self.symbol}" not available at {str(self.date)}'
