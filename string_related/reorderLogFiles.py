def reorderLogFiles(logs):
    #sorted当返回值为一个元祖时，这个元祖中的多个元素即为多个排序条件，从前到后重要程度依次降低
    def f(log):
        idx,content=log.split(' ',1)
        return (0,content,idx) if content[0].isalpha() else (1,)#这个0太精髓，前后呼应，让所有字母的在前

    return sorted(logs,key=f)


if __name__ == "__main__":
    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    print(reorderLogFiles(logs))