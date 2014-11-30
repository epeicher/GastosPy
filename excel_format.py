class ExcelFormat:

    def __init__(self, first_row, col_date, col_concept, col_amount, col_balance):
        self.first_row = first_row
        self.col_date = col_date
        self.col_concept = col_concept
        self.col_amount = col_amount
        self.col_balance = col_balance


def get_San_format_model(wb, sheet, rows, acc_name):
    first_row = 11
    col_date = 3
    col_concept = 5
    col_amount = 7
    col_balance = 9
    xls_model = ExcelFormat(first_row, col_date, col_concept, col_amount, col_balance)
    xls_model.workbook = wb
    xls_model.sheet = sheet
    xls_model.rows = rows
    xls_model.acc_name = acc_name

    return xls_model


def get_Ing_format_model(wb, sheet, rows, acc_name):
    first_row = 5
    col_date = 1
    col_concept = 2
    col_amount = 3
    col_balance = 4
    xls_model = ExcelFormat(first_row, col_date, col_concept, col_amount, col_balance)
    xls_model.workbook = wb
    xls_model.sheet = sheet
    xls_model.rows = rows
    xls_model.acc_name = acc_name

    return xls_model
