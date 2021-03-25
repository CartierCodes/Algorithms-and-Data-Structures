import os

def find(path, filename):
    for p in os.listdir(path):
        if os.path.isfile(os.path.join(path, p)):
            if filename in p:
                print(p)
        else:
            find(os.path.join(path, p), filename)

find("C:/Code/Bots/Discord-Bot/","main")
