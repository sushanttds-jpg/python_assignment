import os
os.system("cd") 
os.system("dir")
os.system("mkdir test_folder")
os.system("type nul > test_folder\\myfile.txt") 
os.system("python --version")
os.system("del test_folder\\myfile.txt")
os.system("rmdir test_folder")
print(f"Current Directory: {os.getcwd()}")