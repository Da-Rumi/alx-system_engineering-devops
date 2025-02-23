#!/usr/bin/python3
"""for a given id return information about their TODO list"""

import requests
import sys


if __name__ == '__main__':

    res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}')
    tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos')
    done_tasks = []
    if res.status_code == 200:
        data = res.json()
        tasks = tasks.json()
        all_tasks = len(tasks)
        for task in tasks:
            if task.get("completed") is True:
                done_tasks.append(task.get("title"))
        print(f'Employee {data.get("name")} is done '
              f'with tasks({len(done_tasks)}/{all_tasks}):')
        print('\n'.join('\t ' + task for task in done_tasks))
