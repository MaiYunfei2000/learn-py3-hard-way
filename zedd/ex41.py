# 此练习主要是为了学习「面向对象」的术语。
# 不记得%？➡️EX37

# 调用模块random
import random
# 从？？ 调用模块urlopen
from urllib.request import urlopen
# 调用模块sys？
import sys

# 设定变量WORD_URL，将字符串“某网址”赋给此变量。
WORD_URL = "http://learncodethehardway.org/words.txt"
# 建立列表，名为WORDS。
WORDS = []

# 创建字典PHRASES，
PHRASES = {
    # 这是一个映射，不用被奇怪的符号搞晕，它们只是字符串而已（⚠️真的吗？）。
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]
    
        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)
        
    return results

# keep going until they hit CTRL-D
# 2333
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            
            print(question)
            
            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")