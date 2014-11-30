from xlrd import *
from datetime import *
import excel_format


def parse_amount(amt):
    if(isinstance(amt,unicode)):
        amt = amt.replace(".","").replace(",",".")

    return float(amt)


def get_movement(r, xls_model):
    sheet = xls_model.sheet
    date_value = xldate_as_tuple(sheet.cell(r,xls_model.col_date).value,
                                 xls_model.workbook.datemode)
    date_movement = date(*date_value[:3])
    concept = sheet.cell_value(r,xls_model.col_concept)
    amt = parse_amount(sheet.cell_value(r,xls_model.col_amount))
    blc = parse_amount(sheet.cell_value(r,xls_model.col_balance))

    return (date_movement, concept,amt, blc)


def get_San_movements():
    file_name = 'San.xlsx'
    first_row = 11
    col_date = 3
    col_concept = 5
    col_amount = 7
    col_balance = 9

    wb = open_workbook(file_name)
    sheet = wb.sheet_by_index(0)

    xls_model = excel_format.ExcelFormat(wb,sheet,col_date, col_concept,col_amount, col_balance)

    list_movements = []
    for r in range(first_row,sheet.nrows):
        list_movements.append(get_movement(r, xls_model))

    return list_movements


def get_Com_movements():
    file_name = 'Com.xls'
    first_row = 5
    col_date = 1
    col_concept = 2
    col_amount = 3
    col_balance = 4

    wb = open_workbook(file_name)
    sheet = wb.sheet_by_index(0)

    xls_model = excel_format.ExcelFormat(wb,sheet,col_date, col_concept,col_amount, col_balance)

    list_movements = []
    for r in range(first_row,sheet.nrows):
        list_movements.append(get_movement(r, xls_model))

    return list_movements


def get_list_movements():
    list_movements = get_San_movements()
    list_movements += get_Com_movements()

    return list_movements
