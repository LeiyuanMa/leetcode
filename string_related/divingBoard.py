def divingBoard( shorter: int, longer: int, k: int):
    if not k:
        return []
    if shorter == longer:
        return [shorter * k]
    res = [0] * (k + 1)
    for i in range(k + 1):
        res[i] = shorter * (k - i) + longer * i
    return res



if __name__ == "__main__":
    shorter = 1
    longer = 2
    k = 3
    print(divingBoard(shorter,longer,k))