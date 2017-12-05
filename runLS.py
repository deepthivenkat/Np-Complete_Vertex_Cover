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
    otherpath = "../Data/as-22july06.graph"
    #for j in range(9,11):
    for k in range(1,3):
            #timeval = j * 60
        seedval = int(random.random() * 1000)
        stringval = "python runproject.py -inst %s -alg LS1 -time %d -seed %d" % (otherpath, 480, seedval)
        os.system(stringval)
