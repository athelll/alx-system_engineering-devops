#!/usr/bin/python3
"""Uses this REST API: `https://jsonplaceholder.typicode.com/users'`
with given users ID returns all information of all users TODO list
and exports the data to a json documenet
"""

import requests
from sys import argv

if __name__ == '__main__':
    api = "https://jsonplaceholder.typicode.com"
    users = requests.get('{}/users'.format(api)).json()
    file = 'todo_all_employees'
    todos = None
    syntax_3 = []
    syntax_4 = ""

    for user in users:
        todos = requests.get('{}/users/{}/todos'.
                             format(api, user.get('id'))).json()

        syntax_1 = []
        syntax_2 = ""

        for todo in todos:
            completed = 'true'\
                    if todo.get('completed') is True else "false"

            syntax_1.append(
                    '{{"username": "{}", "task": "{}", "completed": {}}}'
                    .format(
                            user.get('username'),
                            todo.get('title'),
                            completed
                            )
                    )

            syntax_2 = ", ".join(syntax_1)
        syntax_3.append('"{}": [{}]'.format(user.get('id'), syntax_2))

    syntax_4 = ", ".join(syntax_3)
    with open('{}.json'.format(file), 'w') as jsn:
        jsn.write('{')
        jsn.write(syntax_4)
        jsn.write('}')
