"""
🕷练习：尝试爬取 lagou 网以 Python 为关键词的招聘信息信息
"""

import time
import pandas as pd
from datetime import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

# ========================================
# 初始化
# ========================================

# 查找的职业关键词
job_key = 'Python'
# job_key = input("请输入职业的关键词（可中文）：")

# 获取当前时间
today_time_str = str(datetime.today())[:16]
print(f"\n当前时间：{today_time_str}\n")

# # 禁止图片和 css 加载
# options = Options()
# prefs = {"profile.managed_default_content_settings.images": 2,'permissions.default.stylesheet':2}
# options.add_experimental_option("prefs", prefs)

# Chrome Driver
ChromeDriverPath = '/opt/WebDriver/bin/chromedriver'
try:
    driver = Chrome(executable_path=ChromeDriverPath, chrome_options=options)
except NameError:
    driver = Chrome(executable_path=ChromeDriverPath)

# ========================================
# 打开网页
# ========================================

print("正在加载网页......")
print("（标签页的圈圈转完才意味着加载完毕；视网络条件，有时可能要等待略久）")
driver.get(f"https://www.lagou.com/jobs/list_{job_key}/")
print("\n网页加载完毕。请先登录。")

# 等待这个莫名其妙的红包广告出现
element = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/div/div[2]')))
# 然后把这莫名其妙的红包广告给点掉（点击“给也不要”按钮）
closing_button = driver.find_element_by_xpath('/html/body/div[9]/div/div[2]')
closing_button.click()

# 点开登录界面
login_access = driver.find_element_by_xpath('//*[@id="lg_tbar"]/div/div[2]/ul/li[3]/a')
login_access.click()

def normal_login():
    """
    普通登录（未能解决自动验证问题）
    """
    # 输入账号信息
    id_input = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div[3]/div[1]/div/div[1]/form/div[1]/div/input')
    pass_input = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div[3]/div[1]/div/div[1]/form/div[2]/div/input')
    user_id = 'NONE'
    password = 'NONE'
    id_input.send_keys(user_id)
    pass_input.send_keys(password)

    # 点击“登录”
    login_button = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div[3]/div[2]/div[2]/div[2]')
    login_button.click()

def qq_login():
    # 网络接口过于垃圾，放弃。。。
    """
    使用 QQ 账号登录
    """
    # 选择 QQ 账号登录入口
    # qq_login = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div[3]/div[4]/div/a[3]')
    qq_login = driver.find_element_by_xpath('//*[@id="img_out_572353500"]')
    qq_login.click()

    # 使用账号密码登录
    not_discovered = True
    while not_discovered:
        try:
            id_login = driver.find_element_by_xpath('//*[@id="switcher_plogin"]')
            not_discovered = False # //*[@id="switcher_plogin"]
        except NoSuchElementException:
            print("Still trying...")
            time.sleep(0.5)
    id_login.click()

    # 点击授权并登录
    authorization = driver.find_element_by_xpath('//*[@id="login_button"]')
    authorization.click()

# qq_login()

# # 再解决一次红包广告
# closing_button = driver.find_element_by_xpath('/html/body/div[9]/div/div[2]')
# closing_button.click()

probe = input("请手动登录，然后输入任意字符以继续。")

# 获取招聘信息的总页数
page_num = driver.find_element_by_xpath('//*[@id="s_position_list"]/div[2]/div/span[5]').text
page_num = int(page_num)

# ========================================
# 爬取所有信息
# ========================================

