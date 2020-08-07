# [Driver requirements :: Documentation for Selenium](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)
# [2. Getting Started — Selenium Python Bindings 2 documentation](https://selenium-python.readthedocs.io/getting-started.html)
# [4. Locating Elements — Selenium Python Bindings 2 documentation](https://selenium-python.readthedocs.io/locating-elements.html?highlight=driver.find_element_by_name#locating-by-name)

# Simple assignment
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

driver = Chrome(executable_path='/opt/WebDriver/bin/chromedriver')

"""
# Or use the context manager
with Chrome as driver:
    # your code inside this indent
"""

########################################
# Open the web page
########################################

driver.get("http://www.gzlib.org.cn/")
print(">>> driver.title:", driver.title)

########################################
# 练习一波读取元素
########################################

##### 4.1. Locating by Id

# //*[@id="cityIcon"]
city_icon = driver.find_element_by_id('cityIcon')

##### 4.2. Locating by Name

# //*[@id="q"]
q = driver.find_element_by_name('q')

##### 4.3. Locating by XPath

login = driver.find_element_by_xpath('//a[@title="登录"]')

##### 4.4. Locating Hyperlinks by Link Text

# these two take the same effect if thers's only one text
# using '关于进一步'
# //*[@id="gtggtoplist"]/li/a
more = driver.find_element_by_link_text('关于进一步扩大有序开放的通告')
more = driver.find_element_by_partial_link_text('关于进一步')
# emm这种临时公告很快就会没掉了

##### 4.5. Locating Elements by Tag Name

# /html/head/title
renew = driver.find_element_by_tag_name('title')

##### 4.6. Locating Elements by Class Name

# //*[@id="changeSkip"]
change_skip = driver.find_element_by_class_name('changeSkip')

##### 4.7. Locating Elements by CSS Selectors

# /html/body/div[1]
header = driver.find_element_by_css_selector('div.header')

########################################
# 然后随便操作一下
########################################

# 你可以先在输入框里（对应上面找到的 q ）随便输入一些东西
# 然后运行这行，发现你输入的文字被清掉了！
# 这种情况可以对付文本框里已默认填充一些文字的情况
q.clear()

# 给文本框输入文字
q.send_keys("深度学习")

# 然后回车！
q.send_keys(Keys.RETURN)

# 关掉页面（仅限于最初调用 .get 方法打开的那个页面）
driver.close()

# COOL!!!