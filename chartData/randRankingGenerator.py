import random

def funct(_id):
    c = 2000
    arrFinal = []
    arrRanges = []
    d = {
        "name": "chartData",
        "id": _id,
        "final values": arrFinal,
        "ranges": arrRanges
    }

    for x in range(random.randrange(5, 15)):
        arrItemFinal = []
        arrItemRanges = []
        
        exact = random.randrange(1, 250)
        rangeHigh = exact + random.randrange(1, 20)
        rangeLow = exact - random.randrange(1, 20)

        arrItemFinal.append(c)
        arrItemFinal.append(exact)

        arrItemRanges.append(c)
        arrItemRanges.append(rangeLow)
        arrItemRanges.append(rangeHigh)
        
        arrFinal.append(arrItemFinal)
        arrRanges.append(arrItemRanges)
        c += 1
    return d
def generateFiles(amount):
    for i in range(1, amount + 1):
        filePath = "chartData" + str(i) + ".json"
        file = open(filePath, "w")
        file.write(str(funct(i)))
        file.close()
    print("done")
def generateBigFile(amount):
    filePath = "chartBigData.json"
    file = open(filePath, "w")
    d = {}
    for i in range(amount):
        d[i] = funct(i + i)
    file.write(str(d))
    file.close()
    print("done")
generateFiles(5)
generateBigFile(5)
