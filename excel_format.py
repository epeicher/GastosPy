class ExcelFormat:

    def __init__(self, workbook, sheet, col_date, col_concept, col_amount, col_balance):
        self.workbook = workbook
        self.sheet = sheet
        self.col_date = col_date
        self.col_concept = col_concept
        self.col_amount = col_amount
        self.col_balance = col_balance
