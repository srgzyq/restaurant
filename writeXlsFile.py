# -*- coding: utf-8 -*-
import xlwt
import xlrd
import readXlsFile
import os

from xlutils.copy import copy;


style_date = xlwt.easyxf(num_format_str='YY/MM/DD')

IGNORE_NAME = [u'基础信息']

def mergeXlsData(from_file_name, to_file_name, sheet_num):
	# to_file_name 文件是否存在 sheet_num 是否存在
	
	if os.path.isfile(to_file_name):
		ready_sheet_num = readXlsFile.getXlsSheetNum(to_file_name)
		print "ready_sheet_num",ready_sheet_num,"sheet_num",sheet_num
		copyXlsDataByFile(from_file_name,to_file_name,sheet_num)
		#if (ready_sheet_num == sheet_num+1):
		#	copyXlsDataByFile(from_file_name,to_file_name,sheet_num)
		#else:
		#	writeXlsDataByFile(from_file_name,to_file_name,sheet_num)
	else:
		# 直接 copy
		writeXlsDataByFile(from_file_name,to_file_name,sheet_num)

def mergeMoreXlfFileData(from_file_name_list,to_file_name):
	# 生成一个xls对象
	xls_file = xlwt.Workbook()
	xls_sheet_dic = {}
	# 每一次写入的偏移量
	xls_sheet_content_index = {}

	for file_index,file_name in enumerate(from_file_name_list):
		from_xls_file = xlrd.open_workbook(file_name)

		# 初始化文件
		if file_index == 0:
			# 初始化sheet 以及 title
			for sheet_index in range(from_xls_file.nsheets):
				sheet_name = from_xls_file.sheet_names()[sheet_index]
				if sheet_name not in IGNORE_NAME:
					sheet_xls = xls_file.add_sheet(sheet_name)
					xls_sheet_dic[sheet_name] = sheet_xls

					# 初始化每一个 sheet title 内容
					sheet_content = from_xls_file.sheet_by_index(sheet_index)
					for col,value in enumerate(sheet_content.row_values(0)):
						sheet_xls.write(0,col,value)

					xls_sheet_content_index[sheet_name] = 0
		
		# 初始化内容
		#print xls_sheet_dic
		for sheet_name in from_xls_file.sheet_names():
			if xls_sheet_dic.get(sheet_name) != None:
				sheet_xls = xls_sheet_dic.get(sheet_name)
				# sheet表格内容
				from_xls_sheet = from_xls_file.sheet_by_name(sheet_name)
				# sheet表格行列数
				sheet_rows,sheet_cols = from_xls_sheet.nrows,from_xls_sheet.ncols
				#print sheet_rows,sheet_cols
				# 除去表头的内容行
				for row_index in range(1, sheet_rows):
					line_data_value = from_xls_sheet.row_values(row_index)
					for col,value in enumerate(line_data_value):
						
						sheet_xls.write(row_index+xls_sheet_content_index[sheet_name],col,value)
						
				# 偏移量除去第一行
				xls_sheet_content_index[sheet_name] += sheet_rows -1

	xls_file.save(to_file_name)


def writeXlsDataByFile(read_file_name,write_file_name,sheet_num):
	# 生成一个xls对象
	write_file = xlwt.Workbook()
	# 初始化table
	sheet_name = readXlsFile.getXlsSheetNameByIndex(read_file_name,sheet_num)
	#print sheet_name
	table = write_file.add_sheet(sheet_name)
	
	# 获取文件sheet 为sheet_num的 内容
	xls_titles,xls_data = readXlsFile.getXlsDataByFile(read_file_name,sheet_num)

	for col,title in enumerate(xls_titles):
		if xlrd.XL_CELL_TEXT == title[0]:
			table.write(0,col,title[1])

	# 插入剩余内容
	for row,contents in enumerate(xls_data):
		for col,content in enumerate(contents):
			if xlrd.XL_CELL_DATE == content[0]:
				table.write(row+1,col,content[1],style_date)
			else:
				table.write(row+1,col,content[1])

	write_file.save(write_file_name)

def copyXlsDataByFile(from_file_name,to_file_name,sheet_num):
	old_xls_file = readXlsFile.getXlsTableByFileAndSheet(to_file_name)
	
	# to do list
	old_rows,old_cols = readXlsFile.getXlsTableRowAndCol(to_file_name,0)

	new_xls_table = copy(old_xls_file)
	
	# to do list
	table = new_xls_table.get_sheet(0)

	# 获取文件sheet 为0的 内容
	xls_titles,xls_data = readXlsFile.getXlsDataByFile(from_file_name,sheet_num)

	# 插入剩余内容
	for row,contents in enumerate(xls_data):
		row = row+old_rows-1
		for col,content in enumerate(contents):
			if xlrd.XL_CELL_DATE == content[0]:
				table.write(row+1,col,content[1],style_date)
			else:
				table.write(row+1,col,content[1])

	new_xls_table.save(to_file_name);

def copyAllFile(from_file_name,to_file_name):
	from_xls_file = readXlsFile.getXlsTableByFileAndSheet(from_file_name)
	tempWb = copy(from_xls_file)
	# sheet表格内容
	sheet_name = from_xls_file.sheet_names()[0]
	print sheet_name
	tempWb.save(to_file_name)

def testCopyAllFile():
	copyAllFile("./data/2016.4.11.xlsx",u"./data/4月/2.xls")

def testWriteXlsDataByFile():
	writeXlsDataByFile("./data/2016.4.11.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.12.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.13.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.14.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.15.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.16.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.17.xlsx",u"./data/4月/1.xls",0)

def testMergeXlsData():
	from_file_names = ["./data/2016.4.11.xlsx","./data/2016.4.12.xlsx","./data/2016.4.13.xlsx","./data/2016.4.14.xlsx","./data/2016.4.15.xlsx","./data/2016.4.16.xlsx","./data/2016.4.17.xlsx"]
	to_file_name = u"./data/4月/1.xls"
	for file_name in from_file_names:
		mergeXlsData(file_name,to_file_name,0)
		#mergeXlsData(file_name,to_file_name,1)

def testMergeMoreXlfFileData():
	from_file_names = ["./data/2016.4.11.xlsx","./data/2016.4.12.xlsx","./data/2016.4.13.xlsx","./data/2016.4.14.xlsx","./data/2016.4.15.xlsx","./data/2016.4.16.xlsx","./data/2016.4.17.xlsx"]
	to_file_name = u"./data/4月/3.xls"
	mergeMoreXlfFileData(from_file_names,to_file_name)

#testWriteXlsDataByFile()
testMergeMoreXlfFileData()
#testCopyAllFile()
#testMergeXlsData()
#testWriteXlsDataByFile()


	

