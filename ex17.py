from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input("> ")

out_file = open(to_file, 'w')
out_file,write(indata)

print("Alright, all done.")

# 关闭out_file和in_file对应的文件。
out_file.close()
in_file.close()