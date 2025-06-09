import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("file does not exist")

os.rmdir("empty")