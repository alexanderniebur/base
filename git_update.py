from json import loads
from os import system

def main():
    data = getData()
    if data:
        updateTrees(data["repos"])


def getData():
    file = open("data.json")
    info = "".join(str(x) for x in file.readlines())
    file.close()
    try:
        info = loads(info)
    except:
        print("Something went wrong reading file")
        info = None
    return info

def updateTrees(repos : list):
    system("git add -A")
    system("git commit -m \"Pre import\"")
    for i in range(len(repos)):
            system("git subtree pull --prefix=%s %s master" % (repos[i]['prefix'], repos[i]['remote']))
    

main()

