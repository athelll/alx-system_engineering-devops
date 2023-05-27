#!/usr/bin/python3
"""Uses this REST API: `https://jsonplaceholder.typicode.com/users'`
with given users ID returns information about his/her TODO list progress
"""

import requests
from sys import argv

if __name__ == '__main__':
    api = "https://jsonplaceholder.typicode.com"
    users = requests.get('{}/users'.format(api)).json()
    user_id = int(argv[1])
    done, total = 0, 0
    tasks = []
    found_user = None
    todos = None

    for user in users:
        if user.get('id') == user_id:
            todos = requests.get('{}/users/{}/todos'.
                                 format(api, user_id)).json()
            found_user = user

            for todo in todos:
                if todo.get('completed') is True:
                    tasks.append(todo.get('title'))
                    done += 1
                total += 1
            break

    if found_user:
        print('Employee {} is done with tasks({}/{}):'.
              format(found_user.get('name'), done, total))
        [print('\t '+i) for i in tasks]
