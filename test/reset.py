import os

for f in os.listdir(os.getcwd()):
    temp = f.split(".")
    if temp[-2] == "cryp" or temp[-2] == "dec":
        os.remove(f)