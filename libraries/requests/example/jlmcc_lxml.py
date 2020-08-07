# 本案例爬取的页面：詹姆斯·麦克莱兰的著作目录
# (https://stanford.edu/~jlmcc/papers/)

import requests
import numpy as np
from lxml import etree

########################################
#            LOAD THE HTML
########################################

# request the page
response = requests.get('https://stanford.edu/~jlmcc/papers')
# see if success
if response:
    print('\nSuccessfully requested!\n')
else:
    print('\nAn error occurred.\n')

# get the resonse content, obviously it's a HTML document
content = response.text
# print('='*50, content, '='*50)
# print('\n↑↑↑ WEB CONTENT ↑↑↑\n')
# print('type:', type(content), '\n')

########################################
#       EXTRACT THE INFORMATION
########################################

# parse the content to HTML text
html = etree.HTML(content)
# see how does it look like
# print(etree.tostring(html))

# read the all sibling-<p> nodes after the <em> node  (except the last <p>)
"""
using the tricky copying tool of Chrome, we know we want nodes
from '/html/body/p[3]' to '/html/body/p[251]' and exclude [223]
"""

def read_elements():
    try:
        target_p = []
        for i in range(3, 221):
            # 也可以在这里后面加个 '/text' 但是结果没变
            # 一句话，很没有 bs 灵活
            element = html.xpath(f'//body/p[{i}]')[0]
            target_p.append(element)
    except IndexError:
        pass
    return target_p
# 诡异得一批，用'//body/p'只读到长为221的列表

target_p = read_elements()
# print("target_p:", len(target_p))
# >>> target_p[0].text
# '\r\n  McClelland, J. L. (2020). Exemplar models are useful and deep neural\r\n  networks overcome their limitations: A commentary on Ambridge (2020).\r\n  '

########################################
#        PROCESS THE INFORMATION
########################################

read the first part (text of <p>, authors, year and title)
def process_part1_text(string):
    """
    input  : (lxml.etree._Element.text) outer <p> node, containing
             information of the authors, year and title
    output : (dict) processed certain information
    """
    # print("string:", repr(string))
    # 把奇怪的跳行和空格给处理掉
    author_year_title = ''.join(string.split('\r\n ')).strip()
    # 再来一次
    author_year_title = ' '.join(author_year_title.split('\r\n')).strip()
    # print("[2]author_year_title:", author_year_title)
    # 分割作者、年代和文章标题
        # 只在首个符合条件地方分割一次，避免出现文章标题也有相同字符的情形
    author_year_title = author_year_title.split(' (', maxsplit=1)
    # 把作者单独拎出来
    author = author_year_title[0]
    # print("[3]author_year_title:", author_year_title)
    if author_year_title == ['']:
        return None
    # 把年份+标题拎出来
    year_title = author_year_title[1]
    # print("[4]year_title:", year_title)
    # 继续处理年份+标题，用').'将年份和标题分割
        # 只在首个符合条件地方分割一次，避免出现文章标题也有相同字符的情形
    year_title = year_title.split('). ', maxsplit=1)
    if len(year_title) == 1:
        year_title = year_title[0]
    # print("[4.5]year_title:", year_title)
    try:
        year_title = year_title.split(').', maxsplit=1)
    except AttributeError:
        pass
    # 把年份拎出来
    year = year_title[0]
    # 把标题拎出来
    # print("[5]year_title", year_title)
    title = year_title[1].strip('.')
    # 把三个信息合并到字典里
    inf_dict = {'author': author,
                 'year': year,
                 'title': title}
    return inf_dict

# write existing information into a list
all_paper_inf = []
for i in range(len(target_p)):
    # print("="*50 + '\n' + str(i) + '\n' + "="*50)
    try:
        all_paper_inf.append(process_part1_text(target_p[i].text))
    except:
        all_paper_inf.append(None)

# print(all_paper_inf)

test_output = open('test.csv', 'w+')
test_output.write('author,year,title\n')

for i in range(len(all_paper_inf)):
    try:
        test_output.write(','.join([all_paper_inf[i]['author'],
                                    all_paper_inf[i]['year'],
                                    all_paper_inf[i]['title'] + '\n']))
    except TypeError:
        pass

# wai，这么多逗号的文本用什么 csv ，还是乖乖学 Pandas 吧！

# read the second part


# 结论，别再捣鼓下去了，你只知道你需要学自然语言处理_(:з」∠)_否则这种事情真的没效率