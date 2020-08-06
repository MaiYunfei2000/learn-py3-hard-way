# 根据此文档来一边敲代码一边学习：[Beautiful Soup 4.4.0 文档 — Beautiful Soup 4.2.0 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id19)
# 此文档的标题及篇章结构与上官方文档相一致

# 💡此文档中定义的方法都无实际意义，仅仅是为了可以借助 TextMate 的黑科技快速跳转至任意部分罢了




from bs4 import BeautifulSoup 

##### 开始：将文档传入 BS ，得到一个文档对象

def start():
    pass

# 可以用字符串

soup = BeautifulSoup("<html>data</html>", features="lxml")
print("First soup:", soup)
print()

print(BeautifulSoup("Sacr&eacute; bleu!", features="lxml"), '\n')

# 也可以用文件句柄
    # test.html 来自这里的示例 [学爬虫利器XPath,看这一篇就够了 - 知乎](https://zhuanlan.zhihu.com/p/29436838)
soup = BeautifulSoup(open('test.html'), features="lxml")
print("HTML doc:", soup, '\n')



##### 对象种类

def bs_types():
    pass

# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment


#### Tag 对象

# 与 XML 或 HTML 原生文档中的 tag （HTML 标记/标签）相同
# Tag有很多方法和属性,在 [遍历文档树](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id19) 和 [搜索文档树](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id28) 中有详细解释
# 以下介绍tag中最重要的属性: name 和 attributes

tag = soup.li
print("type(tag)", type(tag))
# 读取了第一个 li ，那怎么读取后面的呢？
print("tag", tag, '\n')

### Name

# 每个 tag 都有自己的名字
print("tag.name", tag.name, '\n')
# 改变 tag 的 name 
tag.name = "lixxx"
print("HTML doc (changed li tag):", soup, '\n')
# 改回来
tag.name = "li"

### Attributes

# 获取标签的属性（与字典的操作方法相同，但是显然 tag 不是 dict）
print("tag['class']:", tag['class'])
# 也可以用 Python 属性的风格来获取
print("tag.attrs:", tag.attrs)
print("type(tag.attrs):", type(tag.attrs), '\n')

# tag 的属性可以被添加/删除/修改，总之，tag 的属性方法与 dict 一样
tag['class'] = 'verybold'
tag['id'] = 10086
tag['eee'] = '2333'
print("modified tag:", tag)

del tag['eee']
print("after deletion:", tag, '\n')

## 多值属性

# 在 Beautiful Soup 中多值属性的返回类型是 list
css_soup = BeautifulSoup('<p class="body strikeout"></p>',
                         features='lxml')
print("css_soup.p['class']:", css_soup.p['class'])
css_soup = BeautifulSoup('<p class="body"></p>',
                         features='lxml')
print("css_soup.p['class']:", css_soup.p['class'], '\n')

# 如果某个属性看起来好像有多个值,但在任何版本的 HTML 定义中都没有被定义为多值属性,那么 Beautiful Soup 会将这个属性作为字符串返回
id_soup = BeautifulSoup('<p id="my id"></p>',
                         features='lxml')
print("id_soup:", id_soup.p['id'])
print("id_soup.p.attrs", id_soup.p.attrs, '\n')

# 将 tag 转换成字符串时,多值属性会合并为一个值
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>',
                         features='lxml')
# 打印 rel_soup 的 标签a 的 属性rel
print(rel_soup.a['rel'])
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p, '\n')

# 如果转换的文档是XML格式,那么tag中不包含多值属性
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
print("xml_soup.p['class']", xml_soup.p['class'])
print(">> compare <<")
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
print("xml_soup.p['class']", xml_soup.p['class'], '\n')


#### NavigableString 对象 （可以遍历的字符串）

# recap
print("tag:", tag)

print("\ntag.string:", tag.string)
print("type(tag.string):", type(tag.string), '\n')

# 将 NavigableString 对象转化为 Unicode 对象
# unicode() 方法只存在于 Python 2 中，这里根据 Python 演化逻辑替换为 str()
unicode_string = str(tag.string)
print("unicode_string:", unicode_string)
print("type(unicode_string):", type(unicode_string), '\n')

# tag 中包含的字符串不能编辑,但是可以被替换成其它的字符串
tag.string.replace_with("No longer bold")
print("Replaced tag:", tag)
# 额，两者没区别诶，那上面那个函数开发出来是干什么的。。。
    # 不对，有区别！标签 a 和 span 都消失了！
print("tag.string", tag.string)
tag.string = "first item"
print("Replaced tag:", tag)


#### BeautifulSoup 对象

# BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象,它支持 遍历文档树 和 搜索文档树 中描述的大部分的方法.

