import argparse
import json

from scripts import *

# id: A unique identifier for the task
# description: A short description of the task
# status: The status of the task (todo, in-progress, done)
# createdAt: The date and time when the task was created
# updatedAt: The date and time when the task was last updated

# Get

# Read file and save directly into dict => tasks
with open("db.json", "r") as file:
    tasks = json.load(file)

tasks = add_new(tasks, description=input("Enter a task: "))

with open("db.json", "w") as file:
    json.dump(tasks, file, indent=4)

print(tasks)