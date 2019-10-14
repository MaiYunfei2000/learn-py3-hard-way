# 此练习学习**类**(class)；顺便入门洗脑OOP(object oriented programming，面向对象编程)。
# 但是还有很多内容没理解到位。


# 建立一个名为Song的类。所以这个object是什么意思？哦，见ex41第一页。
class Song(object):
    
    # 定义函数__init__，含有两个参数self和lyrics
    def __init__(self, lyrics):
        # 这是什么意思？不过貌似可以把self.lyrics整体当作一个变量名
        self.lyrics = lyrics
    
    # 定义函数sing_me_a_song，含有一个参数self
    def sing_me_a_song(self):
        # 将self.lyrics的每一个值赋给变量line
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
# 在这里，这一堆**字符串列表**是丢进去object，可丢进去后到底发生了什么？
# 还是说，这里还没丢进去，只是给了这么一堆东西在这里？这或许就说得通了。
# 也就是：“将这堆东西作为Song类的对象赋给变量happy_bday”？

# 将变量happy_bday里的Object赋给Class类里的函数sing_me_a_song()
# 或者是把这个变量名作为参数丢进这个函数？
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# 总之大概就是调用了这些函数……
# 以及__init__函数到底是干什么的？

'''
代码破坏：如果摘掉bulls_on_parade等于号后面的"Song()"会发生什么？

AttributeError: 'list' object has no attribute 'sing_me_a_song'

属性错误：「列表」对象没有一个叫做'sing_me_a_song'的属性。

看不懂……先放放
'''