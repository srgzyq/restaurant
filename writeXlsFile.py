# -*- coding: utf-8 -*-
import xlwt
import xlrd
import readXlsFile
from xlutils.copy import copy;


style_date = xlwt.easyxf(num_format_str='YY/MM/DD')

def writeXlsDataByFile(read_file_name,sheet_name,write_file_name):
	# 生成一个xls对象
	write_file = xlwt.Workbook()
	# 初始化table
	table = write_file.add_sheet(sheet_name)
	# 获取文件sheet 为0的 内容
	xls_titles,xls_data = readXlsFile.getXlsDataByFile(read_file_name,0)

	for col,title in enumerate(xls_titles):
		if xlrd.XL_CELL_TEXT == title[0]:
			table.write(0,col,title[1])

	#print xls_data
	# 插入剩余内容
	for row,contents in enumerate(xls_data):
		for col,content in enumerate(contents):
			if xlrd.XL_CELL_DATE == content[0]:
				table.write(row+1,col,content[1],style_date)
			else:
				table.write(row+1,col,content[1])

	write_file.save(write_file_name)

def copyXlsDataByFile(from_file_name,to_file_name):
	old_xls_file = readXlsFile.getXlsTableByFileAndSheet(to_file_name)
	old_rows,old_cols = readXlsFile.getXlsTableRowAndCol(to_file_name,0)

	new_xls_table = copy(old_xls_file)
	table = new_xls_table.get_sheet(0)

	# 获取文件sheet 为0的 内容
	xls_titles,xls_data = readXlsFile.getXlsDataByFile(from_file_name,0)

	# 插入剩余内容
	for row,contents in enumerate(xls_data):
		row = row+old_rows-1
		for col,content in enumerate(contents):
			if xlrd.XL_CELL_DATE == content[0]:
				table.write(row+1,col,content[1],style_date)
			else:
				table.write(row+1,col,content[1])

	new_xls_table.save(to_file_name);

def testWriteXlsDataByFile():
	#writeXlsDataByFile("./data/2016.4.25.xlsx",u"用户",u"./data/4月/1.xls")
	#copyXlsDataByFile("./data/2016.2.22.xlsx",u"./data/4月/1.xls",)
	#writeXlsDataByFile("./data/2016.2.22.xlsx",u"用户",u"./data/4月/1.xls")
	
	writeXlsDataByFile("./data/2016.4.11.xlsx",u"用户",u"./data/4月/1.xls")
	copyXlsDataByFile("./data/2016.4.12.xlsx",u"./data/4月/1.xls",)
	copyXlsDataByFile("./data/2016.4.13.xlsx",u"./data/4月/1.xls",)
	copyXlsDataByFile("./data/2016.4.14.xlsx",u"./data/4月/1.xls",)
	copyXlsDataByFile("./data/2016.4.15.xlsx",u"./data/4月/1.xls",)
	copyXlsDataByFile("./data/2016.4.16.xlsx",u"./data/4月/1.xls",)
	copyXlsDataByFile("./data/2016.4.17.xlsx",u"./data/4月/1.xls",)


testWriteXlsDataByFile()


	

