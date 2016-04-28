# -*- coding: utf-8 -*-
import xlwt
import xlrd
import myLogging

fmts = [
	'YY/MM/DD'
 ]

IGNORE_NAME = [u'基础信息']

"""
	合并多张xls表格为一张
"""
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

			# 日志输出:
			myLogging.logging.info("init sheet and title content.")

		
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
						# 输入格式化 to do list
						if from_xls_sheet.row_types(row_index)[col] == 3:
							style = xlwt.XFStyle()
							style.num_format_str = fmts[0]
							sheet_xls.write(row_index+xls_sheet_content_index[sheet_name],col,value,style)
						else:
							sheet_xls.write(row_index+xls_sheet_content_index[sheet_name],col,value)
						
				# 偏移量除去第一行
				xls_sheet_content_index[sheet_name] += sheet_rows -1

		# 日志输出:
		myLogging.logging.info(file_name+" merge to"+to_file_name + " succefull...")

	xls_file.save(to_file_name)


"""
	汇总一周数据总项
"""
def getSumWeeklyXlsFile(from_file_name,to_file_name):
	#file_book = open_workbook(from_file_name)
	# sheet表格内容
	#table = file_book.sheet_by_index(sheet_index)
	pass

def testMergeMoreXlfFileData():
	from_file_names = ["./data/2016.4.11.xlsx","./data/2016.4.12.xlsx","./data/2016.4.13.xlsx","./data/2016.4.14.xlsx","./data/2016.4.15.xlsx","./data/2016.4.16.xlsx","./data/2016.4.17.xlsx"]
	to_file_name = u"./data/4月/3.xls"
	myLogging.logging.info("Merge File Xls staring...")
	mergeMoreXlfFileData(from_file_names,to_file_name)
	myLogging.logging.info("Merge File Xls succefull")

testMergeMoreXlfFileData()



	