# BeautifulSoup 对象包含了一个值为 “[document]” 的特殊属性 .name
print("\nsoup.name:", soup.name)


#### Comment 对象及其它特殊字符串

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'lxml')
comment = soup.b.string
print("\ntype(comment)", type(comment))
# Comment 对象是一个特殊类型的 NavigableString 对象

print("comment:", comment)

# Beautiful Soup中定义的其它类型都可能会出现在XML的文档中: CData , ProcessingInstruction , Declaration , Doctype .与 Comment 对象类似,这些类都是 NavigableString 的子类,只是添加了一些额外的方法的字符串独享.下面是用CDATA来替代注释的例子:
from bs4 import CData
cdata = CData("A CDATA block")
comment.replace_with(cdata)
# prettify() 是干嘛的？没说，搜不到
    # 不，开头就说了，输出一个按照标准的缩进格式的结构
print("\nsoup.b.prettify():\n", soup.b.prettify())



##### 遍历文档树

def navigating_the_tree():
    pass
    
# 还拿”爱丽丝梦游仙境”的文档来做例子:
html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print('\n', soup)
# 两个解析器读取的文档表面上没有什么区别，具体的之后再去探索吧
# soup = BeautifulSoup(html_doc, 'lxml')
# print('\n', soup)

#### 子节点

### tag 的名字

# 操作文档树最简单的方法就是告诉它你想获取的tag的name
print("\n" + "=" * 50 + "\n\nsoup.head:", soup.head)
print("soup.title:", soup.title)
# 可以套娃：
# 获取<body>标签中的第一个<b>标签（那第n个呢？）
print("\nsoup.body.b:", soup.body.b)
# 这两句效果一样，也就是说 bs 的路径可以跳着来
print(soup.body.p.b)
print()

# 前面这种方式只能获得第一个，那第n个呢？
# 只能先找出全部此标签，然后再索引出第n个标签
# 找出全部的 a 标签
print("soup.find_all('a'):", soup.find_all('a'))
print()

### .contents 和 .children

# tag 的 .contents 属性可以将 tag 的子节点以列表的方式输出:
head_tag = soup.head
print("head_tag:", head_tag)
print("head_tag.contents:", head_tag.contents)
print("head_tag.contents[0].contents:", head_tag.contents[0].contents)
print()

# 字符串没有 .contents 属性，因为字符串没有子节点，否则会返回 AttributeError

# 通过 tag 的 .children 生成器，可以对 tag 的子节点进行循环
for child in head_tag.contents[0].children:
    print(child)
print()

### .descendants

# .descendants 属性可以对所有tag的子孙节点进行递归循环

for child in head_tag.descendants:
    print(child)
print()

print("soup.children:", soup.children)
print("list(soup.descendants):", list(soup.descendants))
print()

### .string

title_tag = head_tag.contents[0]
print("title_tag:", title_tag)
print("title_tag.string:", title_tag.string)
print()

# 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None

print(soup.html.string, '\n')

### .strings 和 stripped_strings

# 如果tag中包含多个字符串,可以使用 .strings 来循环获取:
for string in soup.strings:
    # https://docs.python.org/zh-cn/3/library/functions.html#repr
    print('-', repr(string))
    # print('+', string)
print()

# 使用 .stripped_strings 可以去除多余空白内容:
for string in soup.stripped_strings:
    print(repr(string))
print()
# 清爽很多

#### 父节点

### .parent

title_tag = soup.title
print("title_tag:", title_tag)
print("title_tag.parent:", title_tag.parent)

# 文档title的字符串也有父节点:<title>标签
print("\ntitle_tag.string.parent:", title_tag.string.parent)

# 文档的顶层节点比如<html>的父节点是 BeautifulSoup 对象
html_tag = soup.html
print("\ntype(html_tag.parent)", type(html_tag.parent))
print(html_tag.parent)

### .parents

# 通过元素的 .parents 属性可以递归得到元素的所有父辈节点

link = soup.a
print("\nlink:", link)
for parent in link.parents:
    if parent is None:
        print('*', parent)
    else:
        print('+', parent.name)
print()

#### 兄弟节点

# 一个简单例子：
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
print("sibling_soup.prettify()", sibling_soup.prettify())
# 这里，b 和 c 就是兄弟/姊妹节点

# 在文档树中,使用 .next_sibling 和 .previous_sibling 属性来查询兄弟节点
print("\nsibling_soup.b.next_sibling:", sibling_soup.b.next_sibling)
print("sibling_soup.c.previous_sibling:", sibling_soup.c.previous_sibling)

### .next_siblings 和 .previous_siblings

# 与前面的 .descendants, .strings, .parents 同理，略去

#### 回退和前进

# 进度：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id26