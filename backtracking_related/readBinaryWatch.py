def readBinaryWatch(num):
    return [f"{h}:{m:02d}" for h in range(12) for m in range(60) if (bin(h)+bin(m)).count('1') == num]

if __name__ == "__main__":
    num = 1
    result = readBinaryWatch(num)
    print(result)