# [学爬虫利器XPath,看这一篇就够了 - 知乎](https://zhuanlan.zhihu.com/p/29436838)

from lxml import etree

###########################################################

"""

# 声明一段 HTML 文本
text = '''
<div>
    # <ul>: 定义无序列表
    <ul>
        # <li>: 列表的具体一条条项目
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
# 注意，最后一个 li 节点（无序列表）没有用</li>闭合，不过这可以被接下来模块进行修正

# 创建 etree.HTML 类的一个实例
html = etree.HTML(text)
# 输出修正后的 HTML 代码，不过是 bytes 类型，可用 decode() 转成 str 类型
    # bytes 类型：https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=bytes#bytes
result = etree.tostring(html)
print(type(result))
print(result.decode('utf-8'))
# 可见 li 节点的标签被补全，且自动添加了 body 和 html 节点
    # （补全有什么用呢？）@[html与xml的区别与联系（笔记） - 知乎](https://zhuanlan.zhihu.com/p/38355440#:~:text=XML%E8%A2%AB%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%9D%A5,%E7%84%A6%E7%82%B9%E6%98%AF%E6%95%B0%E6%8D%AE%E7%9A%84%E5%A4%96%E8%A7%82%E3%80%82&text=XML%20%E4%B8%8D%E6%98%AF%E8%A6%81%E6%9B%BF%E6%8D%A2HTML,%E9%9B%86%E4%B8%AD%E4%BA%8E%E6%95%B0%E6%8D%AE%E7%9A%84%E5%86%85%E5%AE%B9%E3%80%82)

'''
<html><body><div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </li></ul>
 </div></body></html>
'''

"""

###########################################################

# 另外也可直接读取文本文件来解析：

html = etree.parse('test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))
# 多了一行：
# “<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">”
# 然后就跟上一块代码所演示的没有任何区别了

###########################################################

#### 所有节点

# 用 // 开头的 XPath 规则来选取所有符合要求的节点
result = html.xpath('//*')
# print(result)

# 获取所有的 li 节点
result_li = html.xpath('//li')
# print(result_li)
# print(result_li[0])
# print(result_li[0].text)
# print(result_li[0].label)

#### 子节点

# 获取所有 li 的子节点 a
result_li_a = html.xpath('//li/a')
# print(result_li_a)
# print(result_li_a[0].text)

# 如果这样子就什么也读不出来（返回空列表），因为 a 虽然是 ul 的子孙节点但不是直接的子节点
result_ul_a = html.xpath('//ul/a')
# print(result_ul_a)
# 这样就可以
result_ul_a = html.xpath('//ul//a')
# print(result_ul_a) # 结果就跟 '//li/a' 的一样了

#### 父节点

result_parent = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/../@class')
# 详解一下上句代码中新出现的xpath语法(ref: https://www.runoob.com/xpath/xpath-syntax.html)：
    # a[@href="略略略"] : 即为选取带有此 href 属性的节点 a 
    # .. : 选取当前节点的父节点
    # @class : 选取该节点的属性；因此下面 print 出来的不是 <Element li 略略略>，而是"item-1"
# print(result_parent)
# 若把 @class 去掉，你看，又是像前面那样的 Element 对象了
result_parent = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/..')
# print(result_parent)

#### 属性匹配

# 选取 class 属性为 item-1 的 li 节点
result = html.xpath('//li[@class="item-1"]')
# print(result) # 回看前面的HTML，刚好有两个符合要求的节点

#### 文本获取

# li[@class="item-inactive"] : class 属性为 item-inactive 的节点
# /text(): 节点的文本
result = html.xpath('//li[@class="item-inactive"]/text()')
# print(result) # 咦惹，是空的呢！还是先跟教程吧！

result = html.xpath('//li[@class="item-0"]/text()')
# print(result) # 结果：['\n   ']
# 为什么是这样一个结果？因为这是 li 节点的文本，且原 html 有两个这种属性的节点，只是前一个此种节点的文本是空的（文本在节点 a 内），而后一个此种节点由于代码的自动补齐而多了个换行
# 这样才能读到节点 a 的文本
result = html.xpath('//li[@class="item-0"]/a/text()')
# print(result)

# 另一种方式，读取这些 li 节点的所有子孙节点的文本
result = html.xpath('//li[@class="item-0"]//text()')
# print(result) # 返回了三个文本

#### 属性获取

# 获取所有 li 节点下所有 a 节点的 href 属性
result = html.xpath('//li/a/@href')
# print(result)
# 获取所有 li 节点的 class 属性
result = html.xpath('//li/@class')
# print(result)

#### 属性多值匹配

# 这里的 li 节点的 class 属性有两个值 li 和 li-first
text = '''
<li class="li li-first"><a href="https://ask.hellobi.com/link.html">first item</a></li>
'''
html = etree.HTML(text)
# 用原来的方式就匹配不了了
result = html.xpath('//li[@class="li"]/a/text()')
# print(result) # 结果为空，因为无符合要求的节点

# 正确操作：把 "li li-first" 当作一个值；或者使用 contains()
result = html.xpath('//li[@class="li li-first"]/a/text()')
# print(result)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)

#### 多属性匹配

# 这里 html 有两个属性—— class 和 name ——了
text = '''
<li class="li li-first" name="item"><a href="https://ask.hellobi.com/link.html">first item</a></li>
'''
html = etree.HTML(text)
# 用逻辑运算符 and 解决，其它都跟上面一样
    # 更多见[XPath 运算符 | 菜鸟教程](https://www.runoob.com/xpath/xpath-operators.html)
    # ⚠️属性一长就得留意不要漏了右边的括号了！！！
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result)

