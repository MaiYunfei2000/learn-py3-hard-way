# 题目：编写程序，用户可以自己输入年份日期，然后计算该年份日期是当年的第几天，并用进度条显示。具体参考PPT。
#########################################
##### 不使用datetime库实现

# text is not allowed
def filter_text(v):
    
    try: return int(v) # 更一般的就换成float
    except ValueError:
        print("请输入一个整数！")
        exit(0)

# if the given year is leap year(闰年) 
def is_leapyear(iyear):
    
    if iyear % 100 == 0 and iyear % 400 == 0:
        return True
    elif iyear % 100 != 0 and iyear % 4 == 0:
        return True
    else:
        return False
    
# and then return the days of the year
rtd_year = lambda iyear: 366 if is_leapyear(iyear) == True else 365
# 代码稍微长一点的话隐式函数读起来就不舒服了……果然多数情况下还是def好看……

def rtd_month(iyear, imonth):
    
    if imonth == 2 and is_leapyear(iyear) == True:
        return 29
    elif imonth == 2 and is_leapyear(iyear) == False:
        return 28
    elif imonth in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

# calculate the days have gone this year
def cal_days(iyear, imonth, iday):
    
    months = {
        1: 31,
        2: rtd_month(iyear, 2),
        3: 31,
        4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }
    
    if (imonth in range(1, 13) and iday in range(1, months[imonth])) == False:
        print("请输入有意义的时间。")
        exit(0)
    
    today_days = 0 
    
    for i in range(1, imonth):
        today_days += months[i]
        
    today_days += iday
    
    return today_days
    
def days_progress(today_days, iyear):
    
    b = lambda iyear: 365 if is_leapyear(iyear) == False else 366
    c = b(iyear) - today_days
    print("时间进度条：\n[{}->{}]".format('×'*int(today_days/5), '-'*int(c/5)))

iyear = filter_text(input("请输入一个整数作为「年」："))
imonth = filter_text(input("请输入一个整数作为「月」："))
iday = filter_text(input("请输入一个整数作为「日」："))

today_days = cal_days(iyear, imonth, iday)

print(f"{iyear}年{imonth}月{iday}日是这一年的第{today_days}天。")
days_progress(today_days, iyear)

# 这些代码还太不简洁了……