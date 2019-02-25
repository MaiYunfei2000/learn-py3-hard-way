# @todo弄明白这里的代码，注释完毕，把玩完毕。PS：也可以跑去ex25-run.txt那里去注释一下命令行的运行过程。

def break_words(stuff):
    """This function will break up words for us."""
    # 将参数stuff里的字符打散，打包赋给变量words。
    words = stuff.split(' ')
    # 返回变量words的值。
    return words

# 用起这些函数！

aaa = input("Enter a 4-BYTE-STRING here, it will be broke.\n> ")
aaa0 = break_words(aaa)
print("Print bytes: ", aaa0)
#aaa1, aaa2, aaa3, aaa4 = aaa0
#print(f"Print aaa1: {aaa1}\nPrint aaa2: {aaa2}")
# 留意到了吗，这里的冒号后没有空格哦。
#print("Print aaa3:", aaa3)
#print("Print aaa4: {}".format(aaa4))

def sort_words(words):
    """Sorts the words."""
    # 似乎是将句子中的单词按首字母排序。但是使用方法未知，猜测需要先有个打包的参数集。例如用split()拆开字符串返回若干参数打包而成的参数集。
    return sorted(words)

# 用起这些函数！

bbb = sort_words(aaa0)
print("Sorting the words:", bbb)

def print_first_word(words):
    """Prints the first word after popping it off."""
    # 移除列表的第一个元素，并返回该元素的值给变量words。
    # -1则返回最后一个元素，非0或-1则为倒数第二个。（貌似？）
    word = words.pop(0)
    print(word)

# 用起这些函数！

ccc = print_first_word(bbb)

def print_last_word(words):
    """Prints the last word after popping it off."""
    # 移除列表的最后一个元素，并返回该元素的值给变量word。
    word = words.pop(-1)
    # 打印变量word。
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# 用起这些函数！

#sentence = input("Continue entering a SENTENCE here: ")
#print_first_and_last_sorted(sentence)