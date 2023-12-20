#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        url = "https://jsonplaceholder.typicode.com/"

        usrID = int(argv[1])
        usrDATA = requests.get(f"{url}users/{usrID}").json()
        usrTASKS = requests.get(f"{url}users/{usrID}/todos").json()
        usrcompleteTask = []

        with open("{}.csv".format(usrID), 'w+') as file:
            for All in usrTASKS:
                data = '"{}","{}","{}","{}"\n'.format(
                    usrID, usrDATA, All.get("completed"), All.get("title"))
                file.write(data)
