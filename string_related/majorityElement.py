"""
众数问题，需要验证众数数量是否确实多于一半
"""
def majorityElement(nums):
    if len(nums) == 0:
        return -1
    else:
        count = 0
        major = None
        for i in range(len(nums)):
            if count == 0:
                major = nums[i]
                count += 1
            else:
                if nums[i] != major:
                    count -= 1
                else:
                    count += 1
        if count > 0:
            count_identify = 0
            for i in nums:
                if i == major:
                    count_identify += 1
                    if count_identify > len(nums) / 2:
                        return major
            return -1
        else:
            return -1


if __name__ == "__main__":
    a = [1,2,5,9,5,9,5,5,5]
    print(majorityElement(a))