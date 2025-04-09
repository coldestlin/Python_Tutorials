print("bbbb")

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

##  touch: setting times of '/Workspace/Repos/.internal/ed64b03102_commits/fff': No such file or directory
print(os.system("touch /Workspace/Repos/.internal/ed64b03102_commits/fff"))

print(os.system("du -d1 -h /Workspace/Repos/.internal/ed64b03102_commits"))

print(os.system("touch /Workspace/Repos/.internal/ed64b03102_commits/4bed78f1a021b3f385df81821225c67b60b26a93/abc"))


print(os.system("ls -alh /Workspace/Repos/.internal/ed64b03102_commits/4bed78f1a021b3f385df81821225c67b60b26a93"))

print(os.system("du -d1 -h  /Workspace/Repos/.internal/ed64b03102_commits/4bed78f1a021b3f385df81821225c67b60b26a93"))


print("--check another --\n")


print(os.system("ls -alh /Workspace/Repos/.internal/ed64b03102_commits/41aaba4bcef2f620c010bdf6ba3886ee9fdea0b7"))

print(os.system("cd  /Workspace/Repos/.internal/ed64b03102_commits/41aaba4bcef2f620c010bdf6ba3886ee9fdea0b7 && git status"))



print("---check modify file\n")

print(os.system("touch /Workspace/Repos/testfile-repo"))
print(os.system("ls -alh /Workspace/Repos/"))

print(os.system("touch /Workspace/testfile-workspace"))
print(os.system("ls -alh /Workspace/"))


## AsyncFlushFaliedException: One or more writes may have failed when writing to Databricks Workspace.
## : 400 Bad Request: DIRECTORY_PROTECTED: Folder Users is protected
## print(os.system("touch /Workspace/Users/testfile-users"))

print(os.system("touch /dbfs/testfile-dbfs"))
print(os.system("ls -alh /dbfs/"))

print(os.system("touch /Volumes/testfile-volumes"))
print(os.system("ls -alh /Volumes/"))


print("---check uses\n")
print(os.system("du -d1 -h /Workspace/Users/"))




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

      



