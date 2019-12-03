# 题目：编写程序，用户可以自己输入年份日期，然后计算该年份日期是当年的第几天，并用进度条显示。具体参考PPT。
#########################################
##### 使用datetime库实现

import datetime

# text and invalid date is not allowed
def filter(v):
    
    try:
        return int(v)
    except ValueError:
        print("请输入一个整数！")
        exit(0)

iyear = filter(input("请输入一个整数作为「年」："))
imonth = filter(input("请输入一个整数作为「月」："))
iday = filter(input("请输入一个整数作为「日」："))

date0 = datetime.date(iyear, 1, 1)
date1 = datetime.date(iyear, imonth, iday)

# 输入日期date1减去年初第一天date0
days = str(date1.__sub__(date0)).split(' ', maxsplit=1)
del days[1]
days = int(days[0])+1

print(f"{date1}是这一年的第{days}天。")