import json

# id: A unique identifier for the task
# description: A short description of the task
# status: The status of the task (todo, in-progress, done)
# createdAt: The date and time when the task was created
# updatedAt: The date and time when the task was last updated

# Get
with open("db.json", "r") as file:
    file_data = json.load(file)
