# 统计文本文件中使用频度前十的单词，并按频度高低排列，统计结果中的词频和单词间用逗号隔开，存储到result.txt文件中。所要数据看附件aa.txt。

textfile = open('aa.txt', encoding='UTF-8')
data = textfile.read()
data = data.casefold().split()
textfile.close()


word_frequency = {}
for i in data:
    word_frequency[i] = 0
for i in data:
    word_frequency[i] = word_frequency[i]+1


wordlist = []
for word, frequency in word_frequency.items():
    wordlist.append((frequency, word))
wordist = wordlist.sort(reverse = True)


target = open('result.txt', 'w+')
for i,j in wordlist:
    target.write(f'{i}, {j}\n')
target.close()