import functions


events = {
    "MBH": [
        ("Mountain Range", 1234567890), 
        ("new vista", 1234567899)
        ],
    "MBA": []
}
    




def toRunEverySecond():
    for x in events:
        for i in events[x]:
            if (i[1] == 1234567890):
                functions.start(x, i[0])

toRunEverySecond()