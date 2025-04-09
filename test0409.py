print("aaabb")

import os
import sys

print("---check args\n")

print(sys.argv)

print("--- check lis \n")

print(os.system("ls -alh"))

print("----check df -h \n")

print(os.system("df -h"))

print("---pwd-\n")

print(os.system("pwd"))

print("--check detail folder --\n")

print(os.system("ls -alh /Workspace/Repos/.internal/ed64b03102_commits"))

print(os.system("du -d1 -h /Workspace/Repos/.internal/ed64b03102_commits"))

print(os.system("touch /Workspace/Repos/.internal/ed64b03102_commits/4bed78f1a021b3f385df81821225c67b60b26a93/abc"))


print(os.system("ls -alh /Workspace/Repos/.internal/ed64b03102_commits/4bed78f1a021b3f385df81821225c67b60b26a93"))

print(os.system("du -d1 -h  /Workspace/Repos/.internal/ed64b03102_commits/4bed78f1a021b3f385df81821225c67b60b26a93"))


print("--check another --\n")


print(os.system("ls -alh /Workspace/Repos/.internal/ed64b03102_commits/41aaba4bcef2f620c010bdf6ba3886ee9fdea0b7"))

print(os.system("cd  /Workspace/Repos/.internal/ed64b03102_commits/41aaba4bcef2f620c010bdf6ba3886ee9fdea0b7 && git status"))


# print("---check uses\n")
# print(os.system("du -d1 -h /Workspace/Users/"))




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

      
