print("bbbb")

import os
import sys

print("---check args\n")

print(sys.argv)

print("--- check lis \n")

print(os.system("ls -alh"))

print("----check df -h \n")

print(os.system("df -h"))

print("----\n")

print(os.system("pwd"))

print(os.system("ls -alh /Workspace/Repos/.internal/ed64b03102_commits"))

print("--- check env\n")

print(os.system("env"))


print("--check workspace repo again /Workspace/Repos/\n")

print(os.system("ls -alh /Workspace/Repos/"))

print("--check interna folder l \n")

print(os.system("ls -alh /Workspace/Repos/.internal"))


print("-----check pod ip\n")
print(os.system("ifconfig"))
      
print(os.system("curl ip.sb"))




print("--- call other py")

print(os.system("ls /databricks/python3"))


print("---check /dbfs\n")
print(os.system("ls -alh /dbfs"))

print("--- check /Volumes")

print(os.system("ls -alh /Volumes"))

print("---check /workspace\n")

print(os.system("ls -alh /Workspace"))

print("--check /\n")
print(os.system("ls -alh /"))

      



