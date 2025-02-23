#!/usr/bin/python3
"""for a given id return information about their TODO list"""
import sys
import json
import requests


if __name__ == '__main__':

    user_id = sys.argv[1]
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}')
    tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/todos',
        params={"userId": user_id})
    if res.status_code == 200:
        data = res.json()
        tasks = tasks.json()
        user_name = data.get("username")
        with open(f'{user_id}.json', 'w', newline='') as f:
            json.dump({f"{user_id}": [
                {
                    "task": f"{task.get('title')}",
                    "completed": task.get("completed"),
                    "username": user_name
                } for task in tasks
            ]},
                      f)
