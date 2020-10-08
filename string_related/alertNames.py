def alertNames(keyName, keyTime):
    hashamp = {}
    for i in range(len(keyName)):
        time = keyTime[i].split(":")
        time = int(time[0])*60 + int(time[1])
        if keyName[i] not in hashamp:
            hashamp[keyName[i]] = [time]
        else:
            hashamp[keyName[i]].append(time)
    for name in hashamp.keys():
        hashamp[name].sort()
    lst = []
    for name in hashamp.keys():
        for i in range(len(hashamp[name])-2):
            if 0 < hashamp[name][i+2]-hashamp[name][i] <= 60:
                lst.append(name)
                break
    lst.sort()
    return lst

if __name__ == "__main__":
    keyName = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]
    keyTime = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]
    alertNames(keyName,keyTime)