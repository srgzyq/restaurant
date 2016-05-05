# -*- coding:utf-8 -*- #
# 计算收入数据，求和 求平均值
import datetime
from time import sleep, strftime

# 初始化数据
test_data = [
    {"date": "2016/01/04", "income": 357, "people": 5, "company": "baidu"},
    {"date": "2016/01/04", "income": 100, "people": 2, "company": "baidu"},
    {"date": "2016/01/04", "income": 181, "people": 3, "company": "lenovo"},
    {"date": "2016/01/04", "income": 330, "people": 5, "company": "didi"},
    {"date": "2016/01/05", "income": 170, "people": 2, "company": "oracle"},
    {"date": "2016/01/05", "income": 212, "people": 3, "company": "IBM"},
    {"date": "2016/01/06", "income": 503, "people": 8, "company": "baidu"},
    {"date": "2016/01/06", "income": 470, "people": 6, "company": "didi"},
]

# 常量
DATE_FORMAT = "%Y/%m/%d"
TIME_FORMAT = "%H:%M:%S"
USER_FIRST_NAME = "srgzyq"


def welcome():
    print "欢迎, " + USER_FIRST_NAME + "."
    print "开始..."
    print "日期: " + strftime(DATE_FORMAT)
    print "当前时间: " + strftime(TIME_FORMAT)
    sleep(1)


# tools 工具函数
# 转换字符串为日期以
def getCompareDate(date_str):
    date_obj = datetime.datetime.strptime(date_str, DATE_FORMAT)
    return date_obj

# 更加日期查找数据


def getDataByDate(start, end=None):
    data = test_data
    if end == None:
        end = start

    start = getCompareDate(start)
    end = getCompareDate(end)
    result = []
    for oneData in data:
        index = getCompareDate(oneData["date"])
        if index >= start and index <= end:
            result.append(oneData)

    return result

# 计算收入的总和


def incomeSum(data):
    sum_income = 0
    for oneData in data:
        sum_income += float(oneData["income"])

    return sum_income

# 计算收入的总和对应总人数的评价值


def averagePeople(data):
    sum_income = incomeSum(data)
    sum_people = 0
    for oneData in data:
        sum_people += oneData["people"]

    average_num = sum_income / sum_people

    return average_num

# 计算公司分布，收入和人数


def companyPeopleAndIcome(data):
    result = {}
    for oneData in data:
        company_name = oneData["company"]
        income = oneData["income"]
        people = oneData["people"]
        company_data = result.get(company_name)
        if company_data == None:
            result[company_name] = {"income": income, "people": people}
        else:
            company_data["income"] += income
            company_data["people"] += people

    return result

# 公司分布以收入排序显示


def companyPrintByIncome(company_data):
    sort_income = sorted(company_data.iteritems(), key=lambda value: value[
                         1]['income'], reverse=True)
    print "公司" + " " * 8 + "收入" + " " * 4 + "人数"
    for company_info in sort_income:
        print "%-10s  %-7.2f  %-4d" % (company_info[0], company_info[1]['income'], company_info[1]['people'])

# 格式化基础信息


def printFormatInfo(data):
    print "日期 收入"
    for oneData in data:
        print "%10s, %0.2f" % (oneData["date"], oneData["income"])


def printInfo(data, start, end):
    sum_income = incomeSum(data)
    average_num = averagePeople(data)
    # printFormatInfo(data)
    print "开始: %s, 结束: %s, 收入: %0.2f, 人均: %0.2f" % (start, end, sum_income, average_num)


def startCompute():
    welcome()
    start = True
    while start:

        start_date = "2016/01/04"  # raw_input("输入查询日期开始(YY/MM/DD): ")
        end_date = "2016/01/06"  # raw_input("输入查询结束开始(YY/MM/DD): ")
        user_choice = raw_input("V 查看总收入和人均, C 查看公司分布, X 退出: ")
        user_choice = user_choice.upper()
        print ""
        result = getDataByDate(start_date, end_date)
        if user_choice == "V":
            printInfo(result, start_date, end_date)
        elif user_choice == 'C':
            company_result = companyPeopleAndIcome(result)
            companyPrintByIncome(company_result)
        elif user_choice == "X":
            start = False

startCompute()


def testCompanyPeopleAndIcome():
    test_company_data = [
        {"date": "2016/01/04", "income": 357, "people": 5, "company": "baidu"},
        {"date": "2016/01/04", "income": 100,
         "people": 2, "company": "baidu"},
        {"date": "2016/01/04", "income": 181,
         "people": 3, "company": "lenovo"},
        {"date": "2016/01/04", "income": 330,
         "people": 5, "company": "didi"},
        {"date": "2016/01/05", "income": 170,
         "people": 2, "company": "oracle"},
        {"date": "2016/01/05", "income": 212,
         "people": 3, "company": "IBM"},
        {"date": "2016/01/06", "income": 503,
         "people": 8, "company": "baidu"},
        {"date": "2016/01/06", "income": 470,
         "people": 6, "company": "didi"},
    ]
    result = companyPeopleAndIcome(test_company_data)
    companyPrintByIncome(result)
    assert result["IBM"]["income"] == 212, "erro IBM income"
    assert result["didi"]["people"] == 11, "erro didi people"
    assert result["lenovo"]["income"] == 181, "erro lenovo income"


# testCompanyPeopleAndIcome()
