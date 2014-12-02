from xlrd import *
from datetime import *
import excel_format
import os


def parse_amount(amt):
    if(isinstance(amt,unicode)):
        amt = amt.replace(".","").replace(",",".").split(' ')[0]

    return float(amt)


def get_movement(r, xls_model):
    sheet = xls_model.sheet

    if(xls_model.date_as_text):
        date_movement = datetime.strptime(
            sheet.cell(r,xls_model.col_date).value,
            xls_model.date_format).date()
    else:
        date_value = xldate_as_tuple(sheet.cell(r,xls_model.col_date).value,
                                     xls_model.workbook.datemode)
        date_movement = date(*date_value[:3])

    concept = sheet.cell_value(r,xls_model.col_concept)
    amt = parse_amount(sheet.cell_value(r,xls_model.col_amount))
    blc = parse_amount(sheet.cell_value(r,xls_model.col_balance))

    return (date_movement, concept,amt, blc, xls_model.acc_name)


def get_San_movements():
    file_name = 'San.xlsx'
    acc_name = file_name[:-5]

    if not os.path.isfile(file_name):
        return []

    wb = open_workbook(file_name)
    sheet = wb.sheet_by_index(0)

    xls_model = excel_format.get_San_format_model(wb, sheet, sheet.nrows, acc_name)

    return get_list_mov_by_model(xls_model)


def get_Ing_movements(name):
    file_name = name + '.xls'
    movs = []
    for i in range(1,5):
        if not os.path.isfile(file_name):
            return movs

        wb = open_workbook(file_name)
        sheet = wb.sheet_by_index(0)
        xls_model = excel_format.get_Ing_format_model(wb, sheet, sheet.nrows, name)
        movs += get_list_mov_by_model(xls_model)

        file_name = name + '_' + str(i) + '.xls'

    return movs


def get_list_mov_by_model(model):
    list_movements = []
    for r in range(model.first_row,model.rows):
        list_movements.append(get_movement(r, model))

    return list_movements


def get_list_movements():
    list_movements = get_San_movements()
    list_movements += get_Ing_movements('Com')
    list_movements += get_Ing_movements('MJ')
    list_movements += get_Ing_movements('Rob')
    list_movements += get_Ing_movements('Nar')

    return list_movements

if __name__ == '__main__':
    wb = open_workbook('Com.xls')
    sheet = wb.sheet_by_index(0)
