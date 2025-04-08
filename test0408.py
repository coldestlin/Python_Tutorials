print("bbbb")

import os

print("---\n")

print(os.system("ls -alh"))

print("----\n")

print(os.system("df -h"))
print("----\n")

print(os.system("pwd"))

print("--- check env\n")

print(os.system("env"))


print("--- call other py")

python datatest.py
