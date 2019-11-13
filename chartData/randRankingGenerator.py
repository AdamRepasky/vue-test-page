import random

def funct():
    c = 2000
    arrFinal = []
    arrRanges = []
    d = {
        "name": "chartData",
        "id": 1,
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
        file.write(str(funct()))
        file.close()
    print("done")
generateFiles(5)
