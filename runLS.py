import os, random

inpath = "../Data/"

def runLS1():
    for i in os.listdir(inpath):
        for j in range(1,11):
            for k in range(1,11):
                pathval = inpath + str(i)
                timeval = j * 60
                seedval = int(random.random() * 1000)
                stringval = "python runproject.py -inst %s -alg LS1 -time %d -seed %d" % (pathval, timeval, seedval)
                os.system(stringval)

def test():
    thepath = inpath + "karate.graph"
    otherpath = "../Data/power.graph"
    for j in range(1,11):
        for k in range(1,11):
            timeval = j * 60
            seedval = int(random.random() * 1000)
            stringval = "python runproject.py -inst %s -alg LS1 -time %d -seed %d" % (otherpath, timeval, seedval)
            os.system(stringval)
