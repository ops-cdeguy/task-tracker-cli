# status = {"todo", "in-progress", "done"}
from datetime import datetime
from zoneinfo import ZoneInfo


def add_new(tasks: list, description: str):
    next_id = max([task["id"] for task in tasks], default=-1) + 1

    new_task = {
        "id": next_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now(ZoneInfo("Asia/Singapore")).isoformat(),
        "updatedAt": datetime.now(ZoneInfo("Asia/Singapore")).isoformat(),
    }
    tasks.append(new_task)
    return tasks
