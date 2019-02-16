# ex17 巩固练习2
from_file = input("input the name of the input file: ") ; to_file = input("input the name of the file being written: ") ; open(to_file, 'w').write(open(from_file).read()) ; print(f"\nCopying from {from_file} to {to_file}\n\nThe input file is {len(open(from_file).read())} bytes long\n\nAlright, all done.\n") ; open(to_file).close ; open(from_file).close

# 到底是怎么用一行代码就实现完的？？？？？？？？？？？？？？？？
# （翻到下一页后）尼玛……这有意思吗？？？？？？？？？？？？？？？？？？？？？？？？