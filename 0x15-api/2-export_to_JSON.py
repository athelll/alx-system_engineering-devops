#!/usr/bin/python3
"""Uses this REST API: `https://jsonplaceholder.typicode.com/users'`
with given users ID returns all information about his/her TODO list progress
and exports the data to a json documenet
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
        with open('{}.json'.format(user_id), 'w') as jsn:
            syntax_1 = []
            syntax_2 = ""
            for todo in todos:
                completed = 'true'\
                        if todo.get('completed') is True else "false"

                syntax_1.append(
                        '{{"task": "{}", "completed": {}, "username": "{}"}}'
                        .format(
                                todo.get('title'),
                                completed,
                                found_user.get('username')
                                )
                        )

                syntax_2 = ", ".join(syntax_1)
            syntax_3 = '{{"{}": [{}]}}'.format(user_id, syntax_2)
            jsn.write(syntax_3)
