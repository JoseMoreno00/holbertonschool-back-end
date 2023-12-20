#!/usr/bin/python3
"""
script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        url = "https://jsonplaceholder.typicode.com/"

        usrID = int(argv[1])
        usrDATA = requests.get(f"{url}users/{usrID}").json()
        usrTASKS = requests.get(f"{url}users/{usrID}/todos").json()
        usrcompleteTask = []

        with open('{}.json'.format(usrID), 'w+') as file:
            for todo in usrTASKS:
                task = {"task": todo.get("title"),
                    "completed": todo.get("completed"), "username": usrDATA}
                usrcompleteTask.append(task)
            data = {usrID: usrcompleteTask}
            file.write(json.dumps(data))
