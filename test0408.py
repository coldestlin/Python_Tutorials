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


print("--check file again\n")

print(os.system("ls -alh /Workspace/Repos/"))

print("--check internal \n")

print(os.system("ls -alh /Workspace/Repos/.internal"))



print("--- call other py")



python --version
