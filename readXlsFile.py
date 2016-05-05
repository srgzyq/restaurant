# -*- coding: utf-8 -*-
from xlrd import open_workbook
#from xlrd import cellname


def getXlsSheetNameByIndex(file_name, sheet_index):
    file_book = open_workbook(file_name)
    # sheet表格内容
    sheet_name = file_book.sheet_names()[sheet_index]
    return sheet_name


def getXlsDataByFile(file_name, sheet_index):
    '''
            返回	(表头内容,剩余内容）
            表头内容:[(type,value),(type,value)]
            剩余内容:[[(type,value),(type,value)],[(type,value),(type,value)]]
    '''

    file_book = open_workbook(file_name)
    # sheet表格内容
    table = file_book.sheet_by_index(sheet_index)
    # sheet表格内容
    #table_name = file_book.sheet_names()[sheet_index]
    # sheet表格行列数
    # table_cols = table.ncols
    table_rows = table.nrows

    # 第一行表头
    table_content = []
    table_title_value = table.row_values(0)
    table_title_type = table.row_types(0)
    for t_type, t_value in zip(table_title_type, table_title_value):
        table_content.append((t_type, t_value))

    line_cotents = []
    # 除去表头的内容行
    for line_index in range(1, table_rows):
        line_data_value = table.row_values(line_index)
        line_data_type = table.row_types(line_index)
        line_content = []
        for t_type, t_value in zip(line_data_type, line_data_value):
            line_content.append((t_type, t_value))
        line_cotents.append(line_content)

    return table_content, line_cotents


def getXlsTableByFileAndSheet(file_name):
    file_book = open_workbook(file_name)
    return file_book


def getXlsTableRowAndCol(file_name, sheet_index):
    file_book = open_workbook(file_name)
    # print "file_name:",file_name,"sheet_index:",sheet_index
    # sheet表格内容
    table = file_book.sheet_by_index(sheet_index)
    # sheet表格行列数
    table_rows, table_cols = table.nrows, table.ncols

    return (table_rows, table_cols)


def getXlsSheetNum(file_name):
    file_book = open_workbook(file_name)
    return file_book.nsheets


def testGetXlsDataByFile():
    getXlsDataByFile("./data/2016.4.25.xlsx", 0)

# testGetXlsDataByFile()