#### 按序选择

text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)

"""
情境：有那么多个 li 节点，而有时我们只想要第 x 个节点。
"""

# 第一个 li 节点的直接子节点 a 的文本
    # XPath 语法里首个数字为 1 噢！
# print(html.xpath('//li[1]/a/text()'))

# 最后一个 li 节点的直接子节点 a 的文本
# print(html.xpath('//li[last()]/a/text()'))

# 节点序数小于 3 的，即前两个 li 节点的xxxxx的文本
# print(html.xpath('//li[position()<3]/a/text()'))

# 倒数第3个 li 节点的xxxxx的文本
    # last() 代表最后1个，减 2 就是倒数第3个啦
# print(html.xpath('//li[last()-2]/a/text()'))

##### 节点轴选择

# 轴可定义相对于当前节点的节点集。(@[XPath 轴（Axes） | 菜鸟教程](https://www.runoob.com/xpath/xpath-axes.html))

# 比前面的 html 文本多了个 span 节点 （[HTML 标签列表(字母排序) | 菜鸟教程](https://www.runoob.com/tags/html-reference.html)；[HTML <span> 标签 | 菜鸟教程](https://www.runoob.com/tags/tag-span.html)）
text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)

# 获取第一个 li 节点的所有祖先节点
    # * 表示所有节点，见本文档第 65 行代码
    # 不然最后一级仅指定了 ancestor 这个轴，没有指定任意节点，就会有xpath语法错误（lxml.etree.XPathEvalError: Invalid expression）
# print(html.xpath('//li[1]/ancestor::*')) # [<Element html at 0x102e1e4c8>, <Element body at 0x102e1e488>, <Element div at 0x102e1e448>, <Element ul at 0x102e1e948>]

# 第一个 li 节点的祖先轴的 div 节点
# print(html.xpath('//li[1]/ancestor::div'))

# 第一个 li 节点的属性轴的所有节点，即 li 节点的所有属性
# print(html.xpath('//li[1]/attribute::*'))
# DIY一下，康康有不止一个属性的情况
# print(etree.HTML('<ul><li class="aaa" name="b"></li></ul>').xpath('//li/attribute::*'))
# print(etree.HTML('<ul><li class="aaa" name="b"></li></ul>').xpath('//li/attribute::name'))

# 两者效果一样，这里没啥区别；但是在代码很复杂的真实情境下，用“轴”显然可以显著提升效率
# print(html.xpath('//li[1]/child::a[@href="https://ask.hellobi.com/link1.html"]'))
# print(html.xpath('//li[1]/a[@href="https://ask.hellobi.com/link1.html"]'))

# 第一个 li 节点的子孙轴的 span 节点
# print(html.xpath('//li[1]/descendant::span'))

# 第一个 li 节点的之后所有节点的第二个节点，看起来仅限于姊妹节点和子孙节点
# print(html.xpath('//li[1]/following::*[2]'))
# 与上个情况作对比
# print(html.xpath('//li[1]/following::*'))
# 这三个情况可以互相对比：这里的话就仅限于姊妹节点了
print(html.xpath('//li[1]/following-sibling::*'))

# 恭喜！借助 Python 正式入门 XPath ！