#!/usr/bin/python3
"""Uses this REST API: `https://jsonplaceholder.typicode.com/users'`
with given users ID returns all information about his/her TODO list progress
"""

import requests
from sys import argv

if __name__ == '__main__':
    api = "https://jsonplaceholder.typicode.com"
    users = requests.get('{}/users'.format(api)).json()
    user_id = int(argv[1])
    found_user = None
    todos = None

    for user in users:
        if user.get('id') == user_id:
            todos = requests.get('{}/users/{}/todos'.
                                 format(api, user_id)).json()
            found_user = user
            break

    if found_user:
        with open('USER_ID.csv', 'w') as csv:
            for todo in todos:
                syntax = '"{}","{}","{}","{}"\n'.format(
                        found_user.get('id'),
                        found_user.get('username'),
                        todo.get('completed'),
                        todo.get('title'))
                csv.write(syntax)
