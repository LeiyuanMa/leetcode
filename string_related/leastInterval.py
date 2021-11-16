# coding=utf-8
'''
@author: maleiyuan001@ke.com
@file: leastInterval.py
@time: 2021/9/8 10:35
@desc: 任务调度器，计算所有任务完成所需要的最短时间
'''
import collections

def leastInterval(tasks, n) -> int:
    task_dict = collections.defaultdict(int)
    cool_dict = dict()
    for t in tasks:
        task_dict[t] += 1
        cool_dict[t] = 1
    print(task_dict)
    print(cool_dict)
    time = 0
    for i in range(len(tasks)):
        time += 1
        minNextValid = min(cool_item[1] for cool_item in cool_dict.items() if task_dict[cool_item[0]]>0)
        time = max(time, minNextValid)

        next_task = ""
        for task_item in task_dict.items():
            task_name, task_num = task_item[0], task_item[1]
            if task_dict[task_name] and cool_dict[task_name]<=time:
                if not next_task or task_dict[task_name]>task_dict[next_task]:
                    next_task = task_name

        cool_dict[next_task] = time+n+1
        task_dict[next_task] -= 1
    return time


tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n = 2
print(leastInterval(tasks,n))