def scrape_and_process(inner_interval=0.05, outer_interval=1):
    """
    input:
          inner_interval(int): time interval of scraping an element
          outer_interval(int): time interval of opening a new page
    output:
          df(pandas.DataFrame): cummulated information
    """

    list_job_name = []
    list_city = []
    list_district = []
    list_time_published = []
    list_salary = []
    list_experience = []
    list_education = []
    list_company = []
    list_domain = []
    list_financing = []
    list_scale = []
    list_keyword = []
    list_remark = []

    for page_i in range(1, page_num+1):
        print("\n# " + "=" * 50)
        print(f"# 正在读取第 {page_i:>2} 页信息...")
        print("# " + "=" * 50)

        # 使用 class_name 抓取所有招聘信息节点
        all_elements = driver.find_elements_by_class_name('con_list_item')
        # 遍历每页的列表元素）
        for element_i in range(len(all_elements)):

            # ---------------------------------
            # 框定特定元素，摘取整条文本（各种招聘信息）
            # ---------------------------------

            element = all_elements[element_i]

            overall_text = element.text

            # 拆解字符串
            text_list = overall_text.split('\n')

            print(text_list)

            """
            原始信息：
            | 职业名 | 地区 | 发布时间 | 月薪&经验需求&学历需求 | 公司 | 公司领域&融资轮次&人员规模 | 关键词 | 备注 |

            范例文本：
            'python开发工程师\n[上海·徐汇区]\n2020-08-03\n8k-16k 经验1-3年 / 本科\n上海江煦信息科技\n移动互联网,硬件 / 不需要融资 / 15-50人\nPython\n“同事非常nice 俊男美女 领导也很nice”
            'python开发工程师\n[北京·海淀区]\n1天前发布\n20k-35k 经验1-3年 / 本科\n字节跳动\n文娱丨内容 / C轮 / 2000人以上\n后端开发\n“六险一金，高薪期权，弹性工作，免费三餐”'
            'python', '[西安·高新技…]', '3天前发布', '5k-10k 经验3-5年 / 大专', '鼎拓科技', '信息安全,人工智能 / 未融资 / 50-150人', '“五险一金、双休、加班少、稳定性高”'
            """

            # ---------------------------------
            # 获取具体信息
            # ---------------------------------

            job_name = text_list[0]

            location = text_list[1].strip('[]').split('·')
            city = location[0]
            try:
                district = location[1]
            except IndexError:
                district = '无'

            time_published = text_list[2] # 有待进一步处理为“绝对坐标”

            salary_et_al = ''.join(text_list[3].split(' /')).split(' ')
            salary = salary_et_al[0]
            experience = salary_et_al[1]
            education = salary_et_al[2]

            company = text_list[4]

            domain_et_al = text_list[5].split('/')
            domain = domain_et_al[0].strip()
            financing = domain_et_al[1].strip()
            scale = domain_et_al[2].strip()

            keyword = ';'.join(text_list[6].split(" "))
            try:
                assert keyword[0] != "“" and keyword[-1] != "”"
            except AssertionError:
                print(f"第{page_i}页第{element_i+1}行数据可能有问题")
                keyword = "无"

            remark = text_list[-1]
            try:
                assert remark[0] == "“" and remark[-1] == "”"
            except AssertionError:
                print(f"第{page_i}页第{element_i+1}行数据可能有问题")
                remark = "【可能异常】" + remark


            list_job_name.append(job_name)
            list_city.append(city)
            list_district.append(district)
            list_time_published.append(time_published)
            list_salary.append(salary)
            list_experience.append(experience)
            list_education.append(education)
            list_company.append(company)
            list_domain.append(domain)
            list_financing.append(financing)
            list_scale.append(scale)
            list_keyword.append(keyword)
            list_remark.append(remark)

            time.sleep(inner_interval)

        print("\n# " + "=" * 50)
        print(f"# 第 {page_i:>2} 页信息读取完毕。")
        print("# " + "=" * 50)

        # ---------------------------------
        # 跳至下一页
        # ---------------------------------

        # 定位“下一页”按钮
        next_page = driver.find_element_by_xpath('//*[@id="s_position_list"]/div[2]/div/span[@action="next"]')

        # 点击“下一页”按钮
        next_page.click()

        time.sleep(outer_interval)

    # ---------------------------------
    # 创建 Pandas DataFrame 对象
    # ---------------------------------

    df = pd.DataFrame({
        "职业": list_job_name,
        "城市": list_city,
        "区域": list_district,
        "发布时间": list_time_published,
        "月薪": list_salary,
        "经验需求": list_experience,
        "学历需求": list_education,
        "企业": list_company,
        "领域": list_domain,
        "融资": list_financing,
        "人员规模": list_scale,
        "关键词": list_keyword,
        "备注": list_remark,
    })

    return df

# ========================================
# 导出为 Excel 文件
# ========================================

# df = scrape_and_process()
#
# print("爬取结果：\n", df)
#
# df.to_excel('lagou_data.xlsx', sheet_name=f'{job_key}', index=False)

# ========================================
# 结束程序
# ========================================

# if quit:
#     driver.quit()

# print("\n程序运行完毕。")

"""
🚧待加入功能：

使用 While 循环，用户爬完一个关键词之后以另一个关键词继续收集信息
（比如，搜完“Python”之后又想搜“人工智能”了，又懒得再启动一次程序），
结果存入同一 Excel 文档的新一张 sheet 中。
"""