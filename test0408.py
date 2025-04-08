print("bbbb")

import os

print("--- check lis \n")

print(os.system("ls -alh"))

print("----check df -h \n")

print(os.system("df -h"))

print("----\n")

print(os.system("pwd"))

print("--- check env\n")

print(os.system("env"))


print("--check workspace repo again /Workspace/Repos/\n")

print(os.system("ls -alh /Workspace/Repos/"))

print("--check interna folder l \n")

print(os.system("ls -alh /Workspace/Repos/.internal"))


print("-----check pod ip\n")
print(os.system("ipconfig"))
print(os.system("curl ip.sb"))

      

print("--- call other py")


/databricks/python3 --version


