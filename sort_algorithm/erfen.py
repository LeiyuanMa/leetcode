def merge_search( li , item ):
    #获取li的开始 结束
    start = 0
    end = len(li)-1

    #只要start和end 还没错开 就一直找
    while start <= end :
        #通过计算获取当前查找范围的中间位置
        mid = (start + end)//2
        #如果中间数就是item则返回True
        if li[mid] == item :
            return mid
        #如果mid比item大，说明item可能会出现在mid左边，对左边再查找
        elif li[mid]> item :
            end = mid - 1
        # mid 比item小，说明item有可能在mid右边，对右边再查找
        else :
            start = mid + 1
    #跳出循环说明没找到 返回错误
    return False

if __name__ == '__main__':
    li = [-1,0,3,5,9,12]
    print(merge_search(li , 9) ) #True
    print(merge_search(li , 0) ) #False