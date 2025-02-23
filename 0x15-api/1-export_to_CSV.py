#!/usr/bin/python3
"""for a given id return information about their TODO list"""
import sys
import csv
import requests

if __name__ == '__main__':

    user_id = sys.argv[1]
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}').json()
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={"userId": user_id}).json()
    user_name = user.get("username")
    with open(f'{user_id}.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, user_name, task.get("completed"),
                             task.get("title")])
