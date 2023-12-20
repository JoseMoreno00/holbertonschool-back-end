#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    usrID = int(argv[1])
    usrDATA = requests.get(f"{url}users/{usrID}").json()
    usrTASKS = requests.get(f"{url}users/{usrID}/todos").json()
    usrcompleteTask = []

    for task in usrTASKS:
        if task["completed"]:
            usrcompleteTask.append(task)

    print(f"Employee {usrDATA['name']} is done with ", end="")
    print(f"tasks({len(usrcompleteTask)}/{len(usrTASKS)}):")

    for task in usrcompleteTask:
        print(f"\t {task['title']}")
